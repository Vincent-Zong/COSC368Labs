#!/usr/bin/env python3
import csv
import math
import argparse
from collections import defaultdict

def parse_args():
    p = argparse.ArgumentParser(
        description="Summarize Fitts's Law log: mean time per ID (skipping warm-up selections)."
    )
    p.add_argument("-i", "--input", default="fitts_log.csv", help="Input log CSV (default: fitts_log.csv)")
    p.add_argument("-o", "--output", default="summary.csv", help="Output summary CSV (default: summary.csv)")
    p.add_argument("--warmup", type=int, default=2,
                   help="Number of earliest selections per (A,W) to ignore (default: 2)")
    p.add_argument("--round-id", type=int, default=3,
                   help="Round ID to this many decimals for grouping (default: 3)")
    return p.parse_args()

def coerce_float(value):
    try:
        return float(value)
    except (TypeError, ValueError):
        return None

def read_trials(path):
    """
    Returns:
      per_aw: dict[(A, W)] -> dict[selection_num] -> time_seconds
    """
    per_aw = defaultdict(dict)

    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        headers = [h.strip() for h in (reader.fieldnames or [])]

        # Column detection (compatible with original and revised logs)
        col_distance = next((h for h in headers if h.lower() in {"distance", "amplitude", "a"}), None)
        col_width    = next((h for h in headers if h.lower() in {"width", "w"}), None)
        col_sel      = next((h for h in headers if h.lower() in {"selection#", "selection", "trialincondition", "trial"}), None)
        col_time_ms  = next((h for h in headers if h.lower() in {"time_ms", "time (ms)", "timems"}), None)
        col_time     = next((h for h in headers if h.lower() in {"time", "t"}), None)
        col_time_s   = next((h for h in headers if h.lower() in {"time_s", "time (s)", "times"}), None)
        col_correct  = next((h for h in headers if h.lower() in {"correct"}), None)

        # Sequential fallback for selection numbers per (A,W)
        counters = defaultdict(int)

        for row in reader:
            # Exclude incorrect trials if 'Correct' column exists
            if col_correct is not None:
                try:
                    if int(float(row[col_correct])) != 1:
                        continue
                except Exception:
                    pass

            # Parse A and W
            try:
                A = int(float(row[col_distance])) if col_distance else None
                W = int(float(row[col_width])) if col_width else None
            except Exception:
                continue
            if A is None or W is None:
                continue

            # Selection number
            sel_num = None
            if col_sel:
                try:
                    sel_num = int(float(row[col_sel]))
                except Exception:
                    sel_num = None
            if sel_num is None:
                counters[(A, W)] += 1
                sel_num = counters[(A, W)]

            # Time → seconds
            t_seconds = None
            if col_time_ms and row.get(col_time_ms):
                v = coerce_float(row[col_time_ms])
                if v is not None:
                    t_seconds = v / 1000.0
            if t_seconds is None and col_time and row.get(col_time):
                v = coerce_float(row[col_time])
                if v is not None:
                    # Heuristic: if large, assume ms; else seconds
                    t_seconds = v / 1000.0 if v > 20 else v
            if t_seconds is None and col_time_s and row.get(col_time_s):
                v = coerce_float(row[col_time_s])
                if v is not None:
                    t_seconds = v

            if t_seconds is None:
                continue

            per_aw[(A, W)][sel_num] = t_seconds

    return per_aw

def summarize_by_id(per_aw, warmup_drop, id_decimals):
    """
    Returns:
      dict[id_key] -> list of times (seconds)
      where id_key is ID rounded to `id_decimals`.
    """
    times_by_id = defaultdict(list)
    for (A, W), sel_map in per_aw.items():
        if not sel_map:
            continue
        # Drop first N selections per (A,W)
        sel_nums = sorted(sel_map.keys())
        kept = [sel_map[n] for n in sel_nums[warmup_drop:]] if len(sel_nums) > warmup_drop else []
        if not kept:
            continue

        # Compute ID once for this (A,W)
        ID = math.log2(A / W + 1.0)
        id_key = round(ID, id_decimals)

        # Add all kept times under this ID bin
        times_by_id[id_key].extend(kept)

    return times_by_id

def write_summary_id(path, times_by_id, id_decimals):
    """
    Writes CSV with columns: ID, mean time (seconds)
    Sorted by increasing ID.
    """
    rows = []
    for id_key, times in times_by_id.items():
        if not times:
            continue
        mean_time = sum(times) / len(times)
        rows.append((id_key, mean_time))

    rows.sort(key=lambda r: r[0])

    with open(path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "mean time"])
        for ID, mean_time in rows:
            writer.writerow([f"{ID:.{id_decimals}f}", f"{mean_time:.3f}"])

def main():
    args = parse_args()
    per_aw = read_trials(args.input)
    times_by_id = summarize_by_id(per_aw, warmup_drop=args.warmup, id_decimals=args.round_id)
    write_summary_id(args.output, times_by_id, id_decimals=args.round_id)
    print(f"Wrote {args.output} with mean times per ID "
          f"(dropped first {args.warmup} selections per A,W; ID rounded to {args.round_id} dp).")

if __name__ == "__main__":
    main()

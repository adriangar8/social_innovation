#!/bin/bash

output_dir="/home/adriangar8/Documents/academia/year3/semester2/social_innovation/social_innovation_repo/traditionalVSquantum/quantum/out_metrics/QAOA_out"

echo -1 | sudo tee /proc/sys/kernel/perf_event_paranoid

# Time metrics
perf stat python QAOA.py > "${output_dir}/exeTime_metrics.txt" 2>&1
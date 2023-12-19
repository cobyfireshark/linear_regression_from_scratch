#!/bin/bash
# setup_logs.sh

log_base_dir="/var/log/regression"

if [ ! -d "$log_base_dir" ]; then
    echo "making $log_base_dir"
    mkdir -p "$log_base_dir"
fi

log_names=("cost_function" "create_training_set" "linear_regression_gd")

# Loop through each log name
for log_name in "${log_names[@]}"; do
    log_path="$log_base_dir/${log_name}.log"
    echo "making $log_path..."
    touch "$log_path"
    echo "setting permissions 666"
    chmod 666 "$log_path"
done
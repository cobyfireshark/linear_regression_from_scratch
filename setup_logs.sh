#!/bin/bash
# setup_logs.sh

log_dir="/var/log/regression"

if [ ! -d "$log_dir" ]; then
    echo "making $log_dir"
    mkdir -p "$log_dir"
fi

log_path="$log_dir/cost_function.log"
echo "making $log_path"
touch "$log_path"

chmod 666 "$log_path"
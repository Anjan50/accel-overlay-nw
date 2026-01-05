#!/bin/bash

set -e
for file in /sys/class/net/*/queues/rx-*/rps_flow_cnt; do \
    echo 32768 > $file; \
    echo "$file"; \
    cat $file; \
done

# echo 32768 > /proc/sys/net/core/rps_sock_flow_entries
# echo "/proc/sys/net/core/rps_sock_flow_entries";
# cat /proc/sys/net/core/rps_sock_flow_entries

echo 'Enabled RFS on all interfaces'
#!/bin/bash

set -e
for file in /sys/class/net/*/queues/rx-*/rps_cpus; do \
    echo 7 > $file; \
    echo "$file"; \
    cat $file; \
done

echo 'Enabled RPS on all interfaces'
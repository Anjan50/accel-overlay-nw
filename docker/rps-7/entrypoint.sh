#!/bin/sh
set -e
mount -o remount,rw /sys
/usr/local/bin/enable_rps.sh
exec iperf3 "$@"
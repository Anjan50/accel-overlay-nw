#!/bin/sh
set -e
mount -o remount,rw /sys
/usr/local/bin/enable_rfs.sh
exec iperf3 "$@"
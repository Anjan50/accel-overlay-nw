#!/bin/bash

enable_rfs() {
  local interface=$1
  local flow=32768 
  for queue in /sys/class/net/$interface/queues/rx-*; do
    echo $flow > $queue/rps_flow_cnt
  done
}

echo 32768 > /proc/sys/net/core/rps_sock_flow_entries

enable_rfs eth1
enable_rfs vxlan.calico
enable_rfs calib3c61c3cba9
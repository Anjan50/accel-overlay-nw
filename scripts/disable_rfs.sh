#!/bin/bash

disable_rfs() {
  local interface=$1
  local flow=0 
  for queue in /sys/class/net/$interface/queues/rx-*; do
    echo $flow > $queue/rps_flow_cnt
  done
}

echo 0 > /proc/sys/net/core/rps_sock_flow_entries

disable_rfs eth1
disable_rfs vxlan.calico
disable_rfs calib3c61c3cba9
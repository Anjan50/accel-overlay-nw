#!/bin/bash

# need to enable RPS in both the virtio NIC and VXLAN interface
disable_rps() {
  local interface=$1
  for queue in /sys/class/net/$interface/queues/rx-*; do
    echo 0 > $queue/rps_cpus
  done
}

disable_rps eth1
disable_rps vxlan.calico
disable_rps calib3c61c3cba9
#!/bin/bash

SERVER_IP=$2
NUM_RUNS=20
FIRST_ARG=$1

cpu_charts=""
numbers=""
cpu_data=""

for i in $(seq 1 $NUM_RUNS); do
  echo "Running experiment $i..."
  output=$(./deploy_experiment_rps.sh $FIRST_ARG $SERVER_IP)
  if [ $? -ne 0 ]; then
    echo "Experiment $i failed to run."
    exit 1
  fi
  echo "Experiment $i completed."
  sleep 5
  
  cpu_chart=$(echo "$output" | head -n -${FIRST_ARG})
  number=$(echo "$output" | tail -n ${FIRST_ARG})
  echo "$number"

  cpu_charts="${cpu_charts}${cpu_chart}\n\n"
  numbers="${numbers}${number} "
  
  cpu_data="${cpu_data}$(echo "$cpu_chart" | grep -E 'all|[0-9]+(\.[0-9]+)?' | awk '{print $NF}')\n"
done

echo -e "$cpu_charts"
echo -e "\nNumbers grid:"
echo -e "$numbers" | xargs -n $NUM_RUNS

# Process and print CPU utilization values
# cores=$(echo -e "$cpu_data" | grep -oP '^[0-9]+' | sort -u)
metrics=("idle" "soft" "sys" "usr")

for core in {0..3}; do
  for metric in "${metrics[@]}"; do
    # echo "$cpu_data"
    values=$(echo -e "$cpu_charts" | grep "Average:       $core" | awk -v metric="$metric" '{if (metric == "idle") print $12; else if (metric == "soft") print $8; else if (metric == "sys") print $5; else if (metric == "usr") print $3;}')
    echo -e "Core $core $metric: \n$values"
  done
done

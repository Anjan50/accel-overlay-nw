# Repository Structure Documentation

This document provides a detailed overview of the repository structure and the purpose of each component.

## Directory Structure

```
accel-overlay-nw/
│
├── scripts/                          # Experiment automation scripts
│   ├── deploy_experiment.sh          # Deploy baseline experiment
│   ├── deploy_experiment_rps.sh      # Deploy RPS experiment
│   ├── deploy_experiment_rfs.sh      # Deploy RFS experiment
│   ├── deploy_experiment_rps_7.sh    # Deploy RPS-7 variant experiment
│   ├── run_experiments.sh            # Run 20 baseline iterations
│   ├── run_experiments_rps.sh        # Run 20 RPS iterations
│   ├── run_experiments_rfs.sh        # Run 20 RFS iterations
│   ├── run_experiments_rps_7.sh      # Run 20 RPS-7 iterations
│   ├── enable_rps.sh                 # Enable RPS on host interfaces
│   ├── enable_rfs.sh                 # Enable RFS on host interfaces
│   ├── disable_rps.sh                # Disable RPS on host interfaces
│   └── disable_rfs.sh                # Disable RFS on host interfaces
│
├── docker/                            # Custom Docker images
│   ├── rps/                          # RPS-enabled iperf3 container
│   │   ├── Dockerfile                # Image definition
│   │   ├── enable_rps.sh            # Container-level RPS enable script
│   │   └── entrypoint.sh             # Container entrypoint
│   ├── rfs/                          # RFS-enabled iperf3 container
│   │   ├── Dockerfile
│   │   ├── enable_rfs.sh
│   │   └── entrypoint.sh
│   └── rps-7/                        # RPS-7 variant container
│       ├── Dockerfile
│       ├── enable_rps.sh
│       └── entrypoint.sh
│
├── kubernetes/                        # Kubernetes deployment configs
│   └── helm-charts/                  # Helm charts for deployments
│       ├── client/                   # iperf3 client chart
│       │   ├── Chart.yaml
│       │   ├── values.yaml
│       │   └── templates/
│       │       └── client.yaml
│       ├── server/                   # Baseline server chart
│       │   ├── Chart.yaml
│       │   ├── values.yaml
│       │   └── templates/
│       │       └── server.yaml
│       ├── server-rps/               # RPS server chart
│       │   ├── Chart.yaml
│       │   ├── values.yaml
│       │   └── templates/
│       │       └── server.yaml
│       ├── server-rfs/               # RFS server chart
│       │   ├── Chart.yaml
│       │   ├── values.yaml
│       │   └── templates/
│       │       └── server.yaml
│       └── server-rps-7/             # RPS-7 server chart
│           ├── Chart.yaml
│           ├── values.yaml
│           └── templates/
│               └── server.yaml
│
├── data/                              # Experimental data
│   └── results/                      # Raw experiment output
│       ├── baseline-*.txt           # Baseline results (1, 2, 4, 8, 16 replicas)
│       ├── rps-*.txt                 # RPS results
│       ├── rps-plus-*.txt            # RPS+ (host + container) results
│       ├── rfs-*.txt                 # RFS results
│       ├── rfs-plus-*.txt            # RFS+ (host + container) results
│       ├── rps-7-*.txt                # RPS-7 variant results
│       └── rps-plus-7-*.txt          # RPS-7+ variant results
│
├── analysis/                          # Data analysis and visualization
│   └── data_parse/                   # Analysis scripts and outputs
│       ├── generate.py               # Main analysis script
│       ├── finalized_*.csv           # Processed data (bitrate, idle, soft)
│       ├── confidence_*.csv          # Confidence interval data
│       └── *.png                     # Generated plots
│
├── docs/                              # Documentation
│   ├── STRUCTURE.md                  # This file
│   └── (research paper)              # LaTeX source or PDF
│
├── README.md                          # Main repository documentation
└── .gitignore                        # Git ignore rules
```

## Component Descriptions

### Scripts Directory

All scripts in this directory are bash scripts that automate experiment deployment and execution. They should be run from the repository root or with appropriate path adjustments.

**Deploy Scripts:**
- Deploy Kubernetes pods using Helm charts
- Collect CPU metrics using mpstat
- Extract iperf3 throughput results
- Clean up resources after completion

**Run Scripts:**
- Execute deploy scripts 20 times for statistical significance
- Aggregate results and compute statistics
- Output formatted results for analysis

**Enable/Disable Scripts:**
- Configure RPS/RFS on host network interfaces
- Must be run on the server node with appropriate permissions

### Docker Directory

Contains Dockerfiles and scripts for building custom iperf3 images with RPS/RFS support at the container level.

**Key Features:**
- Based on `networkstatic/iperf3` image
- Includes enable scripts for container-level optimizations
- Requires privileged containers to modify `/sys` filesystem

### Kubernetes Directory

Helm charts for deploying iperf3 clients and servers with different optimization configurations.

**Chart Types:**
- `client`: Standard iperf3 client pods
- `server`: Baseline server pods (no optimizations)
- `server-rps`: Server pods with RPS-enabled container image
- `server-rfs`: Server pods with RFS-enabled container image
- `server-rps-7`: Server pods with RPS-7 variant container image

### Data Directory

Stores raw experimental results in text format. Each file contains output from 20 experiment runs for a specific configuration and replica count.

### Analysis Directory

Contains Python scripts for processing experimental data and generating publication-quality plots.

**Key Files:**
- `generate.py`: Main analysis script that:
  - Reads CSV data files
  - Generates bar charts with error bars
  - Creates multi-panel figures for paper

## Experiment Workflow

1. **Setup**: Enable RPS/RFS on host interfaces (if needed)
2. **Deploy**: Use deploy scripts to run single experiments
3. **Run**: Use run scripts for statistical significance (20 iterations)
4. **Collect**: Results saved to `data/results/`
5. **Analyze**: Process results with `analysis/data_parse/generate.py`
6. **Visualize**: Generated plots in `analysis/data_parse/`

## Path References

When running scripts, ensure you're in the correct directory:

- **From repository root**: Scripts reference paths relative to their location
- **Deploy scripts**: Reference `../kubernetes/helm-charts/` for Helm charts
- **Analysis scripts**: Should be run from `analysis/data_parse/` directory

## Notes

- All scripts assume a Kubernetes cluster is configured and accessible
- SSH access to worker nodes is required for CPU metrics collection
- Container images must be built and pushed to accessible registry
- Interface names in enable/disable scripts may need adjustment for your environment


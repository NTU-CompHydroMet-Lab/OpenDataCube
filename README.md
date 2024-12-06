# Setup Open Data Cube (ODC) with Docker 🛰

This repository contains step-by-step instructions and resources to set up Open Data Cube (ODC) using Docker. Open Data Cube enables efficient handling and analysis of large geospatial datasets. For detail tutorial, please refer to [our ODC notion](https://chingchunchou.notion.site/Setup-ODC-with-Docker-ba965c73e071492a80d2f5a302a1d374) or [Tutorial.pdf](https://github.com/NTU-CompHydroMet-Lab/OpenDataCube/blob/main/Tutorial.pdf) in the repo.

## Table of Contents
- [What is Docker?](#what-is-docker)
- [Setup Instructions](#setup-instructions)
  - [Step 1: Install Docker](#step-1-install-docker)
  - [Step 2: Network Configuration](#step-2-network-configuration)
  - [Step 3: Pull Required Docker Images](#step-3-pull-required-docker-images)
  - [Step 4: Build Containers](#step-4-build-containers)
  - [Step 5: Start Unix Shell in ODC Container](#step-5-start-unix-shell-in-odc-container)
  - [Step 6: Initialize Datacube](#step-6-initialize-datacube)
- [Saving Datasets](#saving-datasets)
  - [Single Timestamp](#single-timestamp)
  - [Multiple Timestamps](#multiple-timestamps)
  - [Time Series Data](#time-series-data)
- [Modules](#modules)
- [Displaying Data](#displaying-data)

---

## What is Docker?

Docker is a platform for building, running, and sharing containerized applications. Containers allow you to package software and its dependencies together for seamless deployment.

For a detailed introduction to Docker, refer to:
- [Docker Basics](https://medium.com/alberthg-docker-notes/docker%E7%AD%86%E8%A8%98-docker%E5%9F%BA%E7%A4%8E%E6%95%99%E5%AD%B8-7bbe3a351caf)
- [Managing PostgreSQL Containers](https://medium.com/alberthg-docker-notes/docker%E7%AD%86%E8%A8%98-%E9%80%B2%E5%85%A5container-%E5%BB%BA%E7%AB%8B%E4%B8%A6%E6%93%8D%E4%BD%9C-postgresql-container-d221ba39aaec)

---

## Setup Instructions

### Step 1: Install Docker
Install Docker Engine for your operating system:
- [Install Docker](https://docs.docker.com/engine/install/)

**Note:** If you encounter WSL issues, follow the troubleshooting steps provided in the installation guide.

### Step 2: Network Configuration
Ensure PostgreSQL and Datacube containers are on the same network:
```bash
docker network inspect bridge
docker network create <network-name>
```

### Step 3: Pull Required Docker Images
Pull the necessary images from Docker Hub:
- [PostgreSQL](https://hub.docker.com/_/postgres)
- [ODC Cube-in-a-Box](https://hub.docker.com/r/opendatacube/cube-in-a-box)
```bash
docker pull postgres
docker pull opendatacube/cube-in-a-box
```

### Step 4: Build Containers
- PostgreSQL:
```bash
docker run -d --name <postgres-container-name> -p 8080:5432 -e POSTGRES_PASSWORD=<password> postgres
```
- Datacube:
```bash
docker run -d --name <datacube-container-name> -p 443:8888 -e DB_HOSTNAME=postgres -e DB_USERNAME=postgres -e DB_PASSWORD=<password> opendatacube/cube-in-a-box
```

### Step 5: Start Unix Shell in ODC Container
Run the following to access the shell:
```bash
docker exec -it <datacube-container-name> bash
```

### Step 6: Initialize Datacube
Initialize the database:
```bash
datacube -v system init
```
If errors occur, create and edit `datacube.conf` with appropriate settings.

---

## Saving Datasets

### Single Timestamp
Prepare the following:
1. **Python script**: Export metadata (`.py`).
2. **Metadata file**: Dataset description (`.yaml`).
3. **Product definition**: To load datasets (`.yaml`).

### Multiple Timestamps
Follow the single timestamp process but ensure consistency in the product and variable names across timestamps.

### Time Series Data
Use provided modules to handle NetCDF files:
1. `Split_nc.py`: Split time series data into slices.
2. `Metadata_auto_generater.py`: Generate metadata.
3. `Metadata_import.bash`: Automate metadata import.

---

## Modules
This repository includes:
- `Split_nc.py`: Split NetCDF files.
- `Metadata_auto_generater.py`: Auto-generate metadata.
- `Metadata_import.bash`: Automate metadata import.

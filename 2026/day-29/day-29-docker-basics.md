# Day 29 – Introduction to Docker

# Task 1: What is Docker?

---

## What is Docker?

Docker is an open-source platform that lets you package applications and everything they need (code, libraries, config, runtime) into a single portable unit called a **container**, which can run consistently on any machine.

---

## What is a Container, and Why Do We Need Them?

Imagine you write a Python app that works perfectly on your laptop. You push it to a server, and it crashes — because the server has a different Python version, missing libraries, or different environment variables. This "works on my machine" problem is exactly what containers solve.

A container bundles your app together with its entire runtime environment — OS libraries, dependencies, config files — into one isolated, self-contained unit. It runs the same way everywhere: your laptop, a CI server, or production in the cloud. No more dependency conflicts, no more environment drift.

---

## Containers vs Virtual Machines

Both containers and VMs provide isolation, but the difference is in *how deep* that isolation goes.

A **Virtual Machine (VM)** runs a full operating system on top of a hypervisor. Each VM includes its own kernel, OS binaries, and apps — making it heavy (GBs in size) and slow to start (minutes).

A **container** shares the host OS kernel and isolates only the user space (libraries, processes, filesystem). This makes containers extremely lightweight (MBs), and they start in milliseconds.

| Feature | Containers | Virtual Machines |
|---|---|---|
| Size | Megabytes | Gigabytes |
| Startup time | Milliseconds | Minutes |
| OS | Shares host kernel | Full guest OS per VM |
| Isolation | Process-level | Full hardware-level |
| Portability | Very high | Moderate |
| Use case | Microservices, CI/CD | Full OS environments |

> **The trade-off:** VMs offer stronger security isolation (separate kernels), while containers offer speed and efficiency. In practice, containers are often run *inside* VMs in cloud environments, giving you both.

---

## Docker Architecture

Docker follows a **client–server architecture**. Here are the key components:

### 1. Docker Client
The CLI tool you type commands into (`docker run`, `docker build`, `docker pull`, etc.). It communicates with the Docker daemon via a REST API.

### 2. Docker Daemon (`dockerd`)
The background service that does the heavy lifting: building images, running containers, managing volumes and networks. It listens for commands from the client.

### 3. Docker Images
Read-only blueprints for containers. Built in layers using a `Dockerfile`. Think of an image as a **class** in OOP — it defines what the container will look like, but isn't running yet.

### 4. Docker Containers
A running instance of an image. You can run many containers from the same image. Each is isolated but shares the host kernel.

### 5. Docker Registry
A storage and distribution system for images. **Docker Hub** is the public default. You push images to and pull images from a registry.

---

## Docker Architecture Diagram (Text)

```
┌─────────────────┐        REST API        ┌──────────────────────────────────────────┐
│  Docker Client  │ ─────────────────────► │             Docker Host                  │
│                 │                         │                                          │
│  docker build   │                         │  ┌──────────────────┐                   │
│  docker pull    │                         │  │   Docker Daemon  │  (dockerd)         │
│  docker run     │                         │  └────────┬─────────┘                   │
└─────────────────┘                         │           │ manages                      │
                                            │  ┌────────▼─────────┐                   │
┌─────────────────┐                         │  │     Images        │                   │
│    Registry     │ ◄──── pull / push ─────►│  │  nginx, myapp…   │                   │
│                 │                         │  └────────┬─────────┘                   │
│  Docker Hub     │                         │           │ run                          │
│  Private repos  │                         │  ┌────────▼─────────┐                   │
└─────────────────┘                         │  │   Containers      │                   │
                                            │  │  C1  C2  C3 …    │                   │
                                            │  └──────────────────┘                   │
                                            │                                          │
                                            │  Host OS Kernel (shared by all)          │
                                            └──────────────────────────────────────────┘
```

---

## The Flow in Plain English

1. You type `docker run nginx` in your terminal **(Docker client)**.
2. The client sends the request to the **Docker daemon** (`dockerd`) running in the background.
3. The daemon checks if the `nginx` **image** is available locally. If not, it pulls it from the **Docker Hub** registry.
4. The daemon uses that image as a blueprint to spin up a new isolated **container** running nginx.
5. The container shares the host's OS kernel but has its own filesystem, processes, and network — completely isolated from other containers.

> That's the full Docker loop. One image → many containers. Registries make images portable across teams. The daemon handles all the heavy lifting behind a clean CLI.

---

## Key Terms Summary

| Term | Meaning |
|---|---|
| **Container** | Isolated, lightweight runtime environment for an app |
| **Image** | Read-only blueprint used to create containers |
| **Dockerfile** | Script of instructions to build a Docker image |
| **Docker Hub** | Public registry to store and share images |
| **Daemon** | Background service that manages Docker objects |
| **Registry** | Storage system for Docker images (public or private) |
| **Volume** | Persistent storage attached to a container |

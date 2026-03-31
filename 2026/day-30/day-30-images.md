# Day 30 – Docker Images & Container Lifecycle


## Challenge Tasks

### Task 1: Docker Images
**1. Pull the `nginx`, `ubuntu`, and `alpine` images from Docker Hub**
<img width="10" height="2" alt="image" src="https://github.com/user-attachments/assets/16790189-5d57-4c7e-9f58-b721e3463707" />

**2. List all images on your machine — note the sizes**
<img width="746" height="283" alt="image" src="https://github.com/user-attachments/assets/417b9895-4f4c-4f85-8264-32e493d81877" />

**3. Compare `ubuntu` vs `alpine` — why is one much smaller?**
Alpine Linux Docker images are dramatically smaller than Ubuntu images, with the Alpine base image being around 5 MB compared to Ubuntu's 75-80 MB.
This size difference is due to Alpine being built around the minimalist musl libc
and BusyBox instead of the more comprehensive glibc and GNU core utilities used by Ubuntu

**5. Inspect an image — what information can you see?**
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/c1513471-35f0-4a5e-92c4-152712df22a0" />
---
## Docker Image Inspect — Deep Dive

---

## `docker images` — Reading the Output

```
alpine:latest           a40c03cbb81c       8.44MB
flask-app-mini:latest   3108550f84eb       69.8MB      U
flask-app:latest        1d8bb1e026b5       1.13GB
hello-world:latest      e2ac70e7319a       10.1kB      U
mysql:latest            a3ecd26c7346        922MB      U
nginx:latest            0cf1d6af5ca7        161MB
ubuntu:latest           f794f40ddfff       78.1MB
```

The `U` flag means **unused** — no container (running or stopped) is currently using that image. As a DevOps engineer this matters for cleanup:

```bash
docker image prune   # removes all unused images automatically
```

### Image Size Comparison

| Image | Size | Why |
|---|---|---|
| `hello-world` | 10.1 kB | Just a binary, nothing else |
| `alpine` | 8.44 MB | Minimal Linux, no extras |
| `ubuntu` | 78.1 MB | Full Ubuntu userspace |
| `nginx` | 161 MB | nginx + Debian base |
| `flask-app-mini` | 69.8 MB | App on a slim base |
| `mysql` | 922 MB | Full database engine |
| `flask-app` | 1.13 GB | App on a heavy base |

> In production, smaller images = faster deployments, less attack surface, lower storage costs.
> A good DevOps engineer always asks: *do I really need Ubuntu, or can I use Alpine?*

---

## `docker image inspect` — Field by Field

### 1. Identity

```json
"Id": "sha256:a40c03cbb81c59bf...",
"RepoTags": ["alpine:latest"],
"RepoDigests": ["alpine@sha256:25109184c71b..."]
```

**Two different hashes — know the difference:**

| Field | What it is | Use case |
|---|---|---|
| `Id` | Hash of the **local** image content | Identifies image on your machine |
| `RepoDigest` | Hash from **Docker Hub** (immutable) | Pin exact versions in production |

In production you never use `alpine:latest` — you pin by digest:

```bash
docker pull alpine@sha256:25109184c71bdad752c8312a8623239686a9a2071e8825f20acb8f2198c3f659
```

Because `latest` can change tomorrow and break your app. The digest never changes.

---

### 2. Created — When It Was Built

```json
"Created": "2026-01-28T01:18:04.977843834Z"
```

This is when the image was **built**, not when you pulled it. Useful for auditing — in security-conscious teams you check image age. An image built 2 years ago likely has unpatched vulnerabilities.

---

### 3. Architecture

```json
"Architecture": "amd64",
"Os": "linux"
```

Your ThinkPad is `amd64` (Intel/AMD 64-bit). This image was built for that architecture.

This matters in DevOps when:
- Running on cloud servers using ARM (AWS Graviton = `arm64`)
- Supporting Apple M1/M2 Macs (`arm64`)
- Building multi-platform images → use `docker buildx` for that

If you try running an `amd64` image on an `arm64` machine, it will fail or run slowly under emulation.

---

### 4. Config — Default Container Behaviour

```json
"Cmd": ["/bin/sh"],
"WorkingDir": "/",
"Env": ["PATH=/usr/local/sbin:/usr/local/bin..."]
```

This is what runs when you do `docker run alpine` with no extra arguments — it runs `/bin/sh`.

You can override the default command:

```bash
docker run alpine echo "hello"    # runs echo instead of sh
docker run alpine ls /etc         # runs ls instead of sh
```

The `PATH` env var is baked into the image so the container knows where to find binaries.

---

### 5. GraphDriver — How the Image is Stored on Disk

```json
"GraphDriver": {
    "Name": "overlay2",
    "Data": {
        "MergedDir": "/var/lib/docker/overlay2/.../merged",
        "UpperDir":  "/var/lib/docker/overlay2/.../diff",
        "WorkDir":   "/var/lib/docker/overlay2/.../work"
    }
}
```

This is **OverlayFS** — the Linux filesystem magic that makes Docker efficient.

```
Base image layer  (read-only)
        +
Container changes (read-write → UpperDir)
        =
What the container sees (MergedDir)
```

- When you run a container and create a file, it goes into `UpperDir`
- The original image is **never touched**
- Delete the container → those changes vanish
- This is why containers are **ephemeral** by default
- This is why you need **volumes** for anything you want to persist

---

### 6. RootFS Layers — The Most Important Concept

```json
"RootFS": {
    "Type": "layers",
    "Layers": [
        "sha256:989e799e634906e94dc9a5ee2ee26fc92ad260522990f26e707861a5f52bf64e"
    ]
}
```

Alpine has **1 layer** — it's as minimal as it gets.

Each instruction in a `Dockerfile` that modifies the filesystem creates a new layer:

```dockerfile
FROM ubuntu               # layer 1 — base OS
RUN apt-get update        # layer 2 — package index
RUN apt-get install nginx # layer 3 — nginx binary
COPY ./site /var/www      # layer 4 — your files
```

**Why layers matter in DevOps:**

| Benefit | Explanation |
|---|---|
| **Caching** | If a layer didn't change, Docker reuses it — builds are fast |
| **Sharing** | Two images sharing the same base layer store it only once on disk |
| **Size** | Fewer layers = smaller image = faster pulls and deployments |

Check the layer count on your images:

```bash
docker image inspect nginx  | grep -A 20 "RootFS"
docker image inspect ubuntu | grep -A 20 "RootFS"
docker image inspect alpine | grep -A 20 "RootFS"
```

---

### DevOps Engineer Takeaways

| What to look at | Why it matters |
|---|---|
| **Image size** | Always minimise — Alpine over Ubuntu where possible |
| **RepoDigest** | Always pin in production, never use `:latest` |
| **Architecture** | Know your target platform — `amd64` vs `arm64` |
| **Layers** | Understand caching, write Dockerfiles layer-efficiently |
| **GraphDriver** | Containers are ephemeral — use volumes for persistence |
| **Created date** | Old images = security risk — keep them updated |

---

` after each step — observe the state changes.

---

## Task 4: Working with Running Containers

1. Run an Nginx container in detached mode
2. View its **logs**
3. View **real-time logs** (follow mode)
4. **Exec** into the container and look around the filesystem
5. Run a single command inside the container without entering it
6. **Inspect** the container — find its IP address, port mappings, and mounts

---

### Task 5: Cleanup
1. Stop all running containers in one command
2. Remove all stopped containers in one command
3. Remove unused images
4. Check how much disk space Docker is using

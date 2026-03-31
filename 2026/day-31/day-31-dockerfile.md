# Day 31 – Dockerfile: Build Your Own Images


## Challenge Tasks

### Task 1: Your First Dockerfile


1. Create a folder called `my-first-image`
<img width="1912" height="334" alt="image" src="https://github.com/user-attachments/assets/93bee70c-70e4-41ec-b8d1-18ec5c8065ed" />

2. Inside it, create a `Dockerfile` that:
   - Uses `ubuntu` as the base image
   - Installs `curl`
   - Sets a default command to print `"Hello from my custom image!"`
   - 
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/c4d0e991-a122-4f18-b4f2-78a4ae818cdf" />

3. Build the image and tag it `my-ubuntu:v1`
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/ddfac26f-01bd-416f-a627-148f965a3d0d" />

4. Run a container from your image
<img width="1912" height="334" alt="image" src="https://github.com/user-attachments/assets/7619ec82-29c0-4c29-955c-7b47e783c485" />


**Verify:** The message prints on `docker run`

---

### Task 2: Dockerfile Instructions
Create a new Dockerfile that uses **all** of these instructions:
- `FROM` — base image
- `RUN` — execute commands during build
- `COPY` — copy files from host to image
- `WORKDIR` — set working directory
- `EXPOSE` — document the port
- `CMD` — default command

Build and run it. Understand what each line does.

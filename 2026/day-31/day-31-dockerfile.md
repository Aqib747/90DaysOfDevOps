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
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/81fe57c1-816b-48ed-acaf-c9317b87e3d0" />
Dockerfile :
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/236653b3-4152-4633-b964-fd504418c9a4" />
Running contaner
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/f009f977-48c0-46bc-9438-9f4f81b1cf9f" />

---

## Task 3: CMD vs ENTRYPOINT
Create an image with CMD ["echo", "hello"] — run it, then run it with a custom command. What happens?
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/c85f49ba-c48e-4205-909c-a6e847dabd82" />


Create an image with ENTRYPOINT ["echo"] — run it, then run it with additional arguments. What happens?
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/354a8dfc-dad0-4e7d-969b-56dc3623a424" />

Write in your notes: When would you use CMD vs ENTRYPOINT?


Use CMD when

Your container can do multiple things
You want users to easily swap the command
Example: a utility image where someone might run bash, python, or sh

Use ENTRYPOINT when

Your container has one specific job
You want the command to always run no matter what
Example: nginx, python app.py, java -jar app.jar

Use both together when

You have a fixed executable (ENTRYPOINT) but want a sensible default argument (CMD)
Example: a backup tool where ENTRYPOINT is the tool and CMD is --help by default

dockerfileENTRYPOINT ["python", "app.py"]   # always runs python app.py
CMD ["--port", "8080"]            # default port, easily overridden

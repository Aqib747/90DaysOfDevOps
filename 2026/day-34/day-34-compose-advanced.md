## Challenge Tasks

### Task 1: Build Your Own App Stack
Create a `docker-compose.yml` for a 3-service stack:
- A **web app** (use Python Flask, Node.js, or any language you know)
- A **database** (Postgres or MySQL)
- A **cache** (Redis)

Write a simple Dockerfile for the web app. The app doesn't need to be complex — even a "Hello World" that connects to the database is enough.

## Import things to consider while writing docker compose 

Flask app → 1 service
Postgres → 1 service
Redis → 1 service

That gives you your services: block.

Step 2: For each service, ask 4 questions:
1. Do I have a Dockerfile or use a ready image?

My own code → build: .
Standard software → image: postgres:15

2. Does it need ports exposed to my browser?

Only the web app needs it → ports: "5000:5000"
DB and Redis are internal, no ports needed

3. Does it need environment variables?

Postgres needs DB name, user, password
Flask needs to know how to reach Postgres

4. Does it need to persist data?

Postgres yes → volumes
Redis and Flask no


Step 3: Figure out dependencies
Ask — which service depends on another to be running first?

Flask needs DB and Redis → depends_on


Step 4: Check the official Docker Hub page
Every image like postgres, redis, nginx has a Docker Hub page that tells you:

What environment variables it accepts
What port it runs on
What volume path to mount

---
docker-compose.yml
<img width="1888" height="1030" alt="image" src="https://github.com/user-attachments/assets/05744286-a765-470d-9bf4-be802432777a" />
Dockerfile

<img width="1888" height="1030" alt="image" src="https://github.com/user-attachments/assets/686e6d75-7a98-4537-a8da-114a1cac14d9" />

<img width="1888" height="1030" alt="image" src="https://github.com/user-attachments/assets/324e50cf-75ed-410f-b90e-89a6600950bf" />

---
## Task 2: depends_on & Healthchecks
1. Add `depends_on` to your compose file so the app starts **after** the database

  <img width="1888" height="1030" alt="image" src="https://github.com/user-attachments/assets/9465a15f-3500-42c1-8acb-4299f1147101" />

2. Add a **healthcheck** on the database service
3. Use `depends_on` with `condition: service_healthy` so the app waits for the database to be truly ready, not just started

**Test:** Bring everything down and up — does the app wait for the DB?

Does wait for th heealth check to be sucessfull
<img width="1888" height="658" alt="image" src="https://github.com/user-attachments/assets/4dc57584-bd71-4bd2-8b63-8182a835b96c" />

---
## Task 3: Restart Policies
1. Add `restart: always` to your database service
2. Manually kill the database container — does it come back?
3. Try `restart: on-failure` — how is it different?
4. Write in your notes: When would you use each restart policy?



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
<img width="1595" height="1015" alt="image" src="https://github.com/user-attachments/assets/0ee2338d-a784-42d1-a49d-62d062bf34dd" />

3. Try `restart: on-failure` — how is it different?
4. Write in your notes: When would you use each restart policy?

## Restart Policies

### When to use each:

| Policy | Use When |
|--------|----------|
| `no` | Development/testing — you want containers to stay dead so you can debug |
| `always` | Critical services like databases, caches — must always be running |
| `on-failure` | Worker jobs — restart if they crash but not if you stop them manually |
| `unless-stopped` | Production web apps — restart automatically but respect manual stops |

### Difference between `always` and `unless-stopped`:

| Situation | `always` | `unless-stopped` |
|-----------|----------|-----------------|
| Container crashes | ✅ Restarts | ✅ Restarts |
| Machine reboots | ✅ Restarts | ❌ Stays stopped |
| `docker compose down` | ❌ Respects stop | ❌ Respects stop |
| `kill -9` inside container | ✅ Restarts | ✅ Restarts |

### Recommendation:
- Database → `always` (must never be down)
- Web app → `unless-stopped` (respect manual deploys)
- Worker/job → `on-failure` (only restart on crashes)

---

### Task 4: Custom Dockerfiles in Compose
1. Instead of using a pre-built image for your app, use `build:` in your compose file to build from a Dockerfile
<img width="684" height="214" alt="image" src="https://github.com/user-attachments/assets/5031c9ac-7013-4d38-ab76-08fb3ff251d7" />

2. Make a code change in your app
<img width="1006" height="370" alt="image" src="https://github.com/user-attachments/assets/a25af3a2-5ee0-49a1-b550-7fca41bdb3b0" />

3. Rebuild and restart with one command
<img width="1017" height="174" alt="image" src="https://github.com/user-attachments/assets/6e635af9-7209-44ac-b908-91aaa5fa37ce" />


---

### Task 5: Named Networks & Volumes
1. Define **explicit networks** in your compose file instead of relying on the default
<img width="673" height="124" alt="image" src="https://github.com/user-attachments/assets/461ce687-45b2-4894-9431-dcc198221444" />

2. Define **named volumes** for database data
<img width="673" height="124" alt="image" src="https://github.com/user-attachments/assets/e88c487b-2eac-4874-b19b-d2af5b6cca60" />

3. Add **labels** to your services for better organization
<img width="1109" height="107" alt="image" src="https://github.com/user-attachments/assets/0b2d659a-7496-4d50-81b5-d36157e96ca8" />


## Task 5: Named Networks & Volumes

### 1. Named Networks

By default Compose puts ALL services on one shared network — every service can talk to every other service. This is a security risk in production.

**Solution — separate networks:**

```
frontend network → web faces the outside world
backend network  → db and cache are hidden inside
```

```yaml
networks:
  frontend:   # web faces the outside world
  backend:    # db and cache are hidden inside
```

- `web` is on BOTH networks — talks to browser AND database
- `postgress` and `redis` are ONLY on backend — isolated from outside

**Think of it like a restaurant:**
- Frontend = dining area (customers can access)
- Backend = kitchen (only staff can access)

---

### 2. Named Volumes

```yaml
volumes:
  pgdata:
```

| | Anonymous Volume | Named Volume |
|--|-----------------|--------------|
| Name | Random ID | `pgdata` — human readable |
| Reuse | Hard to find | Easy to reference |
| Backup | Hard to identify | Easy to target |
| Sharing | Can't share | Can share between services |

```bash
docker volume ls           # see pgdata clearly
docker volume inspect pgdata  # inspect it
```

---

### 3. Labels

Labels are metadata tags attached to containers — like sticky notes. They don't affect how containers run.

```yaml
labels:
  app: flask-stack
  tier: web
```

**Why useful in production:**

```bash
# filter containers by label
docker ps --filter "label=tier=database"

# find all containers belonging to your app
docker ps --filter "label=app=flask-stack"
```

In large systems with 50+ containers, labels help you:
- Filter and find specific containers quickly
- Monitoring tools like Prometheus use labels to group metrics
- Log aggregators use labels to route logs to the right place

---

### The Big Picture
BROWSER
↓
[frontend network]
↓
[web] ← labeled: tier=web
↓
[backend network]
↓
[postgress] ← labeled: tier=database    [redis] ← labeled: tier=cache
↓
[pgdata volume] ← named, persistent



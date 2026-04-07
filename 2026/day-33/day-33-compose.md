## Task 1: Install & Verify
Check if Docker Compose is available on your machine
Verify the version
<img width="1568" height="391" alt="image" src="https://github.com/user-attachments/assets/d107aa78-9776-409d-847f-73cefeaa0cfa" />

## Task 2: Your First Compose File
1. Create a folder `compose-basics`
2. Write a `docker-compose.yml` that runs a single **Nginx** container with port mapping
<img width="1568" height="391" alt="image" src="https://github.com/user-attachments/assets/3dd825c9-eace-46ec-bb23-b19866baaffe" />

3. Start it with `docker compose up`
<img width="1797" height="1055" alt="image" src="https://github.com/user-attachments/assets/94fed3bf-9646-4b3e-9616-8906f5166bf4" />

4. Access it in your browser
<img width="1797" height="1055" alt="image" src="https://github.com/user-attachments/assets/4eb3ae53-9f90-47e9-bd93-6231d06061cd" />


5. Stop it with `docker compose down`
<img width="922" height="301" alt="image" src="https://github.com/user-attachments/assets/6a5bd587-ddf8-4075-83f4-7ad936599e08" />


## Task 3: Two-Container Setup
Write a `docker-compose.yml` that runs:
- A **WordPress** container
- A **MySQL** container


They should:
- Be on the same network (Compose does this automatically)
- MySQL should have a named volume for data persistence
- WordPress should connect to MySQL using the service name
<img width="1911" height="956" alt="image" src="https://github.com/user-attachments/assets/a0c6c327-863d-4ab3-bf06-6bdde7a34094" />


Start it, access WordPress in your browser, and set it up.
<img width="1859" height="1022" alt="image" src="https://github.com/user-attachments/assets/b93b90c9-0cb2-4a41-8b21-e21fb73954a6" />


**Verify:** Stop and restart with `docker compose down` and `docker compose up` — is your WordPress data still there?
<img width="1559" height="229" alt="image" src="https://github.com/user-attachments/assets/7de79c38-5e44-4863-b832-2fe7d495abf7" />
test user still persist
<img width="1888" height="1030" alt="image" src="https://github.com/user-attachments/assets/3d6bed57-f139-48fa-8710-f137731712d6" />



---

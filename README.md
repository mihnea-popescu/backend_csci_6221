# 🎮 Pokémon Guesser Backend  
### **CSCI 6221 – Backend Service (FastAPI + Docker)**

This repository contains the backend API for the **Pokémon Guesser Game** built for **CSCI_6221**.  
The backend provides:

- A Pokémon-themed **random name generator**
- An endpoint to **save player scores**
- A **leaderboard** that returns the top 10 players
- A lightweight **FastAPI** server with **SQLite**
- Fully containerized with **Docker** for easy deployment

---

# 📘 Features

### **1. Save Score**
Players submit their game score, and the backend:

- Generates a random Pokémon-themed username  
  (e.g., `PowerfulPikachu37`)
- Saves the score into a local SQLite database
- Returns the generated username

### **2. Get Leaderboard**
Returns the top 10 users sorted by descending score.

### **3. Deploy Anywhere**
With Docker, the backend runs consistently on:

- Local machine  
- Cloud VM (AWS, Azure, GCP, Hetzner, etc.)
- Render / Railway / Fly.io

---

# 🧩 API Endpoints

## **POST /save**

Save a user's score.

### **Request**
```json
{
  "score": 150
}
```

### **cURL Command**
```bash
curl -X POST http://localhost:8000/save      -H "Content-Type: application/json"      -d '{"score":150}'
```

### **Response**
```json
{
  "success": true,
  "name": "PowerfulPikachu37"
}
```

---

## **GET /leaderboard**

Retrieve the top 10 players.

### **cURL Command**
```bash
curl http://localhost:8000/leaderboard
```

### **Response**
```json
[
  { "name": "StrongEevee22", "score": 200 },
  { "name": "WildGengar81", "score": 150 }
]
```

---

# 🛠️ Local Development

### **1. Install dependencies**
```
pip install -r requirements.txt
```

### **2. Run the FastAPI server**
```
uvicorn main:app --reload --port 9000
```

The API will be available at:

- 👉 http://localhost:8000  
- 👉 http://localhost:8000/docs (Swagger UI)

---

# 🐳 Running with Docker (Recommended)

### **1. Build the Docker image**
```bash
docker build -t pokemon-backend .
```

### **2. Run the container**
```bash
docker run -d -p 8000:8000 --name pokemon-api pokemon-backend
```

Backend will be live at:

👉 http://localhost:8000

---

# 💾 Database

The backend uses **SQLite** for simplicity.  
A file named **scores.db** is created automatically.

If you want to persist scores across container restarts:

```bash
docker run -d -p 8000:8000   -v $(pwd)/scores.db:/app/scores.db   --name pokemon-api pokemon-backend
```

---

# 🧱 Project Structure

```
/app
   ├── main.py             # FastAPI application
   ├── requirements.txt    # Python dependencies
   └── scores.db           # SQLite database (auto-created)

Dockerfile
README.md
```

---

# 🧑‍🎓 Course Information

This backend is part of the **CSCI 6221** course project:  
**Pokémon Guesser Game – Full Stack Application**

The backend provides:

- Score tracking  
- Leaderboard ranking  
- Pokémon-themed player identities  

It is designed to integrate seamlessly with a frontend built in any framework (React, Next.js, Unity WebGL, etc.)

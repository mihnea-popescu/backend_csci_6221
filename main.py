
from fastapi import FastAPI
from pydantic import BaseModel
import random
import sqlite3
import string
import os

app = FastAPI()

# Ensure database exists
DB_PATH = "scores.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
    CREATE TABLE IF NOT EXISTS leaderboard (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        score INTEGER NOT NULL
    );
    """)
    conn.commit()
    conn.close()

init_db()

POKEMON_NAMES = [
    "Pikachu", "Charizard", "Bulbasaur", "Eevee",
    "Gengar", "Snorlax", "Mewtwo", "Lucario", "Greninja"
]


def generate_random_name():
    return f"{random.choice(['Strong', 'Mighty', 'Brave', 'Wild', 'Powerful']) }{random.choice(POKEMON_NAMES)}{random.randint(10,99)}".replace(" ", "")


# --- Request Model ---
class ScoreRequest(BaseModel):
    score: int


@app.post("/save")
def save_score(data: ScoreRequest):
    name = generate_random_name()

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("INSERT INTO leaderboard (name, score) VALUES (?, ?)", (name, data.score))
    conn.commit()
    conn.close()

    return {"success": True, "name": name}

@app.get("/leaderboard")
def get_leaderboard():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT name, score FROM leaderboard ORDER BY score DESC LIMIT 10")
    rows = c.fetchall()
    conn.close()

    return [{"name": r[0], "score": r[1]} for r in rows]


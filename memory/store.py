import json
import os

MEMORY_PATH = "memory/user_profile.json"

def load_memory():
    if not os.path.exists(MEMORY_PATH):
        return {}
    with open(MEMORY_PATH, "r") as f:
        return json.load(f)

def save_memory(memory: dict):
    with open(MEMORY_PATH, "w") as f:
        json.dump(memory, f, indent=2)

def update_memory(memory: dict, updates: dict):
    for k, v in updates.items():
        if v:
            memory[k] = v
    save_memory(memory)
    return memory
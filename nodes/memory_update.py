from memory.store import load_memory, update_memory

def memory_update(state):
    """
    Updates memory only if new preferences are provided.
    """
    memory = load_memory()

    updates = state.get("memory_updates", {})
    updated_memory = update_memory(memory, updates)

    return {"user_memory": updated_memory}
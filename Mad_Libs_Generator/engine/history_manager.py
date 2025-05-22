import json
import os 
from datetime import datetime
import uuid

HISTORY_FILE = 'data/history.json'


def save_story_to_history(story_data, path=HISTORY_FILE):
    """
    Save story data with metadata to history file.
    """
    entry = {
        "id": str(uuid.uuid4()),
        "timestamp": datetime.now().isoformat(),
        "template_title": story_data.get("title"),
        "category": story_data.get("category"),
        "user_inputs": story_data.get("inputs"),
        "final_story": story_data.get("story")
    }

    # Create file if it doesn't exist
    if not os.path.exists(path):
        with open(path, 'w') as f:
            json.dump([entry], f, indent=4)
    else:
        with open(path, 'r+') as f:
            try:
                history = json.load(f)
            except json.JSONDecodeError:
                history = []
            history.append(entry)
            f.seek(0)
            json.dump(history, f, indent=4)
            

def load_history(path=HISTORY_FILE):
    """
    Load the entire history file.
    """
    if not os.path.exists(path):
        return []
    with open(path, 'r') as f:
        return json.load(f)

def search_history_by_keyword(keyword, path=HISTORY_FILE):
    """
    Search history by keyword in the final story.
    """
    results = []
    history = load_history(path)
    for entry in history:
        if keyword.lower() in entry["final_story"].lower():
            results.append(entry)
    return results

def get_stories_by_category(category, path=HISTORY_FILE):
    """
    Return stories from a specific category.
    """
    return [entry for entry in load_history(path) if entry["category"] == category]

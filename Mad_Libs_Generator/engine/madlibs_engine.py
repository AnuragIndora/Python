import json 
import os
import re
import random 

def load_template(file_path):
    """Load story templates from the json"""
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            if isinstance(data, dict):  # Single story
                return [data]
            return data
    except FileNotFoundError:
        print("Error: stories.json file not found!")
        return []
    except json.JSONDecodeError:
        print("Error: JSON file is improperly formatted!")
        return []

    

def list_categories(templates):
    "List all unique categories from the story template"
    categories = list(set(template['category'] for template in templates))
    print("\nAvailable Categories: ")
    for i, category in enumerate(categories, 1):
        print(f"{i}. {category}")
    return categories


def select_template(templates, category=None):
    """Select a template randomly from a category, or from all if no category."""
    if category:
        filtered = [t for t in templates if t['category'].lower() == category.lower()]
        if not filtered:
            print(f"No templates found for category '{category}'. Choosing random.")
            return random.choice(templates)
        return random.choice(filtered)
    return random.choice(templates)


def extract_placeholders(story):
    """Extract all unique placeholders from the story template."""
    return list(set(re.findall(r"{(.*?)}", story)))


def fill_placeholders(placeholders):
    """Prompt the user to fill in each placeholder."""
    user_inputs = {}
    print(f"\nPlease provide the following words:\n")
    for word in placeholders:
        response = input(f"Enter a {word.replace('_', ' ')}: ").strip()
        while not response:
            response = input(f"(Required) Enter a {word.replace('_', ' ')}: ").strip()
        user_inputs[word] = response

    return user_inputs


def generate_story(template, user_inputs):
    """Fill placeholders with user input and return the completed story."""
    story = template
    for key, value in user_inputs.items():
        story = story.replace(f"{{{key}}}", value)
    return story
import json
import re
from datetime import datetime
import uuid
import os

CUSTOM_STORIES = "data/custom_story.json"

# Validate placeholders like {noun}, {verb}, etc.
def validate_placeholder(text):
    return re.findall(r"{(.*?)}", text)


# Save story template to JSON file
def save_template_to_file(data, filename=CUSTOM_STORIES):
    try:
        if os.path.exists(filename) and os.path.getsize(filename) > 0:
            with open(filename, 'r') as file:
                existing = json.load(file)
        else:
            existing = []
    except (FileNotFoundError, json.JSONDecodeError):
        existing = []

    existing.append(data)
    with open(filename, 'w') as file:
        json.dump(existing, file, indent=4)


def generate_custom_id(title, existing_count):
    base = title.lower().replace(" ", "_")
    return f"{base}_{str(existing_count + 1).zfill(3)}"



# Create a new story template
def create_new_template():
    print("Create a New Story Template: ")
    title = input("Enter a Story Title: ").strip()
    category = input("Enter the Category: ").strip()
    story_template = input("Paste your story template with placeholders (e.g., {noun}, {verb}):\n\n")

    placeholder = validate_placeholder(story_template)
    if not placeholder:
        print("❌ No placeholders found. Please include at least one placeholder in the format {noun}")
        return

    # Count existing templates
    try:
        with open(CUSTOM_STORIES, 'r') as file:
            existing = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        existing = []

    custom_id = generate_custom_id(title, len(existing))

    story_data = {
        "id": custom_id,
        "title": title,
        "category": category,
        "template": story_template,
        "placeholder": placeholder,
        "created_at": datetime.now().isoformat()
    }

    existing.append(story_data)
    with open(CUSTOM_STORIES, 'w') as file:
        json.dump(existing, file, indent=4)

    print(f"✅ Template '{title}' saved with ID: {custom_id}")


# List all templates
def list_template(filename=CUSTOM_STORIES):
    try:
        with open(filename, 'r') as file:
            templates = json.load(file)
            if not templates:
                print("No templates found!")
                return
            print("\nAvailable Templates:\n")
            for idx, t in enumerate(templates, 1):
                print(f"{idx}. {t['title']} ({t['category']}) [ID: {t['id']}]")
    except (FileNotFoundError, json.JSONDecodeError):
        print("❌ Template file not found or is corrupted!")


# View a specific template by ID
def view_template(t_id, filename=CUSTOM_STORIES):
    try:
        with open(filename, 'r') as f:
            file = json.load(f)
        for t in file:
            if t['id'] == t_id:
                print(json.dumps(t, indent=4))
                return
        print("❌ Template Not Found!")
    except (FileNotFoundError, json.JSONDecodeError):
        print("❌ Could not read the template file!")


# Update a specific template by ID
def update_template(t_id, filename=CUSTOM_STORIES):
    try:
        with open(filename, 'r') as f:
            templates = json.load(f)

        for t in templates:
            if t["id"] == t_id:
                print("Leave empty to keep existing values.")
                new_title = input(f"New Title (current: {t['title']}): ").strip() or t['title']
                new_category = input(f"New Category (current: {t['category']}): ").strip() or t['category']
                new_template = input(f"New Template (current: {t['template']}): ").strip() or t['template']
                placeholders = validate_placeholder(new_template)

                t.update({
                    "title": new_title,
                    "category": new_category,
                    "template": new_template,
                    "placeholder": placeholders
                })

                with open(filename, "w") as f:
                    json.dump(templates, f, indent=4)

                print("✅ Template updated successfully.")
                return

        print("❌ Template not found.")
    except (FileNotFoundError, json.JSONDecodeError):
        print("❌ Could not read the template file!")


# Delete a specific template by ID
def delete_template(t_id, filename=CUSTOM_STORIES):
    try:
        with open(filename, "r") as f:
            templates = json.load(f)

        new_templates = [t for t in templates if t["id"] != t_id]

        if len(new_templates) == len(templates):
            print("❌ No template found with that ID.")
            return

        with open(filename, "w") as f:
            json.dump(new_templates, f, indent=4)

        print("✅ Template deleted successfully.")
    except (FileNotFoundError, json.JSONDecodeError):
        print("❌ Could not read the template file!")


# CLI Menu
def template_crud_menu():
    while True:
        print("\n---- Template Manager ----")
        print("1. Create Template")
        print("2. List Templates")
        print("3. View Template by ID")
        print("4. Update Template")
        print("5. Delete Template")
        print("6. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            create_new_template()
        elif choice == "2":
            list_template()
        elif choice == "3":
            t_id = input("Enter Template ID to view: ").strip()
            view_template(t_id)
        elif choice == "4":
            t_id = input("Enter Template ID to update: ").strip()
            update_template(t_id)
        elif choice == "5":
            t_id = input("Enter Template ID to delete: ").strip()
            delete_template(t_id)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("❌ Invalid Option. Please try again.")

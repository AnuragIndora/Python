# app.py
import streamlit as st
import json
from datetime import datetime
from engine.madlibs_engine import (
    load_template, extract_placeholders, generate_story
)
from engine.history_manager import (
    save_story_to_history, load_history,
    search_history_by_keyword, get_stories_by_category
)
from engine.template_manager import (
    view_template, update_template, delete_template,
    validate_placeholder, save_template_to_file, generate_custom_id
)

STORY_PATH = "data/stories.json"
CUSTOM_STORY_PATH = "data/custom_story.json"

st.set_page_config(page_title="Mad Libs Generator", layout="centered")
st.title("📚 Mad Libs Story Generator")

menu = st.sidebar.radio("Choose an option:", ["Generate Story", "View History", "Manage Templates"])

if menu == "Generate Story":
    st.header("✨ Generate a Story")

    template_type = st.radio("Choose Template Type:", ["Inbuilt", "Custom"])

    file_to_load = STORY_PATH if template_type == "Inbuilt" else CUSTOM_STORY_PATH

    templates = load_template(file_to_load)
    if not templates:
        st.warning("No templates available.")
    else:
        categories = sorted(set(t['category'] for t in templates))
        category = st.selectbox("Choose a category:", categories)

        if category:
            filtered_templates = [t for t in templates if t["category"] == category]

            for selected_template in filtered_templates:
                st.subheader(f"Story: {selected_template['title']}")
                placeholders = extract_placeholders(selected_template['template'])

                with st.form(f"form_{selected_template['id']}"):
                    inputs = {
                        ph: st.text_input(f"Enter a {ph.replace('_', ' ')}", key=f"{selected_template['id']}_{ph}")
                        for ph in placeholders
                    }
                    submitted = st.form_submit_button("Generate Story")

                if submitted:
                    if all(inputs.values()):
                        story = generate_story(selected_template['template'], inputs)
                        st.success("✅ Your Mad Lib Story:")
                        st.write(story)

                        save_story_to_history({
                            "title": selected_template["title"],
                            "category": selected_template["category"],
                            "inputs": inputs,
                            "story": story
                        })
                    else:
                        st.error("Please fill out all fields!")

elif menu == "View History":
    st.header("🕓 Story History")
    history_data = load_history()

    if not history_data:
        st.warning("No stories in history yet.")
    else:
        st.subheader("📖 All Past Stories")
        for r in reversed(history_data):
            with st.expander(f"{r['template_title']} - {r['timestamp']}"):
                st.markdown(f"**Category:** {r['category']}")
                st.write(r['final_story'])

        st.markdown("---")
        st.subheader("🔍 Search in History")

        tab = st.radio("Search by:", ["Keyword", "Category"], horizontal=True)

        if tab == "Keyword":
            keyword = st.text_input("Enter a keyword to search in stories:")
            if keyword:
                results = search_history_by_keyword(keyword)
                if results:
                    st.success(f"Found {len(results)} result(s):")
                    for r in results:
                        with st.expander(f"{r['template_title']} - {r['timestamp']}"):
                            st.markdown(f"**Category:** {r['category']}")
                            st.write(r['final_story'])
                else:
                    st.info("No stories found with that keyword.")
        elif tab == "Category":
            all_categories = sorted(set(entry['category'] for entry in history_data))
            category = st.selectbox("Choose a category:", all_categories)
            if category:
                results = get_stories_by_category(category)
                if results:
                    st.success(f"Found {len(results)} story(ies) in '{category}'")
                    for r in results:
                        with st.expander(f"{r['template_title']} - {r['timestamp']}"):
                            st.write(r['final_story'])
                else:
                    st.info(f"No stories found in category '{category}'.")

elif menu == "Manage Templates":
    st.header("🧰 Template Manager")
    action = st.selectbox("Choose action", ["Create", "List", "View", "Update", "Delete"])

    if action == "Create":
        st.subheader("Add New Template")
        title = st.text_input("Story Title")
        category = st.text_input("Category")
        template = st.text_area("Story Template with {placeholders}")
        if st.button("Save Template"):
            try:
                with open("data/custom_story.json", "r") as f:
                    existing = json.load(f)
            except:
                existing = []

            placeholder = validate_placeholder(template)
            new_id = generate_custom_id(title, len(existing))
            story_data = {
                "id": new_id,
                "title": title,
                "category": category,
                "template": template,
                "placeholder": placeholder,
                "created_at": datetime.now().isoformat()
            }
            save_template_to_file(story_data)
            st.success(f"Template '{title}' saved with ID: {new_id}")

    elif action == "List":
        st.subheader("Available Templates")
        try:
            with open("data/custom_story.json", "r") as f:
                templates = json.load(f)
                for t in templates:
                    st.markdown(f"**{t['title']}** - *{t['category']}* [ID: `{t['id']}`]")
        except Exception as e:
            st.error(f"Error loading templates: {e}")

    elif action == "View":
        tid = st.text_input("Enter Template ID to View")
        if st.button("View"):
            view_template(tid)

    elif action == "Update":
        tid = st.text_input("Enter Template ID to Update")
        if st.button("Update"):
            update_template(tid)

    elif action == "Delete":
        tid = st.text_input("Enter Template ID to Delete")
        if st.button("Delete"):
            delete_template(tid)
            st.success("Template deleted.")

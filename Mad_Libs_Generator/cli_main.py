from engine.madlibs_engine import load_template, list_categories, select_template, extract_placeholders, fill_placeholders, generate_story, merge_story
from engine.history_manager import save_story_to_history, load_history, search_history_by_keyword, get_stories_by_category
from engine.template_manager import template_crud_menu

def fn_madlib_engine():
    merge_story()
    
    templates = load_template()
    if not templates:
        return

    categories = list_categories(templates=templates)
    selected_category = input("\nChoose a category (or press Enter for Random): ").strip()

    if selected_category and selected_category not in categories:
        print("Invalid category, choosing random...\n")
        selected_category = None

    selected_template = select_template(templates, selected_category)
    print(f"\nCategory: {selected_template['category']} - Title: {selected_template['title']}\n")

    placeholders = extract_placeholders(selected_template['template'])
    user_inputs = fill_placeholders(placeholders)
    final_story = generate_story(selected_template['template'], user_inputs)

    print("\nYour Generated Mad Lib Story:\n")
    print(final_story)

    story_data = {
        "title": selected_template["title"],
        "category": selected_template["category"],
        "inputs": user_inputs,
        "story": final_story  # Use "story" or "final_story" consistently
    }

    save_story_to_history(story_data=story_data)

def fn_hisotry_manager():
    print("Search Option: ")
    print("1. Search by keyword")
    print("2. Search by category")
    choice = input("Enter your choice (1 or 2): ").strip()

    if choice == "1":
        find_word = input("Enter keyword to search in history: ").strip()
        result = search_history_by_keyword(find_word)

        category_result = {}
        for entry in result:
            category = entry.get("category", "Unknown")
            category_result.setdefault(category, []).append(entry)

        for category, entries in category_result.items():
            print(f"\nCategory = {category}")
            for idx, entry in enumerate(entries, 1):
                print(f"{idx}. {entry['final_story']}")  # assuming 'story' is the key used

    elif choice == "2":
        category = input("Enter category name: ").strip()
        result = get_stories_by_category(category=category)
        print(f"\nStories under category '{category}':")
        for idx, entry in enumerate(result, 1):
            print(f"{idx}. {entry['final_story']}")  # assuming 'story' is the key used

    else:
        print("Invalid choice. Please enter 1 or 2.")


def fn_template_manager():
    template_crud_menu()

def main():
    print("Purpose of Visit:")
    print("1. Create a story")
    print("2. Check history")
    print("3. Template Manager")
    choice = input("Enter your choice (1 or 2 or 3): ").strip()

    if choice == "1":
        fn_madlib_engine()
    elif choice == "2":
        fn_hisotry_manager()
    elif choice == "3":
        fn_template_manager()
    else:
        print("Invalid choice. Please enter 1 or 2 or 3.")

if __name__ == '__main__':
    main()

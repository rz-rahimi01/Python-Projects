import json
import os
import random
import string

DB_FILE = "urls.json"
BASE_URL = "http://short.ly/"

# Load URL database
def load_urls():
    if not os.path.exists(DB_FILE):
        return {}
    with open(DB_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}

# Save URL database
def save_urls(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=4)

# Generate short code
def generate_code(length=6):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

# Shorten a URL
def shorten_url(original_url):
    urls = load_urls()

    # Avoid duplicates
    for code, url in urls.items():
        if url == original_url:
            print(f"🔗 Already shortened: {BASE_URL}{code}")
            return

    code = generate_code()
    while code in urls:  # Ensure uniqueness
        code = generate_code()

    urls[code] = original_url
    save_urls(urls)
    print(f"✅ Short URL: {BASE_URL}{code}")

# Retrieve original URL
def retrieve_url(code):
    urls = load_urls()
    if code in urls:
        print(f"🔍 Original URL: {urls[code]}")
    else:
        print("❌ Code not found.")

# Show all URLs
def list_urls():
    urls = load_urls()
    if not urls:
        print("📭 No URLs stored.")
        return
    print("\n===== STORED URLS =====")
    for code, url in urls.items():
        print(f"{BASE_URL}{code} → {url}")

# Menu
def main():
    while True:
        print("\n===== URL SHORTENER =====")
        print("1. Shorten a URL")
        print("2. Retrieve original URL")
        print("3. List all URLs")
        print("4. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            url = input("Enter the original URL: ").strip()
            shorten_url(url)
        elif choice == "2":
            code = input("Enter the short code: ").strip()
            retrieve_url(code)
        elif choice == "3":
            list_urls()
        elif choice == "4":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice.")

if __name__ == "__main__":
    main()

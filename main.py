# Import required libraries
from playwright.sync_api import sync_playwright
from supabase import create_client
import re

# -----------------------------
# SUPABASE CONFIGURATION
# -----------------------------

# Replace these with your actual credentials
SUPABASE_URL = "https://iydkqdjkxiqnvarhjgke.supabase.co/"
SUPABASE_KEY = "sb_publishable_w_n0BVy4DhIZ5GdPCqWYOA_nNT58ztP"

# Create Supabase client
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)


def scrape_github_profile():
    """
    This function opens GitHub profile,
    extracts required data,
    and returns it as a dictionary.
    """

    with sync_playwright() as p:
        # Launch Chromium browser (headless=False to see browser)
        browser = p.chromium.launch(headless=False)

        # Open new browser page
        page = browser.new_page()

        # Navigate to GitHub profile
        page.goto("https://github.com/shantanujain18")

        # Wait for page to load properly
        page.wait_for_selector('span[itemprop="additionalName"]')

        # -----------------------------
        # Extract Username
        # -----------------------------
        username = page.locator('span[itemprop="additionalName"]').first.inner_text().strip()

        # -----------------------------
        # Extract Name (if exists)
        # -----------------------------
        try:
            name = page.locator('span[itemprop="name"]').first.inner_text().strip()
            if not name:
                name = "Not Provided"
        except:
            name = "Not Provided"

        # -----------------------------
        # Extract Bio (if exists)
        # -----------------------------
        try:
            bio = page.locator('div.user-profile-bio').first.inner_text().strip()
        except:
            bio = "Not Provided"

        # -----------------------------
        # Extract Followers
        # -----------------------------
        followers_text = page.locator('a[href$="?tab=followers"]').first.inner_text()
        followers = int(re.search(r"\d+", followers_text).group())

        # -----------------------------
        # Extract Following
        # -----------------------------
        following_text = page.locator('a[href$="?tab=following"]').first.inner_text()
        following = int(re.search(r"\d+", following_text).group())

        # -----------------------------
        # Extract Repositories Count
        # -----------------------------
        repos_text = page.locator('a[href$="?tab=repositories"]').first.inner_text()
        repositories = int(re.search(r"\d+", repos_text).group())

        # Close browser
        browser.close()

        # Return scraped data as dictionary
        return {
            "username": username,
            "name": name,
            "bio": bio,
            "followers": followers,
            "following": following,
            "repositories": repositories
        }


def insert_into_supabase(data):
    """
    This function inserts scraped data into Supabase table.
    """

    try:
        response = supabase.table("github_profiles").insert(data).execute()
        print("Data inserted successfully into Supabase!")
        print(response)

    except Exception as e:
        print("Error inserting into Supabase:")
        print(e)


# -----------------------------
# MAIN EXECUTION
# -----------------------------

if __name__ == "__main__":

    print("Starting GitHub Scraper...")

    # Step 1: Scrape data
    profile_data = scrape_github_profile()

    print("Scraped Data:")
    print(profile_data)

    # Step 2: Insert into Supabase
    insert_into_supabase(profile_data)

    print("Process completed successfully!")
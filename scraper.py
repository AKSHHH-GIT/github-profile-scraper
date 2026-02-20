# Import sync Playwright API
from playwright.sync_api import sync_playwright
import re  # Used for extracting only numbers


def extract_number(text):
    """
    Extracts only numeric part from text.
    Example:
        '25 followers' → 25
    """
    numbers = re.findall(r'\d+', text.replace(",", ""))
    return int(numbers[0]) if numbers else 0


# Start Playwright context
with sync_playwright() as p:
    
    # Launch Chromium browser
    # headless=False → Opens visible browser (good for debugging)
    browser = p.chromium.launch(headless=False)
    
    # Create new browser page
    page = browser.new_page()
    
    # Go to GitHub profile
    page.goto("https://github.com/shantanujain18")
    
    # Wait until page fully loads
    page.wait_for_load_state("networkidle")
    
    
    # ===============================
    # Extract Username
    # ===============================
    username = page.locator('span[itemprop="additionalName"]').inner_text().strip()
    
    
    # ===============================
    # Extract Full Name
    # ===============================
    try:
        name = page.locator(
            'span[itemprop="name"]'
        ).first.inner_text().strip()

        if not name:
            name = "Not Provided"

    except:
        name = "Not Provided"

    
    
    # ===============================
    # Extract Bio (Optional Field)
    # ===============================
    bio_locator = page.locator("div.p-note")
    
    if bio_locator.count() > 0:
        bio = bio_locator.inner_text().strip()
    else:
        bio = "No bio available"
    
    
    # ===============================
    # Extract Followers Count
    # ===============================
    followers_text = page.locator(
        'a[href$="?tab=followers"] span.text-bold'
    ).first.inner_text()
    
    followers = extract_number(followers_text)
    
    
    # ===============================
    # Extract Following Count
    # ===============================
    following_text = page.locator(
        'a[href$="?tab=following"] span.text-bold'
    ).first.inner_text()
    
    following = extract_number(following_text)
    
    
    # ===============================
    # Extract Repository Count
    # ===============================
    repo_text = page.locator(
        'a[href$="?tab=repositories"] span.Counter'
    ).first.inner_text()
    
    repositories = extract_number(repo_text)
    
    
    # ===============================
    # Print Extracted Data
    # ===============================
    print("\n===== GitHub Profile Data =====")
    print("Username:", username)
    print("Name:", name)
    print("Bio:", bio)
    print("Followers:", followers)
    print("Following:", following)
    print("Repositories:", repositories)
    
    
    # Close browser
    browser.close()
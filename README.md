GitHub Profile Scraper using Playwright + Supabase
 What This Project Does

This project automatically:

Opens a GitHub profile page like a real human (using browser automation).

Reads important information from the profile.

Stores that information into an online database (Supabase).

Instead of manually copying data, this script does everything automatically.

Objective

Open a GitHub profile page using automation, extract specific details, and save them into a database table.

The 6 fields collected are:

| username | name | bio | followers | following | repositories |
| -------- | ---- | --- | --------- | --------- | ------------ |

Architeture:
Playwright Script
        ↓
Opens GitHub Profile
        ↓
Extracts Required Data
        ↓
Python Processes Data
        ↓
Sends Data to Supabase
        ↓
Supabase Stores in Database Table

Technologies Used
1️⃣ Playwright

Playwright is a browser automation tool.

It allows Python to:

Open Chrome/Firefox

Visit websites

Click buttons

Extract text

Fill forms

In this project, Playwright controls a real browser like a human user.

2️⃣ Supabase

Supabase is an open-source backend platform.

It provides:

Hosted PostgreSQL database

Dashboard UI

REST APIs

Authentication

In this project, Supabase is used as the online database where scraped data is stored.

 Step-by-Step Implementation
 Phase 1 — Environment Setup

1.Installed Python

2.Created virtual environment:

python -m venv venv

3.Activated virtual environment

4.Installed required packages:

pip install playwright
pip install supabase

5.Installed browser binaries:

playwright install

6.Created project folder:

github-profile-scraper

7.Created Python files:

scraper.py

main.py

* Phase 2 — Scraping GitHub Profile (Playwright) *
What Was Done:

-Imported Playwright sync API
-Launched Chromium browser
-Opened GitHub profile page:

https://github.com/shantanujain18

-Used browser DevTools to inspect HTML
-Identified stable selectors using:

a.itemprop
b.href
c.class

Extracted the Following Data:

-Username
-Name (handled case where name is missing)
-Bio (handled optional case)
-Followers
-Following
-Repository count

Important Improvements Made:

-Cleaned numeric values using regex (removed commas/text)
-Handled strict mode violation using .first()
-Added default value "Not Provided" for missing name
Structured output in dictionary format

Example Output:

{
  'username': 'Shantanujain18',
  'name': 'Not Provided',
  'bio': 'Learning to build full-stack websites using Django',
  'followers': 2,
  'following': 3,
  'repositories': 25
}

Phase 3 — Created Supabase Table

Created a table in Supabase with columns:

| Column Name  | Data Type |
| ------------ | --------- |
| username     | text      |
| name         | text      |
| bio          | text      |
| followers    | integer   |
| following    | integer   |
| repositories | integer   |


Phase 4 — Connect Python to Supabase

-Installed Supabase Python client
-Added project URL and API key
-Successfully connected to Supabase
-Tested manual row insertion

Example test result:

Supabase connected successfully!
Row inserted successfully!

Phase 5 — Integrated Scraper + Supabase

Final Flow:

1.Scrape data
2.Store data in dictionary
3.Insert into Supabase
4.Add error handling
5.Print clean logs
6.Close browser properly

Final terminal output:

Starting GitHub Scraper...
Scraped Data:
{...}
Data inserted successfully into Supabase!
Process completed successfully!

import requests
from bs4 import BeautifulSoup
import csv

BASE_URL = "https://www.scrapethissite.com"

# Home page
current_url = "/pages/forms/?page_num=1"

# List for storing all data
all_teams = []

while True:
    # Loading the page
    response = requests.get(BASE_URL + current_url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all table rows with the class "team"
    rows = soup.find_all("tr", class_="team")

    for row in rows:
        team_name = row.find("td", class_="name").get_text(strip=True)
        year = row.find("td", class_="year").get_text(strip=True)
        wins = row.find("td", class_="wins").get_text(strip=True)
        losses = row.find("td", class_="losses").get_text(strip=True)
        ot_losses = row.find("td", class_="ot-losses").get_text(strip=True)
        win_pct = row.find("td", class_="pct").get_text(strip=True)
        goals_for = row.find("td", class_="gf").get_text(strip=True)
        goals_against = row.find("td", class_="ga").get_text(strip=True)
        diff = row.find("td", class_="diff").get_text(strip=True)

        all_teams.append([
            team_name, year, wins, losses, ot_losses,
            win_pct, goals_for, goals_against, diff
        ])

    # Looking for the "Next" button
    next_button = soup.find("a", {"aria-label": "Next"})
    if next_button:
        # Get a link to the next page
        next_href = next_button.get("href")
        # If the link leads to the same page, then we have reached the end.
        if next_href == current_url:
            break
        current_url = next_href
    else:
        # There is no "Next" button - the end
        break

# Saving data to CSV
with open("teams_stats.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([
        "Team Name", "Year", "Wins", "Losses", "OT Losses",
        "Win %", "Goals For (GF)", "Goals Against (GA)", "+/-"
    ])
    writer.writerows(all_teams)

print(f"The data is saved in teams_stats.csv. Total records: {len(all_teams)}")

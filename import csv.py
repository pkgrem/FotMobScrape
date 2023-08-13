import csv
import requests

def fetch_json_from_url(url):
    """Fetch JSON data from a URL."""
    response = requests.get(url)
    return response.json()

def json_to_csv(json_data, csv_filename):
    """Convert JSON data to CSV."""
    if 'statsData' in json_data:
        stats_data_list = json_data['statsData']
        if stats_data_list:
            keys = stats_data_list[0].keys()
            with open(csv_filename, 'w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=keys)
                writer.writeheader()
                for stat_data in stats_data_list:
                    writer.writerow(stat_data)
            print(f"Data written to {csv_filename}")
        else:
            print(f"No stats data found for {csv_filename}")
    else:
        print(f"Unexpected data format for {csv_filename}. Data keys: {json_data.keys()}")

# Base URL
base_url = "https://www.fotmob.com/api/leagueseasondeepstats?id=47&season=20720&type=players&stat="

# List of sub-queries (stat parameters)
stats_parameters = [
    "accurate_long_balls", "accurate_pass", "goal_assist", "big_chance_created",
    "big_chance_missed", "outfielder_block", "total_att_assist", "clean_sheet",
    "effective_clearance", "expected_assists", "expected_assists_per_90", "expected_goals",
    "expected_goals_per_90", "expected_goalsontarget", "rating", "fouls",
    "_goals_and_goal_assist", "goals_conceded", "goals_per_90", "_goals_prevented",
    "interception", "penalty_conceded", "penalty_won", "poss_won_att_3rd",
    "red_card", "_save_percentage", "saves", "ontarget_scoring_att",
    "total_scoring_att", "won_contest", "won_tackle", "goals",
    "_expected_goals_and_expected_assists_per_90", "yellow_card"
]

# Fetch data for each stat parameter and save to CSV
for stat in stats_parameters:
    url = base_url + stat
    data = fetch_json_from_url(url)
    csv_filename = f"stats_data_{stat}.csv"
    json_to_csv(data, csv_filename)

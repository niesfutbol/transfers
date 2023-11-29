import json

team_id = "50"
with open(f"tests/data/data_file_{team_id}_team_transfer.json") as f:
    data = json.load(f)

transfers = data["response"]

last_years_transfer = [
    transfer
    for transfer in transfers
    if (int(transfer["transfers"][0]["date"][0:4])>=2022)
]

outcity = [
    transfer
    for transfer in last_years_transfer
    if transfer["transfers"][0]["teams"]["out"]["id"] == team_id
]

incity = [
    transfer
    for transfer in last_years_transfer
    if transfer["transfers"][0]["teams"]["in"]["id"] == team_id
]
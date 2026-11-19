# Zeus Strikers

Zeeshan Arshad’s fantasy XI for the Advanced Python for AI Dugout League, PSL 2026.

## Run the assignment

Unzip the project and open its folder in VS Code. Run the PDF’s standalone program in the terminal with Python 3.

```sh
python zeeshan_zeus.py
```

The program prints the 11 players in the order shown in the PDF, their total of 99.0 credits, the role counts, and both captain selections. The team has one wicket-keeper, four batters, two all-rounders, and four bowlers. Shadab Khan (`P029`) is captain with 2× points, and Sikandar Raza (`P065`) is vice-captain with 1.5× points.

## Check the CSV roster

```sh
python scratch.py
```

The validator loads the CSV roster, checks the team selection rules, and reports the largest franchise group. Zeus Strikers has four Lahore Qalandars players against the limit of seven. Both scripts use Python’s standard library.

| File | Purpose |
|---|---|
| `zeeshan_zeus.py` | Standalone assignment program from pages 2–4 of the PDF |
| `models.py` | Reusable `Player`, `FantasyTeam`, and `League` classes |
| `loader.py` | CSV readers for players and teams |
| `rules.py` | Squad size, credit budget, franchise, role, and captain checks |
| `scratch.py` | Runs the CSV roster through the rule checks |
| `data/players.csv` | The 11 players selected in the PDF |
| `data/my_team.csv` | Roster order and captain selections for Zeus Strikers |

The CSV reader accepts the course role codes `WK`, `BAT`, `AR`, and `BOWL` and displays their full role names. When creating a player in Python, pass the role before the franchise as shown in the PDF.

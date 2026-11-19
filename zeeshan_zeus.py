class Player:
    def __init__(self, player_id, name, role, franchise, credits):
        self.player_id = player_id
        self.name = name
        self.role = role
        self.franchise = franchise
        self.credits = credits

    def __str__(self):
        return (
            f"{self.name} ({self.franchise}, "
            f"{self.role}, {self.credits} cr)"
        )


class FantasyTeam:
    def __init__(self, team_name, owner):
        self.team_name = team_name
        self.owner = owner
        self.players = []
        self.captain = None
        self.vice_captain = None

    def add_player(self, player):
        self.players.append(player)

    def total_credits(self):
        total = 0
        for player in self.players:
            total += player.credits
        return total

    def count_by_role(self):
        counts = {}
        for player in self.players:
            if player.role not in counts:
                counts[player.role] = 0
            counts[player.role] += 1
        return counts

    def set_captain(self, captain, vice_captain):
        self.captain = captain
        self.vice_captain = vice_captain

    def __str__(self):
        size = len(self.players)
        cost = self.total_credits()
        return (
            f"{self.team_name} (owner: {self.owner}, "
            f"{size} players, {cost} cr)"
        )


rizwan = Player(
    "P122", "Mohammad Rizwan", "Wicket-keeper", "Rawalpindiz", 10.5
)

babar = Player(
    "P089", "Babar Azam", "Batter", "Peshawar Zalmi", 10.5
)

fakhar = Player(
    "P056", "Fakhar Zaman", "Batter", "Lahore Qalandars", 8.5
)

smith = Player(
    "P075", "SPD Smith", "Batter", "Multan Sultans", 7.5
)

shan = Player(
    "P076", "Shan Masood", "Batter", "Multan Sultans", 6.0
)

shadab = Player(
    "P029", "Shadab Khan", "All-rounder", "Islamabad United", 10.5
)

sikandar = Player(
    "P065", "Sikandar Raza", "All-rounder", "Lahore Qalandars", 10.0
)

shaheen = Player(
    "P068", "Shaheen Shah Afridi", "Bowler", "Lahore Qalandars", 10.5
)

haris = Player(
    "P066", "Haris Rauf", "Bowler", "Lahore Qalandars", 7.5
)

abrar = Player(
    "P114", "Abrar Ahmed", "Bowler", "Quetta Gladiators", 9.5
)

naseem = Player(
    "P140", "Naseem Shah", "Bowler", "Rawalpindiz", 8.0
)


team = FantasyTeam("Zeus Strikers", "Zeeshan Arshad")

for player in [
    rizwan, babar, fakhar, smith, shan, shadab,
    sikandar, shaheen, haris, abrar, naseem
]:
    team.add_player(player)

team.set_captain(shadab, sikandar)

print(team)

print("\nPlayers:")
for player in team.players:
    print(player)

print("\nTotal players:", len(team.players))
print("Total credits:", team.total_credits())
print("Players by role:", team.count_by_role())
print("Captain:", team.captain.name)
print("Vice-captain:", team.vice_captain.name)

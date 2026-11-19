class Player:
    def __init__(self, player_id, name, role, franchise, credits):
        self.player_id = player_id
        self.name = name
        self.role = role
        self.franchise = franchise
        self.credits = credits

    def __str__(self):
        return f"{self.name} ({self.franchise}, {self.role}, {self.credits} cr)"


# Create six player objects
babar = Player("P089", "Babar Azam", "Batter", "Peshawar Zalmi", 10.5)
rizwan = Player("P122", "Mohammad Rizwan", "Wicket-keeper", "Rawalpindiz", 10.5)
fakhar = Player("P056", "Fakhar Zaman", "Batter", "Lahore Qalandars", 8.5)
shadab = Player("P029", "Shadab Khan", "All-rounder", "Islamabad United", 10.5)
shaheen = Player("P068", "Shaheen Shah Afridi", "Bowler", "Lahore Qalandars", 10.5)
haris = Player("P066", "Haris Rauf", "Bowler", "Lahore Qalandars", 7.5)

# Print all six using a loop
print("My Team: Code Strikers")

for player in [babar, rizwan, fakhar, shadab, shaheen, haris]:
    print(player)
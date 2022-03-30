import random
from art import logo, vs
from game_data import data

def format_data(account):
  """Format account data in printable format"""
  account_name = account["name"]
  account_descr = account["description"]
  account_country = account["country"]
  # print(f'{name}: {account["follower_count"]}')
  return f"{account_name}, a {account_descrdescr}, from {account_country}"

# Display game art
print(logo)

# Generate random account from game data
option_a = random.choice(data)
option_b = random.choice(data)
if option_a == option_b:
  option_b = random.choice(data)

print(f"Compare A: {format_data(option_a)}.")
print(vs)
print(f"Against B: {format_data(option_b)}.")

# Ask user for input
input("Who has more followers A or B?: ")

# Get number of followers 
# Check if users input answer is correct
# Give user feedback on answer
# Keep score for player
# Make the game repeatable
# Make account B replaced account A on next round
# Make screen clear better next round
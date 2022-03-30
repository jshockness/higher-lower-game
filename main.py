import random
from art import logo, vs
from game_data import data
from replit import clear

def format_data(account):
  """Format account data in printable format"""
  account_name = account["name"]
  account_descr = account["description"]
  account_country = account["country"]
  # print(f'{name}: {account["follower_count"]}')
  return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(guess, a_followers, b_followers):
  """Take users guess  and followers to check if user is right"""
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"

# Display game art
print(logo)
# Keep score for player
score = 0
should_continue = True
# Make account B replaced account A on next round
option_b = random.choice(data)

# Make the game repeatable
while should_continue:
  # Generate random account from game data
  option_a = option_b
  option_b = random.choice(data)
  while option_a == option_b:
    option_b = random.choice(data)
  
  print(f"Compare A: {format_data(option_a)}.")
  print(vs)
  print(f"Against B: {format_data(option_b)}.")
  
  # Ask user for input
  guess = input("Who has more followers 'A' or 'B': ").lower()
  
  # Get number of followers 
  a_followers = option_a["follower_count"]
  b_followers = option_b["follower_count"]
  
  is_correct = check_answer(guess, a_followers, b_followers)

  # Make screen clear better next round
  clear()
  print(logo)
  
  # Check if users input answer is correct
  # Give user feedback on answer
  if is_correct:
    score += 1
    print(f"You're right. Current score: {score}")
  else:
    print(f"Sorry you lose. Final score: {score}")
    should_continue = False

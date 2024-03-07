import random

def choose_options():
  options = ('rock', 'paper', 'scissor')
  user_opt = input("Enter a choice (rock, paper, scissors): ")
  user_opt = user_opt.lower()

  if user_opt not in options:
    print("Invalid option")
    #continue
    return None, None
    
  computer_opt = random.choice(options)
  
  print('User option =>', user_opt)
  print('Computer option =>', computer_opt)
  return user_opt,computer_opt

def check_rules(user_opt, computer_opt, user_wins, computer_wins):
  if user_opt == computer_opt:
    print('Empate')
  elif user_opt == "rock":
    if computer_opt == 'scissors':
      print('Ganaste')
      user_wins += 1
    else:
      print('Perdiste')
      computer_wins += 1
  elif user_opt == 'paper':
    if computer_opt == 'rock':
      print('Ganaste')
      user_wins += 1
    else:
      print('Perdiste')
      computer_wins += 1
  elif user_opt == 'scissors':
    if computer_opt == 'paper':
      print('Ganaste')
      user_wins += 1
    else:
      print('Perdiste')
      computer_wins += 1
      
  return user_wins, computer_wins
  
def run_game():
  
  rounds = 1
  computer_wins = 0
  user_wins = 0
  
  while True:
    print(' ' * 10)
    print('*' * 10)
    print('ROUND', rounds)
    print('*' * 10)

    print('Computer wins', computer_wins)
    print('User wins', user_wins)

    rounds += 1

    user_opt, computer_opt = choose_options()
    user_wins, computer_wins = check_rules(user_opt, computer_opt, user_wins, computer_wins)

    if computer_wins == 2:
      print('El ganador es la computadora')
      break
    if user_wins == 2:
      print('El ganador es el usuario')
      break

run_game()
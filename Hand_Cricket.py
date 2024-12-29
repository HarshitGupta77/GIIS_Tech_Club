from colorama import Fore, init
init(autoreset=True)
import random
import time

print(" --- Hand Cricket ---")

a = ""          # I used this for adding spaces between the lines
print(a)
print(a)


print(f"{Fore.YELLOW}Let's Begin: ")
print(a)

# Toss 
z = ["odd or eve"]
z = str(input("Odd or Eve?: "))

z == "odd" or z =="eve"
total = 0
numbers=[1,2,3,4,5,6]

if z.lower() == "odd" or z.lower() == "eve":
  your_toss = int(input("Ok, your toss: "))
  if your_toss in numbers:
    pass
  else:
    while your_toss not in numbers:
      print("Please choose a number between 1 to 6")
      your_toss = int(input("Ok, your toss: "))
      if your_toss in numbers:
        break
  
else:
    while z.lower() != "odd" or z.lower() != "eve":
      print("Please choose odd or eve")
      z = str(input("Odd or Eve? : "))
      if z.lower() == "odd" or z.lower() == "eve":
        your_toss = int(input("Ok, your toss: "))
        break


comp_toss = (random.choice([1, 2, 3, 4, 5, 6]))
print(f"Computer Toss: {comp_toss}")

sum_toss = your_toss + comp_toss
if sum_toss % 2 == 0 and z == "eve":
    c = True                              # When we win toss, c = True
    print(f"{Fore.GREEN}You won toss")
elif sum_toss % 2 != 0 and z == "odd":
    c = True
    print(f"{Fore.GREEN}You won toss")
else:
  c = False                               # When we lose toss, c = False
  print(f"{Fore.RED}Computer won toss")
# Toss done


# Choosing Bat / Bowl:
if c == True:
  you_choose = str(input("Bat or Bowl?: "))
else:
  comp_choice = (random.choice(["Bat", "Bowl"]))
  time.sleep(1)
  print(f"Computer chose to: {comp_choice}" )
# Choosing Bat / Bowl done


# Match Start
print(a)
print(a)
print(" ----- 1st Innings ----- ")
print(a)
print(a)

# Case 1 : When we win toss and choose to bowl
total_runs = 0
your_turn = [1, 2, 3, 4, 5, 6] 
comp_turn = [1, 2, 3, 4, 5, 6]
if c == True and you_choose.lower() == "bowl":
  comp_turn = random.choice([1, 2, 3, 4, 5, 6])
       
  while your_turn != comp_turn:
    your_turn = int(input("You Bowl(Pls enter number between 1 to 6): ")) 
    if your_turn in numbers:
      pass
    else:
      while your_turn not in numbers:
        print("Please enter a number between 1 to 6")
        your_turn = int(input("You Bowl(Pls enter number between 1 to 6): "))
        if your_turn in numbers:
          break
    comp_turn = random.choice([1, 2, 3, 4, 5, 6])
    print(f"{Fore.MAGENTA}Computer Bats: " + str(comp_turn))
    total_runs += comp_turn

    if your_turn == comp_turn:
      print(f"{Fore.RED}THATS OUT!!! ")
      total_runs -= comp_turn
      print(f"{Fore.YELLOW}Target: {total_runs + 1}")
      target = total_runs + 1
      break
    

  print(a)
  print(a)
  print(" ----- 2nd Innings -----")
  print(a)
  print(a)

  total_runs = 0
  your_turn = [1, 2, 3, 4, 5, 6] 
  
  comp_turn = random.choice([1, 2, 3, 4, 5, 6])
  while your_turn != comp_turn:
    your_turn = int(input("You Bat(Pls enter number between 1 to 6): ")) 
    if your_turn in numbers:
      pass
    else:
      while your_turn not in numbers:
        print("Please enter a number between 1 to 6")
        your_turn = int(input("You Bat(Pls enter number between 1 to 6): "))
        if your_turn in numbers:
          break
    comp_turn = random.choice([1, 2, 3, 4, 5, 6])
    print(f"{Fore.BLUE}Computer Bowls: " + str(comp_turn))
    total_runs += your_turn
    k = total_runs
   
    if target <= k:
      print("Score " + str(total_runs))
      print(f"{Fore.GREEN}You Win!!! ")
      break

    if your_turn == comp_turn:
      print(f"{Fore.RED}THATS OUT!!! ")
      total_runs -= your_turn
      h = total_runs
      print(f"Score: {total_runs}")
      if h < target:
        print(f"{Fore.RED}Computer Wins!!! ")
      else:
        print(f"{Fore.GREEN}You Win!!! ")
        break
      


# Case 2: When we win toss and choose to bat
  total_runs = 0
  your_turn = [1, 2, 3, 4, 5, 6] 
  comp_turn = [1, 2, 3, 4, 5, 6]
elif c == True and you_choose.lower() == "bat":
  comp_turn = random.choice([1, 2, 3, 4, 5, 6])

  while your_turn != comp_turn:
    your_turn = int(input("You Bat(Pls enter number between 1 to 6): ")) 
    if your_turn in numbers:
      pass
    else:
      while your_turn not in numbers:
        print("Please enter a number between 1 to 6")
        your_turn = int(input("You Bat(Pls enter number between 1 to 6): "))
        if your_turn in numbers:
          break
    comp_turn = random.choice([1, 2, 3, 4, 5, 6])
    print(f"{Fore.BLUE}Computer Bowls: " + str(comp_turn))
    total_runs += your_turn

    if your_turn == comp_turn:
      print(f"{Fore.RED}THATS OUT!!! ")
      total_runs -= your_turn
      target = total_runs
      print("Target: " + str(total_runs + 1))
      break

    
  print(a)
  print(a)
  print(" ----- 2nd Innings -----")
  print(a)
  print(a)

  total_runs = 0
  your_turn = [1, 2, 3, 4, 5, 6] 
  comp_turn = random.choice([1, 2, 3, 4, 5, 6])
  while your_turn != comp_turn:
    your_turn = int(input("You Bowl(Pls enter number between 1 to 6): ")) 
    if your_turn in numbers:
      pass
    else:
      while your_turn not in numbers:
        print("Please enter a number between 1 to 6")
        your_turn = int(input("You Bowl(Pls enter number between 1 to 6): "))
        if your_turn in numbers:
          break
    comp_turn = random.choice([1, 2, 3, 4, 5, 6])
    print(f"{Fore.MAGENTA}Computer Bat: {comp_turn}")
    total_runs += comp_turn
    h = total_runs
    if target < h:
      print(f"Score: {total_runs}")
      print(f"{Fore.RED}Computer Wins!!! ")
      break

    
    if your_turn == comp_turn:
      print(f"{Fore.RED}THATS OUT!!! ")
      total_runs -= comp_turn
      h = total_runs
      print(f"Score: {total_runs}")
      if h < target:
        print(f"{Fore.GREEN}You Win!!! ")
      else:
        print(f"{Fore.RED}Computer Wins!!! ")
        break
        

# Case 3: Comp wins toss and chooses to bowl
  total_runs = 0
  your_turn = [1, 2, 3, 4, 5, 6] 
  comp_turn = [1, 2, 3, 4, 5, 6]
elif c == False and comp_choice == "Bowl": 
  comp_turn = random.choice([1, 2, 3, 4, 5, 6])

  while your_turn != comp_turn:
    your_turn = int(input("You Bat(Pls enter number between 1 to 6): ")) 
    if your_turn in numbers:
      pass
    else:
      while your_turn not in numbers:
        print("Please enter a number between 1 to 6")
        your_turn = int(input("You Bat(Pls enter number between 1 to 6): "))
        if your_turn in numbers:
          break
    comp_turn = random.choice([1, 2, 3, 4, 5, 6])
    print(f"{Fore.BLUE}Computer Bowls: {comp_turn}")
    total_runs += your_turn

    if your_turn == comp_turn:
      print(f"{Fore.RED}THATS OUT!!! ")
      total_runs -= your_turn
      target = total_runs
      print(f"Target: {total_runs + 1}")
      break

    
  print(a)
  print(a)
  print(" ----- 2nd Innings -----")
  print(a)
  print(a)


  total_runs = 0
  your_turn = [1, 2, 3, 4, 5, 6] 
  comp_turn = random.choice([1, 2, 3, 4, 5, 6])
  while your_turn != comp_turn:
    your_turn = int(input("You Bowl(Pls enter number between 1 to 6): ")) 
    if your_turn in numbers:
      pass
    else:
      while your_turn not in numbers:
        print("Please enter a number between 1 to 6")
        your_turn = int(input("You Bowl(Pls enter number between 1 to 6): "))
        if your_turn in numbers:
          break
    comp_turn = random.choice([1, 2, 3, 4, 5, 6])
    print(f"{Fore.MAGENTA}Computer Bats: {comp_turn}")
    total_runs += comp_turn
    h = total_runs
    if target < h:
      print(f"Score: {total_runs}")
      print(f"{Fore.RED}Compter Wins!!! ")
      break

    
    if your_turn == comp_turn:
      print(f"{Fore.RED}THATS OUT!!! ")
      total_runs -= comp_turn
      h = total_runs
      print(f"Score: {total_runs}")
      if h < target:
        print(f"{Fore.GREEN}You Win!!! ")
      else:
        print(f"{Fore.RED}Computer Wins!!! ")
        break



# Case 4: Comp wins toss and chooses to bat
  total_runs = 0
  your_turn = [1, 2, 3, 4, 5, 6] 
  comp_turn = [1, 2, 3, 4, 5, 6]
elif c == False and comp_choice == "Bat":
  comp_turn = random.choice([1, 2, 3, 4, 5, 6])

  while your_turn != comp_turn:
    your_turn = int(input("You Bowl(Pls enter number between 1 to 6): ")) 
    if your_turn in numbers:
      pass
    else:
      while your_turn not in numbers:
        print("Please enter a number between 1 to 6")
        your_turn = int(input("You Bowl(Pls enter number between 1 to 6): "))
        if your_turn in numbers:
          break
    comp_turn = random.choice([1, 2, 3, 4, 5, 6])
    print(f"{Fore.MAGENTA}Computer Bats: {comp_turn}")
    total_runs += comp_turn
    

    if your_turn == comp_turn:
      print(f"{Fore.RED}THATS OUT!!! ")
      total_runs -= comp_turn
      target = total_runs
      print(f"Target: {total_runs + 1}")
      break


  print(a)
  print(a)
  print(" ----- 2nd Innings -----")
  print(a)
  print(a)

  total_runs = 0
  your_turn = [1, 2, 3, 4, 5, 6] 
  comp_turn = random.choice([1, 2, 3, 4, 5, 6])
  while your_turn != comp_turn:
    your_turn = int(input("You Bat(Pls enter number between 1 to 6): ")) 
    if your_turn in numbers:
      pass
    else:
      while your_turn not in numbers:
        print("Please enter a number between 1 to 6")
        your_turn = int(input("You Bat(Pls enter number between 1 to 6): "))
        if your_turn in numbers:
          break
    comp_turn = random.choice([1, 2, 3, 4, 5, 6])
    print(f"{Fore.BLUE}Computer Bowls: " + str(comp_turn))
    total_runs += your_turn
    h = total_runs
    if target < h:
      print("Score " + str(h))
      print(f"{Fore.GREEN}You Win!!! ")
      break

    if your_turn == comp_turn:
      print(f"{Fore.RED}THATS OUT!!! ")
      total_runs -= your_turn
      h = total_runs
      print("Score " + str(total_runs))
      if h > target:
        print(f"{Fore.GREEN}You Win!!! ")
      else:
        print(f"{Fore.RED}Computer Wins!!! ")
        break


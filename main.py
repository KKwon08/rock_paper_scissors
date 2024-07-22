import random

user_input = input("select one of the following, rock, paper, scissors \n")

options = ["rock", "paper", "scissors"]

num_options = len(options)

random_int = random.randint(0, num_options -1)

random_option = options[random_int]

print(random_option)

if random_option == user_input:
    print("Its a draw!")

if random_option == "paper" and user_input == "rock":
    print("YOU LOSE!")

if user_input == "paper" and random_option == "rock":
    print("YOU WIN!")


if random_option == "rock" and user_input == "scissors":
    print("YOU LOSE!")

if user_input == "rock" and random_option == "scissors":
    print("YOU WIN!")

if random_option == "scissors" and user_input == "paper":
    print("YOU LOSE!")

if random_option == "paper" and user_input == "scissors":
    print("YOU WIN!")



import random


def get_choices():
    player_chioice = "Test"
    return player_chioice
play =print(get_choices())
dict = ["Rock","Scissor","Paper"]
answe=input("Please enter anser:")
if answe==random.choice(dict):
    print("Pass")
else:
    print("fail")

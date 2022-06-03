from random import choice


rand_dict = {
  "P": "Paper",
  "R": "Rock",
  "S": "Scissors"
}
dict_keys = list(rand_dict.keys())
# print(dict_keys)
def rock_paper_scissors(greeting="Welcome to rock-paper-scissors!"):
  print(greeting)
  user_input = input("Enter your choice: (R for Rock; P for Paper; S for Scissors)\n")

  if user_input not in dict_keys:
    rock_paper_scissors(greeting="\nInvalid Input!\n")
  else:
    comp_choice = choice(dict_keys)
    print(f"\nPlayer ({rand_dict[user_input]}) : CPU ({rand_dict[comp_choice]})")
    if comp_choice == user_input:
      rock_paper_scissors(greeting="\nDraw! Play again!")
    elif comp_choice == "P" and user_input == "R":
      print("\nWinner: CPU")
    elif comp_choice == "R" and user_input == "P":
      print("\nWinner: Player")
    elif comp_choice == "R" and user_input == "S":
      print("\nWinner: CPU")
    elif comp_choice == "S" and user_input == "R":
      print("\nWinner: Player")
    elif comp_choice == "P" and user_input == "S":
      print("\nWinner: Player")
    elif comp_choice == "S" and user_input == "P":
      print("\nWinner: CPU")
    



rock_paper_scissors()
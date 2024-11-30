import random
from art import logo, vs
import game_data

# show the logo
print(logo)
celebrities = []
score = 0
game_continue = True


def random_celebrity():
    celebrity = random.choice(game_data.data)
    name = celebrity['name']
    follower_count = celebrity['follower_count']
    description = celebrity['description']
    country = celebrity['country']
    celebrities.append(celebrity)


# pick first two celebrities
for person in range(2):
    random_celebrity()


def increase_score(n):
    n += 1
    print(n)
    return n


# print celebrities
# assign first two ppl as a first_person and second_person
def print_celebrity():
    first_person = celebrities[0]
    second_person = celebrities[1]
    print(
        f"A: {first_person['name']}, {first_person['description']} from {first_person['country']}")
    print(vs)
    print(
        f"B: {second_person['name']}, {second_person['description']} from {second_person['country']}")
    return first_person, second_person


# compare the followers (take two ppl)
# leave the winner into the compare def
# ask user input
# check if the user choice is correct


def update_list():
    first_person, second_person = print_celebrity()
    u_choice = input("Who has more followers? Type 'A' or 'B': ").upper()
    print("\n" * 20)
    print(logo)
    if u_choice == 'A' and (first_person['follower_count'] > second_person['follower_count']):
        celebrities.append(random_celebrity())  # new item added at the 3rd position
        del celebrities[1]  # del defeated person
        del celebrities[2]  # del none
        return True
    elif u_choice == 'B' and (first_person['follower_count'] < second_person['follower_count']):
        random_celebrity()
        del celebrities[0]
        return True
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        return False


# Execute functions
while game_continue:
    game_continue = update_list()
    if game_continue:
        score = increase_score(score)
        print(f"You are right! Current score: {score}")

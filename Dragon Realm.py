import random
import time

def display_intro():
    print('''
    You are in a land full of dragons. In front of you, 
    you see five caves. 
    In one cave, the dragon is friendly and will share his treasure with you. 
    The second dragon is greedy and hungry, and will eat you on sight.
    The third dragon is sleeping on his mound of gold and jewels.
    The fourth dragon has a fiery temper.
    The fifth dragon loves to sing and teach.''')
    print()

def choose_cave():
    while True:
        cave = input('Which cave will you go in? (1 - 5)')
        if cave in ['1', '2', '3', '4', '5']:
            return cave
        else:
            print("You need to choose one of the five caves in front of you. Enter a number between 1 and 5")



def check_cave(chosen_cave):
    print('You approach the cave...')
    time.sleep(2)
    print('It is dark and spooky...')
    time.sleep(2)
    print('A large dragon jumps out in front of you! He opens his jaws and...\n')
    time.sleep(2)


    dragon_response = [
        'Gobbles you down in one bite!',
        'Burns you to a crisp!',
        'Sings a song to you about how sharing is caring',
        'Yawns, turns around, and goes back to sleep',
        "Gives you a lecture on how random.choice() would work much better for this game."
    ]

    cave = random.randint(1, 5)
    if chosen_cave != str(cave):
        print(dragon_response[cave - 1])
        print()
    else:
        print("Gives you his treasure!")
        print()

play_again = 'yes'


while play_again in ['yes', 'YES', 'y', 'Y']:
    display_intro()
    cave_number = choose_cave()
    check_cave(cave_number)

    print('Do you want to play again? (yes to play again, or any other key + Enter to exit)')
    play_again = input()
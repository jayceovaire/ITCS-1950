import random


def computer_roll():
    """Rolls the computer dice, does not return any ascii art"""
    value = random.randint(1, 6)
    return value


def update_dice_on_board(player_dice, computer_dice, d_board):
    """checks all the dice that were rolled and adds them to a dictionary"""
    for value in player_dice:
        d_board[value] += 1
    for value in computer_dice:
        d_board[value] += 1


def roll():
    """simulates rolling a 6 sided die, also picks the ascii art that is printed out with each die that is rolled"""

    dice_faces_art = [
        [" ------- ", "|       |", "|   o   |", "|       |", " ------- "],
        [" ------- ", "|  o    |", "|       |", "|    o  |", " ------- "],
        [" ------- ", "|  o    |", "|   o   |", "|    o  |", " ------- "],
        [" ------- ", "| o   o |", "|       |", "| o   o |", " ------- "],
        [" ------- ", "| o   o |", "|   o   |", "| o   o |", " ------- "],
        [" ------- ", "| o   o |", "| o   o |", "| o   o |", " ------- "],
    ]

    value = random.randint(1, 6)
    dice_faces = [dice_faces_art[value - 1][i] for i in range(5)]
    return value, dice_faces


def roll_cup():
    """rolls a cup of dice and appends their values to a list to be referenced, also prints out ascii art to match
    each die that was rolled"""
    rolled_values = []
    dice_faces = []
    for _ in range(5):
        value, faces = roll()
        rolled_values.append(value)
        dice_faces.append(faces)

    for i in range(5):
        print(" ".join([dice_faces[j][i] for j in range(5)]))
    print("You rolled " + "-".join(str(value) for value in rolled_values))
    p_dice = rolled_values
    return p_dice


def update_lying_status(c_face, c_bet, d_board):
    if d_board.get(c_face, 0) < c_bet:
        return True
    else:
        return False


def computer_turn(c_face, c_bet, c_dice, p_lying):
    """Computer checks how many faces of each die it has then calculates probability of players bet being realistic based
    on the dice it has rolled and the 5 anonymous dice remaining in the players cup. It checks for 0 to 5 matching faces
    and also has some RNG to its turns to make it less predictable to play against. It may play the game very safely, or
    call you out on turn 1"""

    """Dice Count dictionary is used to count the values of dice the computer rolled and referenced in order to find the
    safest bet / second safest bet / faces the  computer should use"""

    dice_counts = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    matching_dice_values_count = 0
    safest_bet = 0
    second_safest_bet = 0
    safest_bet_face = None
    second_safest_bet_face = None

    print('Current bet:', c_bet, 'of a kind, with face', c_face)

    for die in c_dice:
        if die in dice_counts:
            dice_counts[die] += 1

    for face in dice_counts:
        if dice_counts[face] > 1:
            matching_dice_values_count += 1

    for face in dice_counts:
        if dice_counts[face] >= safest_bet:
            second_safest_bet = safest_bet
            second_safest_bet_face = safest_bet_face
            safest_bet = dice_counts[face]
            safest_bet_face = face
        elif dice_counts[face] >= second_safest_bet:
            second_safest_bet = dice_counts[face]
            second_safest_bet_face = face

    # risk levels may be implemented in future computer turn logic
    matching_dice_values_count = len([face for face in dice_counts if dice_counts[face] > 1])
    risk = 6 - matching_dice_values_count

    # uncomment below for debugging purposes
    # print('Number of faces that match =', matching_dice_values_count)
    # print('Risk =', risk)
    # print('Computer dice:', computer_dice)
    # print('Safest bet is', safest_bet, 'of a kind with face', safest_bet_face)
    # print('Second-safest bet is', second_safest_bet, 'of a kind with face', second_safest_bet_face)
    # print('Current bet:', c_bet, 'of a kind, with face', c_face)

    probability_at_least_n_total_dice = {
        0: 1.0,  # 100%
        1: 0.5981224279835395,  # 59%
        2: 0.1607510288065844,  # 16%
        3: 0.03215020597709243,  # 3%
        4: 0.0032150206793006755,  # .3%
        5: 0.0001286010744584546,  # .01%
        6: 0.0000019344216418871176,
        7: 0.000000008609454765960044,
        8: 0.000000000000007138041894978875,
        9: 0.00000000000000007120217913816713,
        10: 0.0000000000000000010134202418027312
    }

    face_count = c_dice.count(c_face)

    def call_check():
        """Checks whether the player is lying when the opponent calls them out"""
        if p_lying:
            print("Davey Jones called you a Liar! You Lose!")
            ask_to_replay()
        else:
            print("Davey Jones wrongly calls you a Liar! You Win!")
            ask_to_replay()

    def announce():

        verbs = [
            "smiles",
            "laughs",
            "smirks",
            "grimaces",
            "frowns",
            "grins",
            "winks",
            "nods",
            "raises his eyebrows",
            "blinks",
            "rolls his eyes",
            "raises an eyebrow",
            "squints",
        ]

        print('Davey Jones', random.choice(verbs), 'and', 'raises the bet to', new_bet, 'of a kind with face', new_face)

    def find_probability():
        """Calculate the probability of the player having at least c_bet dice of c_face"""
        diff = abs(face_count - c_bet)
        probability = probability_at_least_n_total_dice[diff]
        return probability

    # uncomment below for debugging purposes
    # probability_player_bet = find_probability()
    # print(probability_player_bet)
    """Decision making logic for the computer to take its turn, it will check how many faces it has matching of its
    safest bet to make decisions based on the probability of the current bet vs the player's chances
    of having at least n dice rolled out of 10 that are not in the computers hand, I've added a RNG to add some unpredictability
    and fun gambling behavior to the computer's moves"""
    if face_count == 0:
        probability_player_bet = find_probability()
        if c_face == 0 or c_bet == 0:
            fun_choice = random.randint(1, 5)
            if fun_choice == 1:
                new_bet = 1
                new_face = new_face = max(dice_counts, key=dice_counts.get)
                c_bet = new_bet
                c_face = new_face
                announce()
                return c_face, c_bet
            elif fun_choice == 2:
                new_bet = second_safest_bet
                new_face = second_safest_bet_face
                c_bet = new_bet
                c_face = new_face
                announce()
                return c_face, c_bet
            elif fun_choice == 3:
                new_bet = safest_bet
                new_face = safest_bet_face
                c_bet = new_bet
                c_face = new_face
                announce()
                return c_face, c_bet
            elif fun_choice == 4:
                new_bet = safest_bet
                new_face = second_safest_bet_face
                c_bet = new_bet
                c_face = new_face
                announce()
                return c_face, c_bet
            elif fun_choice == 5:
                new_bet = second_safest_bet
                new_face = safest_bet_face
                c_bet = new_bet
                c_face = new_face
                announce()
                return c_face, c_bet
        if probability_player_bet > 0.50:
            new_bet = c_bet + 1
            new_face = max(dice_counts, key=dice_counts.get)
            c_bet = new_bet
            c_face = new_face
            announce()
            return c_face, c_bet

        if 0.16 < probability_player_bet < 0.50:
            fun_choice = random.randint(1, 2)
            if fun_choice == 1:
                new_bet = c_bet + 1
                new_face = max(dice_counts, key=dice_counts.get)
                c_bet = new_bet
                c_face = new_face
                announce()
                return c_face, c_bet

            else:
                call_check()

        if probability_player_bet < 0.04:
            call_check()

    elif face_count == 1:
        probability_player_bet = find_probability()
        if probability_player_bet > 0.50:
            fun_choice = random.randint(1, 6)
            if fun_choice < 3:
                new_bet = second_safest_bet + 1
                new_face = second_safest_bet_face
                c_bet = new_bet
                c_face = new_face
                announce()
                return c_face, c_bet

            elif fun_choice == 3:
                new_bet = c_bet + 1
                new_face = safest_bet_face
                c_bet = new_bet
                c_face = new_face
                announce()
                return c_face, c_bet

            elif fun_choice == 4 or fun_choice == 5:
                new_bet = c_bet + 2
                new_face = safest_bet_face
                announce()
                c_bet = new_bet
                c_face = new_face
                return c_face, c_bet
            elif fun_choice == 6:
                new_bet = c_bet + 3
                new_face = max(dice_counts, key=dice_counts.get)
                c_bet = new_bet
                c_face = new_face
                announce()
                return c_face, c_bet

        elif probability_player_bet > .04 and probability_player_bet < .50:
            fun_choice = random.randint(1, 4)
            if fun_choice <= 2:
                new_bet = c_bet + 1
                new_face = safest_bet_face
                c_bet = new_bet
                c_face = new_face
                announce()
                return c_face, c_bet
            elif fun_choice == 3:
                new_bet = c_bet + 1
                new_face = second_safest_bet_face
                c_bet = new_bet
                c_face = new_face
                announce()
                return c_face, c_bet
            else:
                call_check()
        elif probability_player_bet < .04:
            call_check()

    elif face_count == 2:
        probability_player_bet = find_probability()
        if probability_player_bet > 0.50:
            fun_choice = random.randint(1, 6)
            if fun_choice <= 2:
                new_bet = c_bet + 1
                new_face = c_face
                c_bet = new_bet
                c_face = new_face
                announce()
                return c_face, c_bet
            elif fun_choice == 3:
                new_bet = c_bet + 2
                new_face = safest_bet_face
                c_bet = new_bet
                c_face = safest_bet_face
                announce()
                return c_face, c_bet
            elif fun_choice == 4:
                new_bet = c_bet + 3
                new_face = safest_bet_face
                c_bet = new_bet
                c_face = new_face
                announce()
                return c_face, c_bet

            elif fun_choice == 5:
                new_bet = c_bet + 2
                new_face = second_safest_bet_face
                c_bet = new_bet
                c_face = new_face
                announce()
                return c_face, c_bet

            elif fun_choice == 6:
                call_check()

        if 0.16 < probability_player_bet < 0.50:
            fun_choice = random.randint(1, 4)
            if fun_choice <= 2:
                new_bet = c_bet + 1
                new_face = safest_bet_face
                announce()
                return c_face, c_bet

            elif fun_choice == 3:
                if second_safest_bet_face >= (c_face + 1):
                    new_bet = c_bet + 1
                    new_face = c_face + 1
                    c_bet = new_bet
                    c_face = new_face
                    announce()
                    return c_face, c_bet

                elif safest_bet_face >= (c_face + 2):
                    new_bet = c_bet + 1
                    new_face = c_face + 1
                    c_bet = new_bet
                    c_face = new_face
                    announce()
                    return c_face, c_bet

                elif safest_bet_face > c_face:
                    new_bet = c_bet
                    new_face = safest_bet_face
                    c_bet = new_bet
                    c_face = new_face
                    announce()
                    return c_face, c_bet

                else:
                    new_bet = c_bet + 1
                    new_face = c_face
                    c_bet = new_bet
                    c_face = new_face
                    announce()
                    return c_face, c_bet

            elif fun_choice == 4:
                call_check()

        elif probability_player_bet < .04:
            call_check()

    elif face_count == 3:
        probability_player_bet = find_probability()
        if probability_player_bet > 0.50:
            fun_choice = random.randint(1, 6)
            if fun_choice <= 2:
                new_bet = c_bet + 1
                new_face = c_face
                c_bet = new_bet
                c_face = new_face
                announce()
                return c_face, c_bet
            elif fun_choice == 3:
                new_bet = c_bet + 2
                new_face = c_face
                c_bet = new_bet
                c_face = new_face
                announce()
                return c_face, c_bet
            elif fun_choice == 4:
                new_bet = c_bet + 3
                new_face = c_face
                c_bet = new_bet
                c_face = new_face
                announce()
                return c_face, c_bet
            elif fun_choice == 5:
                if second_safest_bet_face > c_face:
                    new_bet = c_bet
                    new_face = second_safest_bet_face
                    c_bet = new_bet
                    c_face = new_face
                    announce()
                    return c_face, c_bet
                else:
                    new_bet = c_bet + 1
                    new_face = second_safest_bet_face
                    c_bet = new_bet
                    c_face = new_face
                    announce()
                    return c_face, c_bet
            elif fun_choice == 6:
                call_check()

        if 0.16 < probability_player_bet < 0.50:
            fun_choice = random.randint(1, 4)
            if fun_choice == 1:
                new_bet = c_bet + 1
                new_face = c_face
                c_bet = new_bet
                c_face = new_face
                announce()
                return c_face, c_bet
            elif fun_choice == 2:
                new_bet = c_bet + 2
                new_face = c_face
                c_bet = new_bet
                c_face = new_face
                announce()
                return c_face, c_bet
            elif fun_choice == 3:
                new_bet = c_bet + 3
                new_face = c_face
                c_bet = new_bet
                c_face = new_face
                announce()
                return c_face, c_bet
            elif fun_choice == 4:
                if second_safest_bet_face > c_face:
                    new_bet = c_bet
                    new_face = second_safest_bet_face
                    c_bet = new_bet
                    c_face = new_face
                    announce()
                    return c_face, c_bet
                else:
                    new_bet = c_bet + 1
                    new_face = second_safest_bet_face
                    c_bet = new_bet
                    c_face = new_face
                    announce()
                    return c_face, c_bet
            elif fun_choice == 5:
                call_check()

        if probability_player_bet < 0.04:
            fun_choice = random.randint(1, 100)
            if fun_choice <= 5:
                new_bet = 10
                new_face = safest_bet_face
                c_bet = new_bet
                c_face = new_face
                announce()
                return c_face, c_bet
            else:
                call_check()

    elif face_count == 4:
        probability_player_bet = find_probability()
        if probability_player_bet > 0.50:
            fun_choice = random.randint(1, 10)
            if fun_choice != 1:
                new_bet = c_bet + 1
                new_face = c_face
                c_bet = new_bet
                c_face = new_face
                announce()
                return c_face, c_bet
            else:
                call_check()

        if 0.16 < probability_player_bet < 0.50:
            fun_choice = random.randint(1, 4)
            if fun_choice == 1:
                new_bet = c_bet + 1
                new_face = c_face
                c_bet = new_bet
                c_face = new_face
                announce()
                return c_face, c_bet
            elif fun_choice == 2:
                new_bet = c_bet + 2
                new_face = c_face
                c_bet = new_bet
                c_face = new_face
                announce()
                return c_face, c_bet
            elif fun_choice == 3:
                if second_safest_bet_face > c_face:
                    new_bet = c_bet
                    new_face = second_safest_bet_face
                    c_bet = new_bet
                    c_face = new_face
                    announce()
                    return c_face, c_bet
                else:
                    new_bet = c_bet + 1
                    new_face = second_safest_bet_face
                    c_bet = new_bet
                    c_face = new_face
                    announce()
                    return c_face, c_bet
            elif fun_choice == 4:
                call_check()

        if probability_player_bet < 0.04:
            fun_choice = random.randint(1, 4)
            if fun_choice != 1:
                call_check()
            else:
                new_bet = c_bet + 1
                new_face = c_face
                c_bet = new_bet
                c_face = new_face
                announce()
                return c_face, c_bet

    elif face_count == 5:
        probability_player_bet = find_probability()
        if probability_player_bet > 0.50:
            fun_choice = random.randint(1, 6)
            if fun_choice < 5:
                new_bet = c_bet + 1
                new_face = c_face
                c_bet = new_bet
                c_face = new_face
                announce()
                return c_face, c_bet

            elif fun_choice >= 5:
                new_bet = c_bet + 2
                new_face = c_face
                c_bet = new_bet
                c_face = new_face
                announce()
                return c_face, c_bet

        if 0.16 < probability_player_bet < 0.50:
            fun_choice = random.randint(1, 6)
            if fun_choice != 6:
                call_check()
            else:
                new_bet = c_bet + 1
                new_face = c_face
                c_bet = new_bet
                c_face = new_face
                announce()
                return c_face, c_bet

        if probability_player_bet < 0.04:
            fun_choice = random.randint(1, 100)
            if fun_choice <= 5 and c_face < safest_bet_face:
                new_bet = 10
                new_face = safest_bet_face
                c_bet = new_bet
                c_face = new_face
                announce()
                return c_face, c_bet

            elif fun_choice <= 5 and c_face < second_safest_bet_face:
                new_bet = 10
                new_face = safest_bet_face
                c_bet = new_bet
                c_face = new_face
                announce()
                return c_face, c_bet
            else:
                call_check()

    print('Current bet:', c_bet, 'of a kind, with face', c_face)


def player_turn(c_face, c_bet, o_lying):
    """logic and menu for player's turn, they can choose to make a bid, call the computer out on lying, or admit defeat"""
    player_menu = ['Make Bid', 'Call', 'Fold']
    for num, option in enumerate(player_menu, 1):
        print(num, ':', option)
    choice = input('Enter your choice: ')
    while choice not in ['1', '2', '3']:
        choice = input('Enter your choice: ')
    if choice == '1':
        c_face, c_bet = make_bid(c_face, c_bet)
    elif choice == '2':
        print("You call Davey Jones a Liar!")
        if o_lying:
            print("YOU WIN!")
            ask_to_replay()
        else:
            print("Davey Jones wasn't lying! YOU LOSE!")
            ask_to_replay()
    elif choice == '3':
        print("You have admitted defeat!")
        ask_to_replay()
    else:
        print("Invalid option. What would you like to do?")

    return c_face, c_bet


def change_face(c_face):
    """Allows player to change the face of the dice bid at the start of the game"""
    local_possible_faces = [1, 2, 3, 4, 5, 6]
    chosen_face = c_face
    while chosen_face not in local_possible_faces:
        try:
            print("What would you like to change the face to?")
            print("It must be a number between", (c_face + 1), "and 6")
            chosen_face = int(input())

            c_face = chosen_face
            print("Face changed to:", c_face)
            return c_face

        except ValueError:
            print("Invalid input. Please enter a valid number.")


def change_bet(c_bet):
    """Allows the player to change the number of dice in their dice bid at the start of the game"""
    local_possible_bets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    chosen_bet = c_bet
    while chosen_bet not in local_possible_bets:
        try:
            print("What would you like to change the bet to?")
            print("It must be a number between", (c_bet + 1), "and 10")
            chosen_bet = int(input())
            if chosen_bet < c_bet or chosen_bet > 10:
                print("Invalid choice. Please choose a number between", (c_bet + 1), "and 10.")

            c_bet = chosen_bet
            print("Current bet changed to:", c_bet)
            return c_bet

        except ValueError:
            print("Invalid input. Please enter a valid number.")


def make_bid(c_face, c_bet):
    """Menu that allows player to choose what type of bet they would like to make"""
    try:
        change_choice = 0
        while change_choice not in ['1', '2', '3']:
            print("1 : Change Face and Increase Bet")
            print("2 : Change Bet of Current Face")
            print("3 : Change Current Face and Keep Bet")

            change_choice = input('Enter your choice: ')

            if change_choice == '1':
                chosen_face = 0
                while chosen_face < 1 or chosen_face > 6:
                    try:
                        print("What would you like to change the face to?")
                        chosen_face = int(input())

                    except:
                        print()
                    if chosen_face < 1 or chosen_face > 6:
                        print("Invalid choice. Please choose a number between 1 and 6.")

                chosen_bet = c_bet
                while chosen_bet < c_bet + 1 or chosen_bet > 10:
                    try:
                        print("What would you like to change the bet to?")
                        print("It must be a number between", (c_bet + 1), "and 10")
                        bet_choice = input()
                        chosen_bet = int(bet_choice)
                    except:
                        print()
                    if chosen_bet < c_bet + 1 or chosen_bet > 10:
                        print("Invalid choice. Please choose a number between", (c_bet + 1), "and 10.")

                c_face = chosen_face
                c_bet = chosen_bet
                print("Face changed to:", c_face)
                print("Current bet changed to:", c_bet)
                return c_face, c_bet

            elif change_choice == '2':
                chosen_bet = c_bet
                while chosen_bet < c_bet + 1 or chosen_bet > 10:
                    try:
                        print("What would you like to change the bet to?")
                        print("It must be a number between", (c_bet + 1), "and 10")
                        bet_choice = input()
                        chosen_bet = int(bet_choice)
                    except:
                        print()
                    if chosen_bet < c_bet + 1 or chosen_bet > 10:
                        print("Invalid choice. Please choose a number between", (c_bet + 1), "and 10.")

                c_bet = chosen_bet
                print("Current bet changed to:", c_bet)
                return c_face, c_bet

            elif change_choice == '3':

                chosen_face = c_face
                if c_face == 6:
                    print('You cannot raise the face any higher')
                    return make_bid(c_face, c_bet)

                while chosen_face < c_face + 1 or chosen_face > 6:
                    try:
                        print("What would you like to change the face to?")
                        print("It must be a number between", (c_face + 1), "and 6")
                        chosen_face = int(input())
                    except:
                        print()
                    if chosen_face < c_face + 1 or chosen_face > 6:
                        print("Invalid choice. Please choose a number between", (c_bet + 1), "and 6.")

                c_face = chosen_face
                print("Face changed to:", c_face)
                return c_face, c_bet

            else:
                print("Invalid option. Please enter a valid choice.")

    except ValueError:
        print("Invalid input. Please enter a valid number.")


def ask_to_replay():
    """Asks player to replay the game, if yes it will reset data and send them back to main menu, if no the program will exit"""
    play_again = ''
    while play_again not in ['1', '2']:
        play_again = input("Do you wish to play again?\n1: Yes\n2: No\n")
        if play_again == '2' or play_again in ['no', 'n', 'N', 'No']:
            exit()
        elif play_again == '1' or play_again in ['y', 'yes', 'Yes', 'Y']:
            main()


def display_main_menu():
    """Game main menu, lets player choose to start a new game, learn the rules, or exit"""

    how_to = """
        The game is played over multiple rounds. To begin each round, all players roll their dice simultaneously. Each player looks at their own dice after they roll,
        keeping them hidden from the other players. The first player then states a bid consisting of a face ("1's", "5's", etc.) and a quantity. The quantity represents the player's
        guess as to how many of each face have been rolled by all the players at the table, including themselves. For example, a player might bid "five 2's."
        Each subsequent player can either then make a higher bid of the same face (e.g., "six 2's"), they can make a bid for the same number of dice rolled
        but use a higher face,(e.g. "five 3's"), or they can challenge the previous bid.
        If the player challenges the previous bid, all players reveal their dice. If the bid is matched or exceeded, the bidder wins. Otherwise the challenger wins."""

    main_menu = ['Play Game', 'How to Play', 'Exit']

    for num, option in enumerate(main_menu, 1):
        print(num, ':', option)
    choice = input('Enter your choice: ')
    if choice == '1':
        print("Let's Play!")
        return True
    elif choice == '2':
        print(how_to)
        return display_main_menu()
    elif choice == '3':
        print('Goodbye!')
        exit()
    else:
        print("Invalid option.")
        return display_main_menu()


def main():
    """Main function to start program"""

    graphic = """
     __        __                     __               _______   __                     
    /  |      /  |                   /  |             /       \ /  |                    
    $$ |      $$/   ______    ______ $$/_______       $$$$$$$  |$$/   _______   ______  
    $$ |      /  | /      \  /      \$//       |      $$ |  $$ |/  | /       | /      \ 
    $$ |      $$ | $$$$$$  |/$$$$$$  |/$$$$$$$/       $$ |  $$ |$$ |/$$$$$$$/ /$$$$$$  |
    $$ |      $$ | /    $$ |$$ |  $$/ $$      \       $$ |  $$ |$$ |$$ |      $$    $$ |
    $$ |_____ $$ |/$$$$$$$ |$$ |       $$$$$$  |      $$ |__$$ |$$ |$$ \_____ $$$$$$$$/ 
    $$       |$$ |$$    $$ |$$ |      /     $$/       $$    $$/ $$ |$$       |$$       |
    $$$$$$$$/ $$/  $$$$$$$/ $$/       $$$$$$$/        $$$$$$$/  $$/  $$$$$$$/  $$$$$$$
    
    """

    dice_on_board = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    c_face = 0
    c_bet = 0
    print(graphic)
    game_active = display_main_menu()
    turn = 'turn_one'
    p_dice = roll_cup()
    computer_dice = [computer_roll() for _ in range(5)]
    update_dice_on_board(p_dice, computer_dice, dice_on_board)
    opponent_is_lying = False
    player_is_lying = False
    while game_active:
        if turn == 'turn_one':
            first = random.randint(1, 2)
            if first == 1:
                c_face = change_face(c_face)
                c_bet = change_bet(c_bet)
                player_is_lying = update_lying_status(c_face, c_bet, dice_on_board)
                turn = 'computer'
                continue

            if first == 2:
                c_face, c_bet = computer_turn(c_face, c_bet, computer_dice, player_is_lying)
                opponent_is_lying = update_lying_status(c_face, c_bet, dice_on_board)
                turn = 'player'
                continue

        if turn == 'player':
            c_face, c_bet = player_turn(c_face, c_bet, opponent_is_lying)
            player_is_lying = update_lying_status(c_face, c_bet, dice_on_board)
            turn = 'computer'
            continue

        if turn == 'computer':
            c_face, c_bet = computer_turn(c_face, c_bet, computer_dice, player_is_lying)
            opponent_is_lying = update_lying_status(c_face, c_bet, dice_on_board)
            turn = 'player'
            # uncomment below for debugging
            #print('computer is lying =', opponent_is_lying)
            continue


main()

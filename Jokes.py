
def jokes():

    print("What do you get when you cross a snowman with a vampire?")
    response = input()
    if response in ["Frostbite", "frostbite"]:
        print("...You've heard that one before haven't you")
    else:
        print("Frostbite!")

    print("What do dentists call an astronaut's cavity?")
    response_two = input()
    if response_two in ['A black hole', 'black hole', 'a black hole']:
        print("...can you read minds? Have you done this before?")
    else:
        print("A black hole!")

    print('Knock Knock')
    response_three = input()
    if response_three == "MOO":
        print("HOW DID YOU KNOW THAT?!")
        print("THIS ISN'T FAIR I QUIT. GOODBYE!")
        exit()
    else:
        while response_three not in ["Who's there?", "Who's there", "who's there?", "who's there"]:
            print("I'm waiting...(hint: (who's there)")
            response_three = input()

    print("interrupting cow.")
    response_four = input()
    print(response_four, end='')
    print("-MOO!")


jokes()

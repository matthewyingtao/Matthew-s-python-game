# importing allows us to use random numbers and exit commands
import random
import sys

# Defining Variables
emoji_assets = ["🗿", "🏜️", "💦", "🌴", "🐧", "💰", "🐕", "🦂", "👽", "🦀", "🐠", "🔥", "🦜", "📚", "🍏", "🏠", "🏎️",
                "🍔", "🍹", "🛸", "🐾", "🧘", "⛑️"]
map = ["e", "s", "o", "", "t", "o", "", "t", "h", "e", "", "b", "o", "n", "e", "!", "", "", "", "", "", "", "", "", ""]
penguin_facts = ["Penguins are birds but cannot fly.",
                 "Penguins are often black and white, which lets the camouflage into the water and ice",
                 "Penguins spend half their life on land and the other half in water",
                 "Penguins wings function as flippers", "Penguins waddle their feet when they walk",
                 "Penguins slide on their bellies across the snow",
                 "Almost all penguins live in the southern hemisphere", "Most penguins actually live in warmer seas",
                 "Penguins eat krill (which look similar to shrimp)",
                 "Penguins are fast swimmers, and can outswim a lot of their predators",
                 "Penguins can swim at speeds of over 20 miles per hour"]
endings = ["no", "no", "no", "no", "no", "no", "no", "no", "no", "no"]
play = 1
replay = 0
finished_endings = [-1, -1, -1, -1]
expected_inputs = [1, 2, 3, 4]
questions = ["first question: what category are dogs? \n-1- carnivore \n-2- omnivore \n-3- herbivore\n-4- trucknivore",
             "second question: how many paw pads do dogs have? \n-1- \"4\" \n-2- \"16\" \n-3- \"28\" \n-4- \"10\"",
             "third question: how long does a dog sleep in a day? \n-1- 8-10 hours \n-2- 10-12 hours \n-3- 12-14 hours \n-4- 14-16 hours",
             "fourth question: how many muscles do dogs have for moving their ears? \n-1- \"4\" \n-2- \"7\" \n-3- \"24\" \n-4- \"18\"",
             "last question: how many dogs are there in the world? \n-1- 300 million \n-2- 900 million \n-3- 1 billion \n-4- 10 million",
             "first question: what meat has the most protein? \n-1- chicken \n-2- beef \n-3- lamb \n-4- pig",
             "second question: how much sugar is in a can of coke? \n-1- 13 grams\n-2- 25 grams \n-3- 39 grams \n-4- 42 grams",
             "third question: what color is an unripe lemon? \n-1- yellow \n-2- green \n-3- orange \n-4- grey",
             "fourth question: what fruit contains the most sugar? (all weighing the same) \n-1- bananas \n-2- cherries \n-3- mangos \n-4- grapes",
             "last question: how long can a human live without water? \n-1- 3 days \n-2- 1 week \n-3- 5 days \n-4- 1 month"]
answers = [2, 3, 3, 4, 2, 1, 3, 2, 4, 1]
color_string = ""


def game():
    global emoji_assets
    global map
    global penguin_facts
    global color_string
    global consecutive_invalid
    global map_making
    global event
    global score
    global penguin_position
    global event1_location
    global event2_location
    global area
    global crab_location
    global parrot_location
    global book_location
    global apple_location
    global fish_location
    global fire_stage
    global fish_collected
    global answer
    global lives
    global endings
    global play
    global replay
    global question_number
    global questions
    global answers
    global answered
    penguin_position = 12
    event = 0
    map_making = 0
    consecutive_invalid = 0
    score = 0
    event = 0
    direction = 0
    book_location = -1
    answer = 0
    lives = 3
    answered = 0
    # disallows area to be areas with all completed endings
    if endings[0 - 2] == "yes":
        finished_endings[0] = 0
        print("you have finished all endings a")
    elif endings[3 - 5] == "yes":
        finished_endings[1] = 1
        print("you have finished all endings b")
    elif endings[6 - 7] == "yes":
        finished_endings[2] = 2
        print("you have finished all endings d")
    elif endings[8 - 9] == "yes":
        finished_endings[3] = 3
        print("you have finished all endings e")
    # checks to see if all endings have been completed
    if "no" not in endings:
        end = 0
        print("Congratulations! You have completed all endings! \n"
              "I hope you enjoyed my game :) \n"
              "Thanks for playing!")
        while True:
            try:
                while end not in (1, 2):
                    end = input("do you wish to leave the game? \n"
                                "-1- yes \n"
                                "-2- no \n")
                    if end in ("", "1"):
                        play = 0
                        event = 1
                        sys.exit()
                    elif end == "2":
                        break
            except:
                print("please enter a valid input")
    # Random number to choose map
    area = random.randint(0, 3)
    while area in (finished_endings):
        area = random.randint(0, 3)
        if area not in (finished_endings):
            break
    if area == 0:
        event_emoji = 5
    elif area == 1:
        event_emoji = 7
    elif area == 2:
        event_emoji = 9
        fish_collected = 0
        apple_location = -1
    elif area == 3:
        event_emoji = 11
        fire_stage = 0

    if area == 0:
        question_number = 0
    elif area == 1:
        question_number = 5

    #   ~FUNCTIONS~
    # manages invalid inputs
    def invalid_input():
        global consecutive_invalid
        consecutive_invalid += 1
        if consecutive_invalid < 3:
            print("please enter a valid input")
        else:
            exit = input("do you want to exit the game? \n"
                         "-1- yes \n"
                         "-2- no \n")
            if exit in ("1", ""):
                play = 0
                sys.exit()
            else:
                consecutive_invalid = 0
                exit = ""

    # asks player for color
    def wrong_answer():
        global lives
        global play
        global event
        lives -= 1
        if lives < 1:
            if area == 0:
                print("the dog starts to growl at {}, and {} runs away \n".format(color_string, color_string) +
                      "    ~THE END~    ")
            elif area == 1:
                print("He leaves and {} starve/thirst in the desert \n".format(color_string) +
                      "    ~THE END~    ")
            play = 0
            event = 1
            sys.exit()
        else:
            print("Wrong answer! You have {} lives remaining.".format(lives))

    # asks the user for their color, which will be used in place of their name.
    def ask_color():
        global color_string
        while color_string == "":
            try:
                color = int(input("-1- Blue       -2- Red \n"
                                  "-3- Yellow    -4- Green \n"))
                if color == 1:
                    color_string = "Blue"
                elif color == 2:
                    color_string = "Red"
                elif color == 3:
                    color_string = "Yellow"
                elif color == 4:
                    color_string = "Green"
                else:
                    invalid_input()
            except:
                invalid_input()
        print("That's a unique color for a penguin! I'll call you {} from now on.".format(color_string))

    # Checks for area boundaries
    def move_check():
        if position[1] <= area_boundry[2]:
            print("there is a wall there")
            position[1] += 1
        elif position[1] >= area_boundry[3]:
            print("there is a wall there")
            position[1] -= 1
        elif position[0] <= area_boundry[0]:
            print("there is a wall there")
            position[0] += 1
        elif position[0] >= area_boundry[1]:
            print("there is a wall there")
            position[0] -= 1
        else:
            move_map()
            event_check()
            show_map()

    # Displays the current map
    def show_map():
        if event == 0:
            print("{} {} {} {} {} \n"
                  "{} {} {} {} {} \n"
                  "{} {} {} {} {} \n"
                  "{} {} {} {} {} \n"
                  "{} {} {} {} {}".format(map[0], map[1], map[2], map[3], map[4], map[5], map[6], map[7], map[8],
                                          map[9], map[10], map[11], map[12], map[13], map[14], map[15], map[16],
                                          map[17], map[18], map[19], map[20], map[21], map[22], map[23], map[24]))

    # replaces the tiles in the map into the area tiles
    def make_map():
        global map_making
        global map
        while map_making < 25:
            map[map_making] = emoji_assets[area]
            map_making += 1
        map[12] = emoji_assets[4]

    # moves the penguin on the map
    def move_map():
        global penguin_position
        if direction == 1:
            map[penguin_position - 5] = emoji_assets[4]
            map[penguin_position] = emoji_assets[area]
            penguin_position -= 5
        elif direction == 2:
            map[penguin_position + 5] = emoji_assets[4]
            map[penguin_position] = emoji_assets[area]
            penguin_position += 5
        elif direction == 3:
            map[penguin_position + 1] = emoji_assets[4]
            map[penguin_position] = emoji_assets[area]
            penguin_position += 1
        elif direction == 4:
            map[penguin_position - 1] = emoji_assets[4]
            map[penguin_position] = emoji_assets[area]
            penguin_position -= 1
        if area == 3:
            global fire_stage
            if fire_stage == 0:
                if penguin_position > 9:
                    map[5] = emoji_assets[event_emoji]
                    map[6] = emoji_assets[event_emoji]
                    map[7] = emoji_assets[event_emoji]
                    map[8] = emoji_assets[event_emoji]
                    map[9] = emoji_assets[event_emoji]
                    fire_stage += 1
            elif fire_stage == 1:
                if penguin_position > 14:
                    map[10] = emoji_assets[event_emoji]
                    map[11] = emoji_assets[event_emoji]
                    map[12] = emoji_assets[event_emoji]
                    map[13] = emoji_assets[event_emoji]
                    map[14] = emoji_assets[event_emoji]
                    fire_stage += 1
            elif fire_stage == 2:
                if penguin_position > 19:
                    map[15] = emoji_assets[event_emoji]
                    map[16] = emoji_assets[event_emoji]
                    map[17] = emoji_assets[event_emoji]
                    map[18] = emoji_assets[event_emoji]
                    map[19] = emoji_assets[event_emoji]
                    fire_stage += 1

    # places the events on the map
    def make_events():
        global book_location
        if area in {0, 1}:
            global event1_location
            global event2_location
            event1_location = random.randint(0, 24)
            while event1_location in {penguin_position}:
                event1_location = random.randint(0, 24)
                if event1_location not in {penguin_position}:
                    break
            event2_location = random.randint(0, 24)
            while event2_location in {penguin_position, event1_location}:
                event2_location = random.randint(0, 24)
                if event2_location not in {penguin_position, event1_location}:
                    break
            book_location = random.randint(0, 24)
            while book_location in {penguin_position, event1_location, event2_location}:
                book_location = random.randint(0, 24)
                if book_location not in {penguin_position, event1_location, event2_location}:
                    break
            map[event1_location] = emoji_assets[event_emoji]
            map[event2_location] = emoji_assets[event_emoji + 1]
            map[book_location] = emoji_assets[13]
        elif area == 2:
            global fish_location
            global crab_location
            fish_location = [0, 0, 0]
            fish_location[0] = random.randint(0, 24)
            while fish_location[0] in {penguin_position}:
                fish_location[0] = random.randint(0, 24)
                if fish_location[0] not in {penguin_position}:
                    break
            fish_location[1] = random.randint(0, 24)
            while fish_location[1] in {penguin_position, fish_location[0]}:
                fish_location[1] = random.randint(0, 24)
                if fish_location[1] not in {penguin_position, fish_location[0]}:
                    break
            fish_location[2] = random.randint(0, 24)
            while fish_location[2] in {penguin_position, fish_location[0], fish_location[1]}:
                fish_location[2] = random.randint(0, 24)
                if fish_location[2] not in {penguin_position, fish_location[0], fish_location[1]}:
                    break
            crab_location = random.randint(0, 24)
            while crab_location in {penguin_position, fish_location[0], fish_location[1], fish_location[2]}:
                crab_location = random.randint(0, 24)
                if crab_location not in {penguin_position, fish_location[0], fish_location[1], fish_location[2]}:
                    break
            book_location = random.randint(0, 24)
            while book_location in {penguin_position, fish_location[0], fish_location[1], fish_location[2],
                                    crab_location}:
                book_location = random.randint(0, 24)
                if book_location not in {penguin_position, fish_location[0], fish_location[1], fish_location[2],
                                         crab_location}:
                    break
            map[crab_location] = emoji_assets[event_emoji]
            map[fish_location[0]] = emoji_assets[event_emoji + 1]
            map[fish_location[1]] = emoji_assets[event_emoji + 1]
            map[fish_location[2]] = emoji_assets[event_emoji + 1]
            map[book_location] = emoji_assets[13]
        elif area == 3:
            global parrot_location
            parrot_location = random.randint(10, 19)
            while parrot_location in {penguin_position}:
                parrot_location = random.randint(10, 19)
                if parrot_location not in {penguin_position}:
                    break
            map[parrot_location] = emoji_assets[event_emoji + 1]
            map[0] = emoji_assets[event_emoji]
            map[1] = emoji_assets[event_emoji]
            map[2] = emoji_assets[event_emoji]
            map[3] = emoji_assets[event_emoji]
            map[4] = emoji_assets[event_emoji]

    # Does the quizzes
    def quiz():
        global score
        global answer
        global question_number
        global answered
        answer = 0
        while answered != 5:
            while answer not in (expected_inputs):
                try:
                    answer = int(input("\n" + questions[question_number] + "\n"))
                    if answer not in (expected_inputs):
                        invalid_input()
                except:
                    invalid_input()
            if answer == (answers[question_number]):
                print("Correct!")
                score += 1
            else:
                wrong_answer()
            question_number += 1
            answer = 0
            answered += 1

    # Checks if the penguin is occupying an event space
    def event_check():
        global event
        global score
        global lives
        global answer
        global fish_collected
        global crab_location
        global apple_location
        global play
        global color_string
        event_choice = 0
        if area == 0:
            if penguin_position == event1_location:
                event = 1
                while event_choice not in (1, 2):
                    try:
                        event_choice = int(input("{} has found big money! Do you want to: \n".format(color_string) +
                                                 "-1- Take it for yourself \n"
                                                 "-2- Donate it to charity \n"))
                        if event_choice == 1:
                            print(color_string + " goes home and buys themself a very nice house and a car \n" +
                                  emoji_assets[4] + emoji_assets[15] + emoji_assets[16])
                            print("    ~THE END~    ")
                            endings[0] = "yes"
                        elif event_choice == 2:
                            print(
                                color_string + " goes home and donates the money towards starving Antarctic penguins \n" +
                                emoji_assets[4] * 3)
                            print("    ~THE END~    ")
                            endings[1] = "yes"
                        else:
                            invalid_input()
                    except:
                        invalid_input()
            elif penguin_position == event2_location:
                event = 1
                print("The golden dog greets {} \n".format(color_string) +
                      "\"Hello fellow animal! I assume you want to leave this dungeon, I can help you, if you answer at least 3 of my 5 dog questions correctly\"")
                quiz()
                print("{} scored {} out of 5!".format(color_string, score))
                print("'alright, as promised, I'll get you out of this dungeon, hop onto my back!' \n"
                      "*{} hops onto the dog, gripping his fur as tight as your flippers will allow* \n".format(
                    color_string) +
                      "*The golden dog bolts {} out of the dungeon safely*".format(color_string))
                print("{} live a fulfilling life outside of the dungeon \n".format(color_string) +
                      "    ~THE END~    ")
                endings[2] = "yes"
        elif area == 1:
            if penguin_position == event1_location:
                event = 1
                print("The scorpion croaks to {} \n".format(color_string) +
                      "\"Brttt brtt me give sustenance, if you answer 3 of my 5 food and drink questions correctly\"")
                quiz()
                print("{} scored {} out of 5!".format(color_string, score))
                print("*The scorpion silently crawls into his burrow and brings out a burger and a drink* \n"
                      "'Brtt Brtt'" + emoji_assets[event_emoji] + emoji_assets[17] + emoji_assets[18])
                print("He gives {} the refreshments and {} walk back home to Antarctica".format(color_string,
                                                                                                color_string) +
                      emoji_assets[4] + emoji_assets[20] + "\n"
                                                           "    ~THE END~    ")
                endings[5] = "yes"
            elif penguin_position == event2_location:
                event = 1
                while event_choice not in (1, 2):
                    try:
                        event_choice = int(
                            input("{} has found Bob le Alien francais! Tu vouloir: \n".format(color_string) +
                                  "-1- Ask to board his cool UFO \n"
                                  "-2- Escort him to Area 51 \n"))
                        if event_choice == 1:
                            print(color_string + " and Bob have a very fun time in his UFO with the boys \n"
                                  + emoji_assets[4] + emoji_assets[17] + emoji_assets[18] + "     " + emoji_assets[8] +
                                  emoji_assets[18] + emoji_assets[17] + "\n" +
                                  color_string + " and the boys -------->", emoji_assets[19])
                            print("    ~THE END~    ")
                            endings[4] = "yes"
                        elif event_choice == 2:
                            print("The government gives {} a billion dollars for saving le alien \n".format(
                                color_string) + emoji_assets[4] + (3 * emoji_assets[5]) + "\n"
                                  + emoji_assets[8] + emoji_assets[2])
                            print("    ~THE END~    ")
                            endings[3] = "yes"
                        else:
                            invalid_input()
                    except:
                        invalid_input()
        elif area == 2:
            if penguin_position in {fish_location[0], fish_location[1], fish_location[2]}:
                print("{} has collected a fish".format(color_string))
                fish_collected += 1
                if fish_collected == 3:
                    event = 1
                    print("{} swims home and feed your family \n".format(color_string) +
                          emoji_assets[4] + emoji_assets[15] + (3 * emoji_assets[4]) + "\n"
                                                                                       "    ~THE END~    ")
                    endings[7] = "yes"
            if penguin_position == crab_location:
                print("'I am the Crab of Wisdom!' \n"
                      "'To prove it, I will tell you three facts about your kind'")
                fact1 = random.randint(0, 11)
                fact2 = random.randint(0, 11)
                while fact2 == fact1:
                    fact2 = random.randint(0, 11)
                    if fact2 != fact1:
                        break
                fact3 = random.randint(0, 11)
                while fact3 in {fact1, fact2}:
                    fact3 = random.randint(0, 11)
                    if fact3 not in {fact1, fact2}:
                        break
                print(penguin_facts[fact1])
                print(penguin_facts[fact2])
                print(penguin_facts[fact3])
                apple_location = random.randint(0, 24)
                while apple_location in {penguin_position, fish_location[0], fish_location[1], fish_location[2],
                                         crab_location}:
                    apple_location = random.randint(0, 24)
                    if apple_location not in {penguin_position, fish_location[0], fish_location[1], fish_location[2],
                                              crab_location, book_location}:
                        break
                crab_location = 30
                map[apple_location] = emoji_assets[14]
                print("okay, you get the point. Now I'll tell you about the Apple of Wisdom. \n"
                      "*the Apple of Wisdom has appeared on the map*")
            if penguin_position == apple_location:
                event = 1
                print("{} has found the Apple of Wisdom \n".format(color_string) +
                      "{} eats the apple and transcend the universe, {} has infinite knowledge and wisdom, {} has ascended.".format(
                          color_string, color_string, color_string) + emoji_assets[21] + emoji_assets[4] + emoji_assets[
                          21] + "\n"
                                "    ~THE END~    ")
                endings[6] = "yes"
        elif area == 3:
            if penguin_position == parrot_location:
                event = 1
                print("'ey ey it's me, parrot' \n"
                      "Hop on my back, I can fly you out of here!")
                print(
                    "The parrot flies {} out of the rainforest unhurt and takes {} back to his family in antarctica. ".format(
                        color_string, color_string) + "\n" + emoji_assets[event_emoji + 1] + "\n" +
                    emoji_assets[4] + emoji_assets[15] + "\n"
                                                         "    ~THE END~    ")
                endings[9] = "yes"
            if penguin_position > 19:
                event = 1
                print("{} runs away from the fire and meets a firefighter \n".format(color_string) +
                      "He takes {} under his WING and {} becomes a firefighter \n".format(color_string, color_string) +
                      emoji_assets[22] + "\n" +
                      emoji_assets[4] + "\n"
                                        "The forest is saved!")
                make_map()
                show_map()
                print("    ~THE END~    ")
                endings[8] = "yes"
        if penguin_position == book_location:
            fact = random.randint(0, 11)
            print(penguin_facts[fact])

    #   ~END OF FUNCTIONS~
    #   ~Introduction~
    if replay == 0:
        print("PENGUIN CLUB 97 \n"
              "As I'm colorblind, I can't see the color of your feathers. \n"
              "What color are you?")
        ask_color()
    else:
        print("""You have completed:
    ~DUNGEON~
    use money: {}
    donate money: {}
    successfully answer dog questions: {}
    ~DESERT~
    bring Bob to area 51: {}
    hop in his UFO: {}
    successfully answer food & drink questions: {}
    ~OCEAN~
    obtain the apple of wisdom: {}
    collect fish: {}
    ~RAINFOREST~
    run from the fire: {}
    go to the parrot: {}
    """.format(endings[0], endings[1], endings[2], endings[3], endings[4], endings[5], endings[6], endings[7],
               endings[8], endings[9]))
    # position variable contains the x, y
    position = [0, 0]
    # sets area boundaries in a "west x", "east x", "south y", "north y". Based on what area it is
    area_boundry = [-3, 3, -3, 3]
    if area == 0:
        print("{} is in a musty dungeon".format(color_string))
    elif area == 1:
        print("{} is in a sandy desert".format(color_string))
    elif area == 2:
        print("{} is in the Pacific Ocean".format(color_string))
    elif area == 3:
        print("{} is in a jungle \n".format(color_string) +
              "The jungle is on fire! run away!")
    make_map()
    make_events()
    show_map()
    while event == 0:
        try:
            direction = int(input("Which way would you like to go? \n"
                                  "-1- north ▲       -2- south ▼ \n"
                                  "-3- east ▶        -4- west ◀ \n"))
            if direction == 1:
                if map[penguin_position - 5] == emoji_assets[11]:
                    print("Don't walk into the fire!")
                else:
                    position[1] += 1
                    move_check()
            elif direction == 2:
                position[1] -= 1
                move_check()
            elif direction == 3:
                position[0] += 1
                move_check()
            elif direction == 4:
                position[0] -= 1
                move_check()
            else:
                invalid_input()
        except:
            invalid_input()
    replay = 1


while play == 1:
    game() 

			
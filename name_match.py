import random

# name_match.py - a game where the user will matches the first name to the last.
# Player will choose the number of rounds/ questions and be given 3 chioces (1
# correct, 2 false)


# Obtained the names from webscraping the roster - stored in a dictionary.
# In the case of multiple people having the same surname the first names are
# grouped.

name_dict = {'Flowers': 'Tre',
 'Ray': 'Wyatt',
 'McCloud': 'Nick',
 'Hill': 'B.J./ Trey/ Holton',
 'Hodge': 'Darius',
 'Evans': 'Chris/ Jordan',
 'McPherson': 'Evan',
 'Shelvin': 'Tyler',
 'Sample': 'Cam/ Drew',
 'Carman': 'Jackson',
 'Chase': "Ja'Marr",
 'Allen': 'Ricardo/ Brandon',
 'Apple': 'Eli',
 'Ogunjobi': 'Larry',
 'Hilton': 'Mike',
 'Awuzie': 'Chidobe',
 'Hendrickson': 'Trey',
 'Reiff': 'Riley',
 'Spain': 'Quinton',
 'Davis': 'Jalen',
 'Wilcox': 'Mitchell',
 'Bailey': 'Markus',
 'Davis-Gaither': 'Akeem',
 'Wilson': 'Logan/ Brandon',
 'Higgins': 'Tee',
 'Burrow': 'Joe',
 'Thomas': 'Mike/ Michael',
 'Bell': 'Vonn',
 'Reader': 'D.J.',
 'Prince': 'Isaiah',
 'Johnson': 'Fred',
 'Irwin': 'Trenton',
 'Perine': 'Samaje',
 'Morgan': 'Stanley',
 'Pratt': 'Germaine',
 'Williams': 'Jonah/ Trayveon',
 'Tate': 'Auden',
 'Phillips': 'Darius',
 'Hubbard': 'Sam',
 'Bates III': 'Jessie',
 'Huber': 'Kevin',
 'Hopkins': 'Trey',
 'Uzomah': 'C.J.',
 'Tupou': 'Josh',
 'Harris': 'Clark',
 'Boyd': 'Tyler',
 'Mixon': 'Joe',
 'Adeniji': 'Hakeem',
 'Kareem': 'Khalid',
 'Smith': "D'Ante",
 'Ossai': 'Joseph',
 "Su'a-Filo": 'Xavier',
 'Waynes': 'Trae',
 'Hubert': 'Wyatt',
 'Holyfield': 'Elijah',
 'Browning': 'Jake',
 'Spence': 'Noah',
 'Gaillard': 'Lamont',
 'Bachie': 'Joe',
 'Taylor': 'Trent',
 'Williams Jr.': 'Pooka',
 'Jones': 'Keandre',
 'Daniels': 'Mike',
 'Sutherland': 'Keaton',
 'Wren': 'Renell',
 'Henderson': 'Trayvon',
 'Schreck': 'Mason',
 'Moss': 'Thaddeus'}

# Returns shuffled lists of first and last names
def create_lists(dict):
    last_names = []
    first_names = []
    for last, first in name_dict.items():
        last_names.append(last)
        first_names.append(first)
    random.shuffle(first_names)
    random.shuffle(last_names)
    return first_names, last_names


def ask_question(first_names, last_names, rounds):
    score = 0
    for i in range(rounds):
        # Questions will be the shuffled last names in order for i rounds
        print(f'{i+1}. _________ {last_names[i]}')
        print('\n')
        # create list of 1 correct and 2 incorrect names and shuffle
        choices = []
        choices.append(name_dict[last_names[i]])
        first_names.remove(name_dict[last_names[i]])
        choices = choices + random.sample(first_names, 2)
        random.shuffle(choices)

        for x in range(1,4):
            print(f'\t {x}. {choices[x-1]}')
        guess_index = make_guess()
        
        if choices[guess_index] == name_dict[last_names[i]]:
            score+=1
            print('Correct!\n')
        else:
            print(f'Incorrect. The answer was {name_dict[last_names[i]]} {last_names[i]}\n')
    print(f'You scored {score}/{rounds}')

# converts guess (1,2,3) to index (0,1,2)
def make_guess():
    guess = 999
    options = [1,2,3]
    while guess not in options:
        guess = int(input('Guess the first name? 1, 2 or 3'))
        if guess not in options:
            print('Pick 1,2 or 3')
    
    return int(guess-1)


in_game = True
while in_game:
    fn, ln = create_lists(name_dict)
    try:
        rnds = int(input("How many rounds would you like to play?"))
        if rnds <= 0 | rnds > len(name_dict):
            raise Exception
    
    except ValueError:
        print(f'Must be a number below {len(name_dict)}')
        break
    except Exception:
        print(f"Number must be between 1 and {len(name_dict)}")
        break

    ask_question(fn, ln, rnds)
    play = 'abc'
    while play.lower() not in ['y', 'n']:
        play = input('Play again (y/n)?')
    
    if play == 'y':
        pass

else:
    in_game = False

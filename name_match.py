import bs4, requests, lxml
import random

class Player:

    def __init__(self, first, last, pos, number):
        self.first = first
        self.last = last
        self.pos = pos
        self.number = number

    def __str__(self):
        return f'#{self.number} {self.first} {self.last} Position: {self.pos}'


def clean_data(row):
    split_row = row.getText().strip('\n').split('\n')
    clean_row = []
    for data in split_row:
        if data != '':
            clean_row.append(data)
    return clean_row


def create_player_list(rows):
    players = []

    for row in rows:
        clean = clean_data(row)
        if clean[0] != 'Player':
            first, last = clean[0].split(maxsplit=1)
            name, num, pos, ht, wt, age, exp, college = clean
            # print(first, last, pos, num, 'has been added')
            players.append(Player(first, last, pos, num))
    
    return players

# Returns shuffled lists of first and last names
def create_lists(players):
    firsts = [player.first for player in players]
    lasts = [player.last for player in players]
    random.shuffle(firsts)
    random.shuffle(lasts)
    return firsts, lasts
    

def check_duplicates(choices, first):
    while len(set(choices)) != 3:
        c2 = []
        for item in choices:
            if item not in c2:
                c2.append(item)
        while len(c2) < 3:
            new = random.sample(set(first), 1)
            if new not in c2:
                c2.extend(new)
        choices = c2
    return choices


def ask_question(first, last, rounds):
    score = 0
    for i in range(rounds):
        # Find the class instance that matches the last name
        for player in players:
            if last[i] == player.last:
                chosen = player
        # Questions will be the shuffled last names in order for i rounds
        print(f'{i+1}. _________ {chosen.last} - {chosen.pos}')
        print('\n')
        choices = []
        choices.append(chosen.first)
        choices = choices + random.sample(first, 2)
        checked_choices = check_duplicates(choices,first)
        random.shuffle(checked_choices)

        for x in range(1,4):
            print(f'\t {x}. {choices[x-1]}')
        guess_index = make_guess()

        if choices[guess_index] == chosen.first:
            score+=1
            print(f'Correct! {chosen}\n')
        else:
            print(f'Incorrect. The answer was {chosen}\n')
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


res = requests.get("https://www.bengals.com/team/players-roster/")
soup = bs4.BeautifulSoup(res.text, 'lxml')
rows = soup.select('tr')

players = create_player_list(rows)



# GAME LOGIC

in_game = True
while in_game:
    fn, ln = create_lists(players)
    try:
        rnds = int(input("How many rounds would you like to play?"))
        if rnds <= 0 | rnds > len(players):
            raise Exception
    
    except ValueError:
        print(f'Must be a number below {len(players)}')
        break
    except Exception:
        print(f"Number must be between 1 and {len(players)}")
        break

    ask_question(fn, ln, rnds)
    play = 'abc'
    while play.lower() not in ['y', 'n']:
        play = input('Play again (y/n)?')
    
    if play == 'y':
        pass

    else:
        in_game = False

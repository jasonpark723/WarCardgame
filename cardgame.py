"""
    OOP Card Game Hackathon

    open terminal -> cd to dir where your py file is
    open shell by typing python or python3 on mac
    from name_of_file import *

    now you can execute functions / use vars from file in shell

    Starting code:
"""
import random
import pyfiglet


class CardImg(object):

    card_values = {
        'Ace': 11,  # value of the ace is high until it needs to be low
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10,
        'Jack': 10,
        'Queen': 10,
        'King': 10
    }

    def __init__(self, suit, rank):
        """
        :param suit: The face of the card, e.g. Spade or Diamond
        :param rank: The value of the card, e.g 3 or King
        """
        self.suit = suit.capitalize()
        self.rank = rank
        self.points = self.card_values[rank]


def ascii_version_of_card(*cards, return_string=True):
    """
    Instead of a boring text version of the card we render an ASCII image of the card.
    :param cards: One or more card objects
    :param return_string: By default we return the string version of the card, but the dealer hide the 1st card and we
    keep it as a list so that the dealer can add a hidden card in front of the list
    """
    # we will use this to prints the appropriate icons for each card
    suits_name = ['Spades', 'Diamonds', 'Hearts', 'Clubs']
    suits_symbols = ['♠', '♦', '♥', '♣']

    # create an empty list of list, each sublist is a line
    lines = [[] for i in range(9)]

    for index, card in enumerate(cards):
        # "King" should be "K" and "10" should still be "10"
        if card.rank == '10':  # ten is the only one who's rank is 2 char long
            rank = card.rank
            space = ''  # if we write "10" on the card that line will be 1 char to long
        else:
            # some have a rank of 'King' this changes that to a simple 'K' ("King" doesn't fit)
            rank = card.rank[0]
            space = ' '  # no "10", we use a blank space to will the void
        # get the cards suit in two steps
        suit = suits_name.index(card.suit)
        suit = suits_symbols[suit]

        # add the individual card on a line by line basis
        lines[0].append('┌─────────┐')
        # use two {} one for char, one for space or char
        lines[1].append('│{}{}       │'.format(rank, space))
        lines[2].append('│         │')
        lines[3].append('│         │')
        lines[4].append('│    {}    │'.format(suit))
        lines[5].append('│         │')
        lines[6].append('│         │')
        lines[7].append('│       {}{}│'.format(space, rank))
        lines[8].append('└─────────┘')

    result = []
    for index, line in enumerate(lines):
        result.append(''.join(lines[index]))

    # hidden cards do not use string
    if return_string:
        return '\n'.join(result)
    else:
        return result


def ascii_version_of_hidden_card(*cards):
    """
    Essentially the dealers method of print ascii cards. This method hides the first card, shows it flipped over
    :param cards: A list of card objects, the first will be hidden
    :return: A string, the nice ascii version of cards
    """
    # a flipper over card. # This is a list of lists instead of a list of string becuase appending to a list is better then adding a string
    lines = [['┌─────────┐'], ['│░░░░░░░░░│'], ['│░░░░░░░░░│'], ['│░░░░░░░░░│'], [
        '│░░░░░░░░░│'], ['│░░░░░░░░░│'], ['│░░░░░░░░░│'], ['│░░░░░░░░░│'], ['└─────────┘']]

    # store the non-flipped over card after the one that is flipped over
    cards_except_first = ascii_version_of_card(*cards[1:], return_string=False)
    for index, line in enumerate(cards_except_first):
        lines[index].append(line)

    # make each line into a single list
    for index, line in enumerate(lines):
        lines[index] = ''.join(line)
    return '\n'.join(lines)

    # convert the list into a single string
    return '\n'.join(lines)


# TEST CASES
test_card_1 = CardImg('Diamonds', '4')
# test_card_2 = CardImg('Clubs', 'Ace')
# test_card_3 = CardImg('Spades', 'Jack')
# test_card_4 = CardImg('Hearts', '10')


def end_game():
    print(ascii_version_of_hidden_card(test_card_1))
    print('\n'*8)
    print(ascii_version_of_hidden_card(test_card_1))


def show_card(pile_card):
    print(ascii_version_of_hidden_card(test_card_1))
    print(ascii_version_of_card(pile_card))
    print(ascii_version_of_hidden_card(test_card_1))

# print(ascii_version_of_hidden_card(test_card_1, test_card_2))

##########################################################################################


p1_cards = []
p2_cards = []
pile = []


class Card():
    def __init__(self, suit, val):
        self.suit = suit
        self.val = val

        names = {
            1: "Ace",
            11: "Jack",
            12: "Queen",
            13: "King"
        }

        # if name doesn't exist, use val as a string for name
        self.name = names.get(val) or str(val)

    def __str__(self):
        return f"{self.name} of {self.suit}"

    def show(self):
        print(f"{self.name} of {self.suit}")


class Deck():
    def __init__(self):
        self.cards = []

        for suit in ["Hearts", "Clubs", "Diamonds", "Spades"]:
            for val in range(1, 14):
                self.cards.append(Card(suit, val))
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)
        return self

    def show(self):
        for card in self.cards:
            card.show()
        return self

    def split(self):
        for x in range(0, 26):
            p1_cards.append(self.cards[x])
        for y in range(26, 52):
            p2_cards.append(self.cards[y])


class GameStart():
    def __init__(self, p1_cards, p2_cards, pile):
        self.p1_cards = p1_cards
        self.p2_cards = p2_cards
        self.pile = pile
        self.attack = None
        self.count = None

    def p1_flip(self):
        if len(self.p1_cards) == 0:
            print("GAME OVER! PLAYER 2 IS THE WINNER")
        flipped_card = self.p1_cards.pop(0)
        self.pile.append(flipped_card)
        card_value = flipped_card.name
        card_suit = flipped_card.suit
        new_card_image = CardImg(card_suit, card_value)
        show_card(new_card_image)
        print(f'player 1 played: {flipped_card} & (' +
              f"player 1 has {len(self.p1_cards)} cards left)")
        self.checkpile("player 2")

    def p2_flip(self):
        if len(self.p2_cards) == 0:
            print("GAME OVER! PLAYER 1 IS THE WINNER")
        flipped_card = self.p2_cards.pop(0)
        self.pile.append(flipped_card)
        card_value = flipped_card.name
        card_suit = flipped_card.suit
        new_card_image = CardImg(card_suit, card_value)
        show_card(new_card_image)
        print(f'player 2 played: {flipped_card} & (' +
              f"player 2 has {len(self.p2_cards)} cards left)")
        self.checkpile("player 1")

        # return flipped_card

    def p1_win(self):
        self.p1_cards += self.pile
        self.pile = []
        self.attack = None
        end_game()
        print("player 1 won the pot!")
        print(
            f"player 1 has {len(self.p1_cards)} cards left and player 2 has {len(self.p2_cards)} left")

    def p2_win(self):
        self.p2_cards += self.pile
        self.pile = []
        self.attack = None
        end_game()
        print("player 2 won the pot!")
        print(
            f"player 1 has {len(self.p1_cards)} cards left and player 2 has {len(self.p2_cards)} left")

    def checkpile(self, which_player):
        if self.pile[-1].val == 13:
            self.attack = True
            self.count = 3
            print(f"{which_player} has {self.count} moves left")
        elif self.pile[-1].val == 12:
            self.attack = True
            self.count = 2
            print(f"{which_player} has {self.count} moves left")
        elif self.pile[-1].val == 11:
            self.attack = True
            self.count = 1
            print(f"{which_player} has {self.count} moves left")
        elif self.pile[-1].val == 1:
            self.attack = True
            self.count = 4
            print(f"{which_player} has {self.count} moves left")
        elif 2 <= self.pile[-1].val <= 10:
            if self.attack:
                self.count -= 1
                if self.count == 0:
                    if which_player == "player 1":
                        self.p1_win()
                        self.count == None
                        return
                    else:
                        self.p2_win()
                        self.count == None
                        return
                if which_player == "player 1":
                    print(f"player 2 has {self.count} moves left")
                else:
                    print(f"player 1 has {self.count} moves left")
            return

            # self.p1_win
        # if player 2 wins then run p2 wins
        # else continue game


# starts the game and split the deck game_test
my_deck = Deck()  # makes a new deck
my_deck.shuffle().split()  # shuffle and split two
game_test = GameStart(p1_cards, p2_cards, pile)  # start game

result = pyfiglet.figlet_format('Welcome to the WAR GAMES!')
print(result)
end_game()
tutorial = pyfiglet.figlet_format('tutorial: ', font='digital')
print(tutorial)
print("To start the game, player 1 input a() + enter, and player 2 b() + enter")
# game_test.p1_flip()  # flip players1 card
# game_test.p2_flip()  # flip players2 card

# for card in game_test.p1_cards:
#     print(card.val, card.suit)
# print("%"*30)
# for card in game_test.p2_cards:
#     print(card.val, card.suit)
# print("%"*30)


def a():
    game_test.p1_flip()


def b():
    game_test.p2_flip()
# print(a.val, a.suit)
# print(b.val, b.suit)


def reveal():
    print("player 1 has " + str(len(game_test.p1_cards)) +
          " cards left and player 2 has " + str(len(game_test.p2_cards)) + " left")

# for card in game_test.p1_cards:
#   print(card.val, card.suit)
# print("%"*30)
# for card in game_test.p2_cards:
#   print(card.val, card.suit)
# print("%"*30)

# for card in game_test.p2_cards:
#   print(card.val, card.suit)
# print("%"*30)
# game_test.p2_flip()
# game_test.p2_flip()
# game_test.p2_flip()
# game_test.p2_flip()
# game_test.p2_flip()
# game_test.p2_flip()
# game_test.p2_flip()
# game_test.p2_flip()
# for card in game_test.pile:
#   print(card.val, card.suit)
# print("%"*30)
# for card in game_test.p2_cards:
#   print(card.val, card.suit)

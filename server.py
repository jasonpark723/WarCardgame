from flask import Flask, render_template, request, redirect
import random
app = Flask(__name__)
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

    def p1_flip(self):
        flipped_card = self.p1_cards.pop(0)
        self.pile.append(flipped_card)
        self.check()
        return flipped_card

    def p2_flip(self):
        flipped_card = self.p2_cards.pop(0)
        self.pile.append(flipped_card)
        self.check()
        return flipped_card

    def p1_win(self):
        self.p1_cards += self.pile
        self.pile = []

    def p2_win(self):
        self.p2_cards += self.pile
        self.pile = []

    def check(self):
        pass
        # if player 1 wins then run p1_win
        # if player 2 wins then run p2 wins
        # else continue game


# starts the game and split the deck game_test
my_deck = Deck()
my_deck.shuffle().split()
game_test = GameStart(p1_cards, p2_cards, pile)


for card in game_test.p1_cards:
    print(card.val, card.suit)
print("%"*30)
for card in game_test.p2_cards:
    print(card.val, card.suit)
print("%"*30)
a = game_test.p1_flip()
b = game_test.p2_flip()
print(a.val, a.suit)
print(b.val, b.suit)


@app.route('/')
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)

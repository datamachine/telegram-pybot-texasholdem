import deck import deck
from rules import name_of_hand

class Table:
    def __init__(self, players):
        self.deck = deck()
        self.board = []

        if len(players) < 2 or len(players) > 10:
            raise Exception('Invalid number of players. It must be between 2 and 10.')

        self.players = players

    def new_hand(self):
        for player in self.players:
            player.hand = []

        self.board = []
        self.shuffle()

    def shuffle(self):
        return self.deck.shuffle()

    def get_flop(self):
        # Burn 3
        if not self.deck.deal(3):
            return False
        return self.deck.deal(3)

    def get_one(self):
        # Burn 1
        if not self.deck.deal(1):
            return False
        return self.deck.deal(1)

    def deal(self):
        num_cards = 2
        if num_cards * len(self.players) > self.deck.cards_left():
            return False # Can't imagine how this is possible

        for i in range(num_cards):
            for player in self.players:
                player.hand.extend(self.deck.deal(1))

    def score_player(self, player):
        score = 0
        hand = player.hand
        hand.extend(self.board)

        # Find pairs
        pairs = {}
        prev = 0

        for card in sorted(hand, key=lamda card: card.value):
            if prev == card.value:
                if key in pairs:
                    pairs[key] += 1
                else:
                    pairs[key] = 2
            prev = card.value

        # Find set distributions
        nop = {}
        for k, v in pairs.items():
            if v in nop:
                nop[v] += 1
            else:
                nop[v] = 1

        # 4 of a kind
        if 4 in nop:
            score = 7
            kicker = pairs.keys()
            # Ensures the first kicker is the value of the 4 of a kind
            kicker = [key for key in kicker if pairs[key] == 4]
            key = kicker[0]

            # Gets a list of all the cards remaining once the the 4 of a kind is removed
            temp = [card.value for card in hand if card.value != key]
            card_value = temp.pop()
            kicker.append(card_value)

            return [score, kicker]

        # 3 of a kind
        elif 3 in nop:
            pass


        pass

    def determine_winner(self):
        pass

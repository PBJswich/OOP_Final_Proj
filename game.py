import random
class cards():
    def __init__(self):
        
        # C = clover, D = diamond, H = Hearts, S = Spades
        self.card_symbol = ["C", "D", "H", "S"]
        self.deck = []
    
    def create_deck(self):
        for i in self.card_symbol:
            # 10 = jack, 11 = queen, 12 = king, 13 = ace
            for j in range(1,14):
                m = str(j)
                conjoin = [i+m]
                self.deck.append(conjoin)

    def show_deck(self):
        for i in self.deck:
            print(f"{i}")

    def shuffle_deck(self):
        for i in range(1,10):
            for k in range(1, len(self.deck) - 1):
                r = random.randint(0,len(self.deck) - 1)
                l = self.deck[r]
                self.deck[r] = self.deck[k]
                self.deck[k] = l
    def get_rid_used_cards(self, i ,k):
        self.deck.remove(i)
        self.deck.remove(k)

    def give_hand(self):
        i = random.randint(0,len(self.deck) - 1)
        k = random.randint(0,len(self.deck) - 1)
        return self.deck[i],self.deck[k]
    
    def delete_deck(self):
        self.deck = []
# Tests for cards
# c = cards()
# c.create_deck()
# c.show_deck()
# c.shuffle_deck()
# c.show_deck()
# i,k = c.give_hand()
# print(str(i), str(k))
# print()
# c.get_rid_used_cards(i,k)
# c.show_deck()  

class Poker:                    #default blinds 5/10
    def __init__(self, player, small_blind = 5, big_blind =10, card = []):
        self.player = player
        self.small_blind = small_blind
        self.big_blind = big_blind
        self.pot_size = 0
        self.game_state = "Pre-Flop"
        self.cards = card
    
class player:
    def __init__(self, name, balance, hand, blind_state, turn):
        self.name = name
        self.balance = balance
        self.hand = hand
        self.blind_state = blind_state
        self.turn = turn
    def show_hand(self):
        for i in self.hand:
            print(f"{i}")
    def raise_pot(self, ammount):
        balance -= balance-ammount


        
    
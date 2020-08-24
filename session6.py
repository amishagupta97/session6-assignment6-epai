import gc
vals = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
suits = ['spades', 'clubs', 'hearts', 'diamonds']

def deck_cards_using_single_expression():
    '''
    function creates 52 cards in a deck with the help of lambda, zip and map functions 
    input : no input required
    output : list of tuples containing combination of 52 cards in a deck.
    '''
    return list(card for new_suit in map(lambda one_suit: list(zip(vals, [one_suit] * len(vals))), suits) for card in new_suit)

def deck_cards_using_normal_function():
    '''
    function creates 52 cards in a deck with the normal function without using lambda, zip and map functions
    input : no input required
    output : list of tuples containing combination of 52 cards in a deck.
    '''
    deck_cards = []
    for i in suits:
        for j in vals:
            deck_cards.append((j, i))
    return deck_cards

def play_poker_game(hand1:'list of tuples containing cards for player1', hand2:'list of tuples containing cards for player2') -> str:
    '''
    function evaluates which player has won poker game
    input : two list of tuples containing set of 3, 4 or 5 cards
    output : player who won with reason
    '''
    if len(hand1) != len(hand2) or len(hand1) < 3 or len(hand1) > 5:
        raise ValueError
    playerOnesHand = Hand(hand1)
    playerTwosHand = Hand(hand2)

    playerOneScore = playerOnesHand.check_hand_score()
    playerTwoScore = playerTwosHand.check_hand_score()

    if playerOneScore[0] != 0 or playerTwoScore[0] != 0:
        if playerOneScore[0] > playerTwoScore[0]:
            result = "Player 1 won! He has a {0}".format(playerOneScore[1])
        elif playerOneScore[0] == playerTwoScore[0]:
            result = "It's a draw! Both players have {0}".format(playerOneScore[1])
        else: 
            result = "Player 2 won! He has a {0}".format(playerTwoScore[1])
    else:
        if max(playerOnesHand.values) > max(playerTwosHand.values):
            result = "Player 1 won! He has a High Card"
        elif max(playerOnesHand.values) == max(playerTwosHand.values): 
            result = "Again it's a draw! Both players have same High Card"
        else: 
            result = "Player 2 won! He has a High Card"
    return result

class Hand: 

    def __init__(self, cards):
        self.cards = []
        self.values = []
        for c in cards:
            self.cards.append(Card(c))
        self.setValues()

    def setValues(self):
        for card in self.cards:
            self.values.append(card.value)
        self.values.sort()

    def isRoyalFlush(self):
        currentSuit = self.cards[0].suit
        for card in self.cards:
            if card.suit != currentSuit:
                return False
            currentSuit = card.suit
        lowest_value = max(self.values)
        if lowest_value == 14 :
            num = len(self.values)
            for i in range(num):
                if not((lowest_value - i) in self.values):
                    return False
            return True

    def isStraightFlush(self):
        if self.isStraight() and self.isFlush():
            return True
        else:
            return False

    def isFourOfAKind(self):
        if (len(self.values)) < 4:
            return False
        cardOneCount = self.values.count(self.values[0])
        cardTwoCount = self.values.count(self.values[len(self.values) - 1])
        if cardOneCount == 4 or cardTwoCount == 4:
            return True
        else: 
            return False

    def isFullHouse(self):
        if (len(self.values)) < 5:
            return False
        cardOneCount = self.values.count(self.values[0])
        cardTwoCount = self.values.count(self.values[len(self.values) - 1])

        if (cardOneCount == 2 and cardTwoCount == 3 ) or (cardOneCount == 3 and cardTwoCount == 2):
            return True
        else: 
            return False

    def isFlush(self):
        currentSuit = self.cards[0].suit
        for card in self.cards:
            if card.suit != currentSuit:
                return False
            currentSuit = card.suit
        return True

    def isStraight(self):
        lowest_value = min(self.values)
        num = len(self.values)
        for i in range(num):
            if lowest_value + i not in self.values:
                return False
        return True

    def isThreeOfAKind(self):
        cardOneCount = self.values.count(self.values[0])
        cardTwoCount = self.values.count(self.values[len(self.values) - 1])

        if cardOneCount == 3 or cardTwoCount == 3:
            return True
        else: 
            return False

    def isTwoPair(self):
        if (len(self.values)) < 4:
            return False
        cardOneCount = self.values.count(self.values[0])
        cardTwoCount = self.values.count(self.values[2])
        cardThreeCount = self.values.count(self.values[len(self.values) - 1])

        if(cardOneCount == 2 and cardTwoCount == 2) or (cardOneCount == 2 and cardThreeCount == 2) or (cardTwoCount == 2 and cardThreeCount == 2):
            return True
        return False

    def isOnePair(self):
        cardOneCount = self.values.count(self.values[0])
        cardTwoCount = self.values.count(self.values[2])
        cardThreeCount = self.values.count(self.values[len(self.values) - 1])

        if(cardOneCount == 2 or cardTwoCount == 2 or cardThreeCount == 2):
            return True
        return False

    def check_hand_score(self):
        if self.isRoyalFlush():
            return (9, 'Royal Flush')
        elif self.isStraightFlush(): 
            return (8, 'Straight Flush')
        elif self.isFourOfAKind(): 
            return (7, 'Four Of A Kind')
        elif self.isFullHouse(): 
            return (6, 'Full House')
        elif self.isFlush(): 
            return (5, 'Flush')
        elif self.isStraight(): 
            return (4, 'Straight')
        elif self.isThreeOfAKind(): 
            return (3, 'Three Of A Kind')
        elif self.isTwoPair(): 
            return (2, 'Two Pair')
        elif self.isOnePair(): 
            return (1, 'One Pair') 
        else:
            return (0, 'No Hand')

class Card:

    def __init__(self, card=[]):
        self.value = self.determineValue(card[0])
        self.suit = card[1]

    def determineValue(self,y):
        return {
            '2':2,
            '3':3,
            '4':4,
            '5':5,
            '6':6,
            '7':7,
            '8':8,
            '9':9,
            '10':10,
            'jack':11,
            'queen':12,
            'king':13,
            'ace':14
        }.get(y)
import numpy as np
N = 10
nPlayers = 5
startingHand = ["2c", "3c"]

def compare_two_players(player1Cards,player2Cards,dealerCards):
    return np.random.choice([0,1,2],size=1)

def cardname_to_int(ranksuit):
    rank_dict = {'2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7, '9': 8, 'T': 9, 'J': 10, 'Q': 11, 'K': 12,
                 'A': 13}
    card_dict = {'c': 1, 'd': 2, 'h': 3, 's': 4}
    return (rank_dict[ranksuit[0]] - 1) * 4 + card_dict[ranksuit[1]] - 1

def generatePlayersCards(nPlayers: int, availableDeck: np.array):
    # do things here
    playersCards = np.random.choice(availableDeck, size=2 * nPlayers, replace=False)
    playersCards = playersCards.reshape(nPlayers, 2)
    updatedCardDeck = np.setdiff1d(availableDeck, playersCards)
    return (playersCards, updatedCardDeck)


def generateDealerCards(availableDeck: np.array):
    # do things here
    dealerCards = np.random.choice(availableDeck, size=5, replace=False)
    updatedCardDeck = np.setdiff1d(availableDeck, dealerCards)
    return (dealerCards, updatedCardDeck)


def WhoWin(startCards, playersCards, dealerCards):
    allwin = True
    alltie = True
    for player2Cards in playersCards:
        result = compare_two_players(startCards, player2Cards, dealerCards)
        if result != 0:
            allwin = False
        if result != 2:
            alltie = False
    if allwin:
        gameResult = [1, 0, 0]
    elif alltie:
        gameResult = [0, 0, 1]
    else:
        gameResult = [0, 1, 0]
    gameResult = np.array(gameResult)
    return gameResult


gameResult = np.array([0, 0, 0])
for i in range(N):
    availableDeck = np.arange(52)
    np.random.shuffle(availableDeck)
    startcards = [cardname_to_int(x) for x in startingHand]
    availableDeck = np.setdiff1d(availableDeck, startcards)
    playersCards, availableDeck = generatePlayersCards(nPlayers, availableDeck)
    dealerCards, availableDeck = generateDealerCards(availableDeck)
    result = WhoWin(startcards, playersCards, dealerCards)
    gameResult += result

print(gameResult)
gameResult = gameResult / N
winProbability, loseProbability, tieProbability = gameResult
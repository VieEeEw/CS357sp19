import numpy as np

def WhoWin(startCards, playersCards, dealerCards):
    win_count = 0
    lose_count = 0
    tie_count = 0
    gameResult = np.zeros(3, dtype=int)
    for oc in playersCards:
        if compare_two_players(startCards,oc,dealerCards) == 0:
            # print(sc.shape, oc.shape)
            win_count += 1
        elif compare_two_players(startCards,oc,dealerCards) == 1:
            lose_count += 1
        else:
            tie_count += 1
    if win_count == len(playersCards):
        gameResult[0] = 1
        return gameResult
    elif lose_count >= 1:
        gameResult[1] = 1
        return gameResult
    gameResult[2] = 1
    return gameResult


#first change the startingHands to startCards
startCards = np.zeros(len(startingHand), dtype=int)
for index, card in enumerate(startingHand):
    startCards[index] = cardname_to_int(card)
whole_deck = np.arange(52)
updatedCardDeck = np.setdiff1d(whole_deck,startCards)
win_rounds = 0
tie_rounds = 0
lose_rounds = 0
#start simulation
for game in range(N):
    playersCards, availableDeck = generatePlayersCards(nPlayers, updatedCardDeck)
    dealerCards, availableDeck = generateDealerCards(availableDeck)
    #mark:I have already distributed the cards
    gameResult = WhoWin(startCards, playersCards, dealerCards)
    if gameResult[0] == 1:
        win_rounds += 1
    elif gameResult[1] == 1:
        lose_rounds += 1
    elif gameResult[2] == 1:
        tie_rounds += 1
winProbability = win_rounds / N
loseProbability = lose_rounds / N
tieProbability = tie_rounds / N
print(winProbability)
print(loseProbability)
print(tieProbability)
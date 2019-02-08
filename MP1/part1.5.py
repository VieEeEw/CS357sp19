import numpy as np
def MonteCarloSimulation(M,N,nPlayers,startingHand):
    # do stuff here
    startCards = [cardname_to_int(x) for x in startingHand]
    gameDeck = np.arange(52)
    gameDeck = np.setdiff1d(gameDeck, startCards)
    winProb = []
    for i in range(M):
        win_count = 0
        for j in range(N):
            playersCards, availableDeck = generatePlayersCards(nPlayers, gameDeck)
            dealerCards, availableDeck = generateDealerCards(availableDeck)
            result = WhoWin(startCards, playersCards, dealerCards)
            win_count += result[0]
        winProb.append(win_count/N)
    return np.array(winProb)
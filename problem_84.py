import random
from collections import deque

# Set how many faces a die has
FACES = 4

# Set the maximum number of moves in a game
MAX_MOVES = 100000

# Games to be simulated
GAMES = 100

# Constructing the decks of cards
CC_CARDS = ["advance to go", "go to jail"] + ["dud"] * 14
CH_CARDS = [
    "advance to go", "go to jail", 
    "go to c1", "go to e3",
    "go to h2", "go to r1",
    "go to next r", "go to next r",
    "go to next u", "go back 3 squares"
] + ["dud"] * 6

# Constructing the board as a dictionary
cells_list = [
    "GO", "A1", "CC1", "A2", "T1", "R1", "B1", "CH1",
    "B2", "B3", "JAIL", "C1", "U1", "C2", "C3", "R2",
    "D1", "CC2", "D2", "D3", "FP", "E1", "CH2", "E2",
    "E3", "R3", "F1", "F2", "U2", "F3", "G2J", "G1",
    "G2", "CC3", "G3", "R4", "CH3", "H1", "T2", "H2"
]

CELLS = {name: idx for idx, name in enumerate(cells_list)}
REVERSE_CELLS = {idx: name for name, idx in CELLS.items()}
CELLS_NUMBER = len(cells_list)

def die(n):
    return random.randint(1, n)

def throw(doublesCounter):
    d1 = die(FACES)
    d2 = die(FACES)
    if d1 == d2:
        doublesCounter += 1
    else:
        # Rolling non-double resets doubles counter for the usual Monopoly rules
        doublesCounter = 0
    return d1, d2, doublesCounter

def advance(currentPosition, d1, d2):
    return (currentPosition + d1 + d2) % CELLS_NUMBER

def draw(deck):
    card = deck.popleft()
    deck.append(card)
    return card

def visited(currentPosition, cellsVisited):
    cellsVisited[REVERSE_CELLS[currentPosition]] += 1
    return cellsVisited

def effectCC(currentPosition, cc_deck):
    effect = draw(cc_deck)
    if (effect == "advance to go"):
        currentPosition = CELLS["GO"]
    elif (effect == "go to jail"):
        currentPosition = CELLS["JAIL"]
    return currentPosition

def gotoNextR(currentPosition):
    if currentPosition < CELLS["R1"]:
        return CELLS["R1"]
    elif currentPosition < CELLS["R2"]:
        return CELLS["R2"]
    elif currentPosition < CELLS["R3"]:
        return CELLS["R3"]
    return CELLS["R4"]

def gotoNextU(currentPosition):
    if currentPosition < CELLS["U1"]:
        return CELLS["U1"]
    return CELLS["U2"]

def effectCH(currentPosition, ch_deck, cc_deck):
    effect = draw(ch_deck)
    # If go back 3 squares lands on CC, we must draw from CC deck
    if effect == "go back 3 squares":
        currentPosition = (currentPosition - 3) % 40
        # if that square is a CC, apply CC effect
        if currentPosition in [CELLS["CC1"], CELLS["CC2"], CELLS["CC3"]]:
            currentPosition = effectCC(currentPosition, cc_deck)
    else:
        if effect == "advance to go":
            currentPosition = CELLS["GO"]
        elif effect == "go to jail":
            currentPosition = CELLS["JAIL"]
        elif effect == "go to c1":
            currentPosition = CELLS["C1"]
        elif effect == "go to e3":
            currentPosition = CELLS["E3"]
        elif effect == "go to next r":
            currentPosition = gotoNextR(currentPosition)
        elif effect == "go to next u":
            currentPosition = gotoNextU(currentPosition)
        # other dud cards do nothing
    return currentPosition

def game():
    # Shuffle and create decks for this game (don't reuse global deques from earlier runs)
    random.shuffle(CC_CARDS)
    random.shuffle(CH_CARDS)
    cc_deck = deque(CC_CARDS)
    ch_deck = deque(CH_CARDS)
    
    currentPosition = CELLS["GO"]
    doublesCounter = 0
    remainingMoves = MAX_MOVES

    # Create a fresh visited dict
    cellsVisited = {name: 0 for name in CELLS.keys()}

    while remainingMoves > 0:
        d1, d2, doublesCounter = throw(doublesCounter)
        if doublesCounter == 3:
            currentPosition = CELLS["JAIL"]
            doublesCounter = 0
        else:
            currentPosition = advance(currentPosition, d1, d2)
            if currentPosition == CELLS["G2J"]:
                currentPosition = CELLS["JAIL"]
            elif currentPosition in [CELLS["CC1"], CELLS["CC2"], CELLS["CC3"]]:
                currentPosition = effectCC(currentPosition, cc_deck)
            elif currentPosition in [CELLS["CH1"], CELLS["CH2"], CELLS["CH3"]]:
                currentPosition = effectCH(currentPosition, ch_deck, cc_deck)
        cellsVisited = visited(currentPosition, cellsVisited)
        remainingMoves -= 1
    return cellsVisited

def getTopThree(cellsVisited):
    return sorted(cellsVisited, key=cellsVisited.get, reverse=True)[:3]

def main():
    bestCells = dict()
    for i in range(GAMES):
        cellsVisited = game()
        topThree = getTopThree(cellsVisited)
        for j in range(len(topThree)):
            if topThree[j] not in bestCells.keys():
                bestCells[topThree[j]] = cellsVisited[topThree[j]]
            else:
                bestCells[topThree[j]] += cellsVisited[topThree[j]]

        if i % 10 == 0:
            print("Games played: {}".format(i))

    # Played all the games. Display time
    print("Best cells overall:")
    bestCellsTopThree = getTopThree(bestCells)
    b1 = CELLS[bestCellsTopThree[0]]
    b2 = CELLS[bestCellsTopThree[1]]
    b3 = CELLS[bestCellsTopThree[2]]
    for el in bestCellsTopThree:
        print("- {}: {} ({}%)".format(el, bestCells[el], bestCells[el] / (GAMES * MAX_MOVES) * 100))
    print("Six-digit modal string: {}{}{}".format(b1, b2, b3))
    return

main()
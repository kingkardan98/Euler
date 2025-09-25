# Monopoly with 4-sided dies: what are the three most popular squares?
# I assign each cell a number, starting from 0 to 39

import random
from collections import deque

# Set how many faces a die has
FACES = 6

# Set the maximum number of moves in a game
MAX_MOVES = 1000

# Set the maximum number of games to run
MAX_GAMES = 100

# Constructing the decks of cards
CC_CARDS = ["advance to go", "go to jail"]
CH_CARDS = ["advance to go", "go to jail", 
            "go to c1", "go to e3",
            "go to h2", "go to r1",
            "go to next r", "go to next r",
            "go to next u", "go back 3 squares"]

CC_CARDS += ["dud"] * 14
CH_CARDS += ["dud"] * 6

CC_DECK = deque(CC_CARDS)
CH_DECK = deque(CH_CARDS)

CARDS_LEN = 16

# Constructing the board as a dictionary
cells_list = [
    "GO", "A1", "CC1", "A2", "T1", "R1", "B1", "CH1",
    "B2", "B3", "JAIL", "C1", "U1", "C2", "C3", "R2",
    "D1", "CC2", "D2", "D3", "FP", "E1", "CH2", "E2",
    "E3", "R3", "F1", "F2", "U2", "F3", "G2J", "G1",
    "G2", "CC3", "G3", "R4", "CH3", "H1", "T2", "H2"
]

CELLS = {name: idx for idx, name in enumerate(cells_list)}

# Second dictionary, for numerical board exploration
REVERSE_CELLS = {idx: name for name, idx in CELLS.items()}

def die1(n):
    """Throw die1"""
    return random.randint(1, n)

def die2(n):
    """Throw die2"""
    return random.randint(1, n)

def throw(doublesCounter):
    """Function that emulates the throw of two FACE-sided dies"""
    d1 = die1(FACES)
    d2 = die2(FACES)

    if d1 == d2:
        doublesCounter += 1

    return d1, d2, doublesCounter

def advance(currentPosition, d1, d2):
    """Returns the new position of the pawn on the board""" 
    return (currentPosition + d1 + d2) % 39

def draw(deck):
    """Draws a card from a deck, then places it on the bottom"""
    card = deck.popleft()
    deck.append(card)
    return card

def visited(currentPosition, cellsVisited):
    """Update the cellsVisited array. Search the etiquette numerically through REVERSE_CELLS"""
    cellsVisited[REVERSE_CELLS[currentPosition]] += 1
    return cellsVisited

def effectCC(currentPosition):
    """Emulates the drawing of a card on a CC cell"""
    # Landed on one of the community chest cells. Draw a card and operate accordingly
    effect = draw(CC_DECK)

    # Analyze first the cases that bring me to jail
    if (effect == "advance to go"):
        # Go to the GO cell and end turn.
        currentPosition = CELLS["GO"]
    elif (effect == "go to jail"):
        # Go to the JAIL cell and end turn.
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

def effectCH(currentPosition):
    effect = draw(CH_DECK)

    # SUPREME EDGE CASE: currentPosition = CC3 and effect = go back 3,
    # change the current position and call effectCC
    if currentPosition == CELLS["CH3"] and effect == "go back 3 squares":
        # Go back 3 squares and draw a CC card
        currentPosition = effectCC(currentPosition - 3)
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
        elif effect == "go back 3 squares":
            currentPosition -= 3
        else: 
            # Got a dud, do nothing
            pass
    return currentPosition

def game():
    """Emulates a MAX_MOVES-moves long game of monopoly"""
    # Shuffle the 16-card decks
    random.shuffle(CC_CARDS)
    random.shuffle(CH_CARDS)

    # Set my pawn at GO (cell 0)
    currentPosition = CELLS["GO"]

    # Counter to keep track of how many doubles I have rolled
    doublesCounter = 0

    # Set the length of the game
    remainingMoves = MAX_MOVES

    # Create a dictionary to keep track of which cells I visited, and how many times.
    # I base it on the alredy existing CELLS dictionary, just to not retype the structure.
    # I then reset each value to 0.
    cellsVisited = CELLS

    for cell in cellsVisited.keys():
        cellsVisited[cell] = 0

    while remainingMoves > 0:
        d1, d2, doublesCounter = throw(doublesCounter)
        if doublesCounter == 3:
            # First edge case: I rolled 3 doubles, I immediately go to jail
            currentPosition = CELLS["JAIL"]

            # Reset the doubles counter
            doublesCounter = 0
        else:
            # The triple double penalty wasn't met, advance.
            # This doesn't yet give me the condition to register the new cell as visited.
            # We first need to analyze all edge cases.
            advance(currentPosition, d1, d2)

            if currentPosition == CELLS["G2J"]:
                # Second edge case: I land on the G2J cell. I go to jail.
                currentPosition = CELLS["JAIL"]

            elif currentPosition in [CELLS["CC1"], CELLS["CC2"], CELLS["CC3"]]:
                currentPosition = effectCC(currentPosition)

            elif currentPosition in [CELLS["CH1"], CELLS["CH2"], CELLS["CH3"]]:
                # Landed on one of the chance cells. Draw a card.
                currentPosition = effectCH(currentPosition)
        
        # After the turn has ended, and positions have been set, update the cellsVisited array
        cellsVisited = visited(currentPosition, cellsVisited)
        remainingMoves -= 1
    
    return cellsVisited

def main():
    print(game())

main()
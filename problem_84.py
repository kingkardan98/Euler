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

def throw(doubles_counter):
    d1 = die(FACES)
    d2 = die(FACES)
    if d1 == d2:
        doubles_counter += 1
    else:
        # Rolling non-double resets doubles counter for the usual Monopoly rules
        doubles_counter = 0
    return d1, d2, doubles_counter

def advance(current_position, d1, d2):
    return (current_position + d1 + d2) % CELLS_NUMBER

def draw(deck):
    card = deck.popleft()
    deck.append(card)
    return card

def visited(current_position, cells_visited):
    cells_visited[REVERSE_CELLS[current_position]] += 1
    return cells_visited

def effect_cc(current_position, cc_deck):
    effect = draw(cc_deck)
    if effect == "advance to go":
        current_position = CELLS["GO"]
    elif effect == "go to jail":
        current_position = CELLS["JAIL"]
    return current_position

def goto_next_r(current_position):
    if current_position < CELLS["R1"]:
        return CELLS["R1"]
    elif current_position < CELLS["R2"]:
        return CELLS["R2"]
    elif current_position < CELLS["R3"]:
        return CELLS["R3"]
    return CELLS["R4"]

def goto_next_u(current_position):
    if current_position < CELLS["U1"]:
        return CELLS["U1"]
    return CELLS["U2"]

def effect_ch(current_position, ch_deck, cc_deck):
    effect = draw(ch_deck)
    # If we go back 3 squares lands on CC, we must draw from CC deck
    if effect == "go back 3 squares":
        current_position = (current_position - 3) % 40
        # if that square is a CC, apply CC effect
        if current_position in [CELLS["CC1"], CELLS["CC2"], CELLS["CC3"]]:
            current_position = effect_cc(current_position, cc_deck)
    else:
        if effect == "advance to go":
            current_position = CELLS["GO"]
        elif effect == "go to jail":
            current_position = CELLS["JAIL"]
        elif effect == "go to c1":
            current_position = CELLS["C1"]
        elif effect == "go to e3":
            current_position = CELLS["E3"]
        elif effect == "go to next r":
            current_position = goto_next_r(current_position)
        elif effect == "go to next u":
            current_position = goto_next_u(current_position)
        # other dud cards do nothing
    return current_position

def game():
    # Shuffle and create decks for this game (don't reuse global deques from earlier runs)
    random.shuffle(CC_CARDS)
    random.shuffle(CH_CARDS)
    cc_deck = deque(CC_CARDS)
    ch_deck = deque(CH_CARDS)
    
    current_position = CELLS["GO"]
    doubles_counter = 0
    remaining_moves = MAX_MOVES

    # Create a fresh visited dict
    cells_visited = {name: 0 for name in CELLS.keys()}

    while remaining_moves > 0:
        d1, d2, doubles_counter = throw(doubles_counter)
        if doubles_counter == 3:
            current_position = CELLS["JAIL"]
            doubles_counter = 0
        else:
            current_position = advance(current_position, d1, d2)
            if current_position == CELLS["G2J"]:
                current_position = CELLS["JAIL"]
            elif current_position in [CELLS["CC1"], CELLS["CC2"], CELLS["CC3"]]:
                current_position = effect_cc(current_position, cc_deck)
            elif current_position in [CELLS["CH1"], CELLS["CH2"], CELLS["CH3"]]:
                current_position = effect_ch(current_position, ch_deck, cc_deck)
        cells_visited = visited(current_position, cells_visited)
        remaining_moves -= 1
    return cells_visited

def get_top_three(cells_visited):
    return sorted(cells_visited, key=cells_visited.get, reverse=True)[:3]

def main():
    best_cells = dict()
    for i in range(GAMES):
        cells_visited = game()
        top_three = get_top_three(cells_visited)
        for j in range(len(top_three)):
            if top_three[j] not in best_cells.keys():
                best_cells[top_three[j]] = cells_visited[top_three[j]]
            else:
                best_cells[top_three[j]] += cells_visited[top_three[j]]

        if i % 10 == 0:
            print("Games played: {}".format(i))

    # Played all the games. Display time
    print("Best cells overall:")
    best_cells_top_three = get_top_three(best_cells)
    b1 = CELLS[best_cells_top_three[0]]
    b2 = CELLS[best_cells_top_three[1]]
    b3 = CELLS[best_cells_top_three[2]]
    for el in best_cells_top_three:
        print("- {}: {} ({}%)".format(el, best_cells[el], best_cells[el] / (GAMES * MAX_MOVES) * 100))
    print("Six-digit modal string: {}{}{}".format(b1, b2, b3))
    return

main()
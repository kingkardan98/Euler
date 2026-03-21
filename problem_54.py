from collections import Counter

def parse_hand(hand):
    # Separate the ranks and suits
    ranks = [card[0] for card in hand]
    suits = [card[1] for card in hand]
    return ranks, suits

def evaluate_hand(hand):
    ranks, suits = parse_hand(hand)
    
    # Map ranks to numerical values for easier comparison
    rank_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, 
                   '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 
                   'Q': 12, 'K': 13, 'A': 14}
    
    # Convert ranks to their numerical values
    rank_counts = Counter([rank_values[rank] for rank in ranks])
    suit_counts = Counter(suits)
    
    # Check for different hand ranks
    is_flush = len(set(suits)) == 1
    is_straight = (max(rank_counts.keys()) - min(rank_counts.keys()) == 4 
                   and len(rank_counts) == 5)
    
    # Check for pairs, three of a kinds, and four of a kinds
    counts = rank_counts.values()
    hand_rank = None
    if 4 in counts:
        hand_rank = (7, max(rank_counts, key=lambda k: rank_counts[k]))  # Four of a Kind
    elif 3 in counts and 2 in counts:
        hand_rank = (6, max(rank_counts, key=lambda k: rank_counts[k]))  # Full House
    elif is_flush and is_straight:
        hand_rank = (8, max(rank_counts))  # Straight Flush
    elif is_flush:
        hand_rank = (5, sorted(rank_counts.keys(), reverse=True))  # Flush
    elif is_straight:
        hand_rank = (4, max(rank_counts))  # Straight
    elif 3 in counts:
        hand_rank = (3, max(rank_counts, key=lambda k: rank_counts[k]))  # Three of a Kind
    elif list(counts).count(2) == 2:
        hand_rank = (2, sorted([k for k in rank_counts if rank_counts[k] == 2], reverse=True))  # Two Pair
    elif 2 in counts:
        hand_rank = (1, max(rank_counts, key=lambda k: rank_counts[k]))  # One Pair
    else:
        hand_rank = (0, sorted(rank_counts.keys(), reverse=True))  # High Card
    
    return hand_rank

def compare_hands(hand1, hand2):
    value1 = evaluate_hand(hand1)
    value2 = evaluate_hand(hand2)
    
    # Compare hand ranks
    if value1[0] > value2[0]:
        return 1
    elif value1[0] < value2[0]:
        return -1
    else:
        # If ranks are the same, compare the tie-breaking values
        if value1[1] > value2[1]:
            return 1
        elif value1[1] < value2[1]:
            return -1
        else:
            return 0

def main():
    with open('P54_aux.txt', 'r') as f:
        lines = f.readlines()
    
    counter = 0

    for line in lines:
        if line.strip():  # Ensure line is not empty
            cards = line.strip().split(' ')
            hand1 = cards[:5]
            hand2 = cards[5:]

            if compare_hands(hand1, hand2) == 1:
                counter += 1

    print(counter)

if __name__ == '__main__':
    main()

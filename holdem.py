def card2text(cards):
    if len(cards) != 2:
        raise ValueError('Only accepts a list of exactly 2 cards!')

    rankhi = cards[0].rank
    ranklo = cards[1].rank
    suited = cards[0].suit == cards[1].suit

    if rankhi == ranklo:
        # Check for pair
        return str(rankhi) * 2
    elif suited:
        # Check for suited
        return rankhi + ranklo + 's'
    else:
        # Offsuit
        return rankhi + ranklo + 'o'

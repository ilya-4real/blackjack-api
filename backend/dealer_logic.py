def decide(cards_sum):
    return True if cards_sum <= 13 else False


def get_result(users_total: int, dealers_total: int) -> str:
    users_cards_stronger: bool = users_total > dealers_total
    users_cards_out: bool = users_total > 21
    dealers_cards_stronger: bool = dealers_total > users_total
    dealers_cards_out: bool = dealers_total > 21
    cards_equal: bool = not dealers_cards_out and not users_cards_out and dealers_total == users_total

    if not users_cards_out and not dealers_cards_out:
        return 'user wins' if users_cards_stronger else 'dealer wins' if dealers_cards_stronger else 'draw'
    elif not users_cards_out and dealers_cards_out:
        return 'user win'
    elif not dealers_cards_out and users_cards_out:
        return 'dealer win'
    elif cards_equal:
        return 'draw'
    return 'draw'

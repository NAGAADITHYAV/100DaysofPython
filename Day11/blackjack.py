from art import CARDS, CARD_ART, HIDDEN_CARD
import random


class BlackJack:
    def __init__(self):
        self._reset_deck()

    def _reset_deck(self):
        self.deck = list(CARDS.keys())
        random.shuffle(self.deck)

    def deal_card(self):
        if len(self.deck) <= 6:
            raise Exception("Low on cards")
        return self.deck.pop()

    def deal_hand(self):
        return {
            "dealer_hand": [self.deal_card(), self.deal_card()],
            "player_hand": [self.deal_card(), self.deal_card()],
        }

    def hit(self, hand):
        hand.append(self.deal_card())
        return hand

    def calculate_score(self, hand):
        score = sum(CARDS[card]["score"] for card in hand)
        aces = sum(1 for card in hand if CARDS[card]["value"] == "A")

        while score > 21 and aces > 0:
            score -= 10
            aces -= 1

        return score

    def is_bust(self, hand):
        return self.calculate_score(hand) > 21

    def is_blackjack(self, hand):
        return len(hand) == 2 and self.calculate_score(hand) == 21

    def can_split(self, hand):
        if len(hand) != 2:
            return False
        first_value = CARDS[hand[0]]["value"]
        second_value = CARDS[hand[1]]["value"]
        return first_value == second_value

    def play_dealer_turn(self, dealer_hand, stand_on=17):
        while self.calculate_score(dealer_hand) < stand_on:
            self.hit(dealer_hand)
        return dealer_hand

    def resolve_round(self, player_hand, dealer_hand):
        player_score = self.calculate_score(player_hand)
        dealer_score = self.calculate_score(dealer_hand)

        if player_score > 21:
            return "lose"
        if dealer_score > 21:
            return "win"
        if dealer_score > player_score:
            return "lose"
        if dealer_score < player_score:
            return "win"
        return "draw"

    def display_cards(self, hand):
        for card in hand:
            print(CARD_ART[card])

    def display_in_game(self, hand):
        self.display_player_cards(hand)
        self.display_dealer_cards(hand, hide_second_card=True)

    def display_final_game(self, hand):
        self.display_player_cards(hand)
        self.display_dealer_cards(hand)

    def display_player_cards(self, hand):
        self.display_cards(hand["player_hand"])
        print(f"Player's hand: {hand['player_hand']}")
        print(f"Player's score: {self.calculate_score(hand['player_hand'])}")

    def display_dealer_cards(self, hand, hide_second_card=False):
        if hide_second_card:
            self.display_cards(hand["dealer_hand"][:1])
            print(HIDDEN_CARD)
            print(f"Dealer's score: {self.calculate_score(hand['dealer_hand'][:1])}")
            print(f"Dealer's hand: {hand['dealer_hand'][:1]}")
            return

        self.display_cards(hand["dealer_hand"])
        print(f"Dealer's hand: {hand['dealer_hand']}")
        print(f"Dealer's score: {self.calculate_score(hand['dealer_hand'])}")

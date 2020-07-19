class Card:

    def __init__(self, card_name="", card_effect=""):
        self.card_name = card_name
        self.card_effect = card_effect

    def __str__(self):
        return f'card_name={self.card_name}, card_effect={self.card_effect}'

    def __repr__(self):
        super()
        return f'card_name={self.card_name}'

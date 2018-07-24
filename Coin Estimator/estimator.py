import decimal

class Coin():
    # given weights in grams
    WEIGHTS = {
        'PENNY': 2.5,
        'NICKEL': 5.0,
        'DIME': 2.268,
        'QUARTER': 5.67
    }
    ROLL_COUNT = {
        'PENNY': 50,
        'NICKEL': 40,
        'DIME': 50,
        'QUARTER' : 40,
    }

    def __init__(self, coin_weight, coin_type):
        self.weight = coin_weight
        self.type = coin_type

    #def __repr__(self):
    #   return str(self.get_value())

    def get_roll(self):
        return self.get_value() // Coin.ROLL_COUNT.get(self.type, -1)

    def get_value(self):
        return self.weight // Coin.WEIGHTS.get(self.type, -1)

def estimator(given_weight, weight_unit_type, coin_type):
    weight = given_weight
    if weight_unit_type == 'p':
        weight = convert_units(given_weight, weight_unit_type)
    coin_collection = Coin(weight, coin_type)
    return coin_collection.get_value(), coin_collection.get_roll()


def convert_units(amount, unit_type):
    if amount < 0:
        raise ValueError("unable to convert negative units")
    if unit_type == 'p':
        return round(amount * 453.592, 6)
    return round(amount * 0.00220462, 6)



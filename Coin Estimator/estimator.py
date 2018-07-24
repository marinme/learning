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



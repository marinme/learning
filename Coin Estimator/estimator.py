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
    def __repr__(self):
        pass
    def get_roll(self):
        pass


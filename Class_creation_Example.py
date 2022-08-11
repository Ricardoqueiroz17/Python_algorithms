class Option:
    def __init__(self, asset, vol, expiry):
        self.asset = asset
        self.vol = vol
        self.expiry = expiry
    def show(self):
        print(f'Basic information about your option:\n \
Asset: {self.asset}\n \
Volatility: {self.vol}\n \
Expiration time (days): {self.expiry}\n')

class Strategy:
    def __init__(self, type, budget): #Here (__init-- is where it goes the info which you could declare directly while defining the instance with
                                      #the class Name, e.g.: c = Strategy("type", "budget")
        self.type = type
        self.budget = budget

    def show_info(self):
        print(f'Hello and welcome! The strategy that you are dealing is {self.type}!\n \
Also, your budget for this strategy is {self.budget} USD dolars!')

o = Option("KO", 0.25, 252)
print(o.asset)
print(o.vol)
print(o.expiry)

o.show()

s = Strategy("Straddle", 1500)
s.show_info()


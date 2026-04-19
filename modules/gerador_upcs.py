import random
random.seed(10)
def pressao():
        upc = random.randint(1,250)
        if upc > 150:
                upc *= 1.08
        else:
                upc *= 0.96
        return upc


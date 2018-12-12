class WrongAbbreviation(Exception):
    pass
class NegativePrice(Exception):
    pass
class ZeroError(Exception):
    pass



class objectprice():
    def __init__(self, name, price, prov):
        try:
            self.name = name
            self.price = price
            if isinstance(self.price,int)==True or isinstance(self.price,float)==True:
                if self.price<0:
                    raise NegativePrice()
            else:
                raise ValueError
            self.prov = prov
            if len(self.prov)>2:
                raise WrongAbbreviation()
        except ValueError:
            print("Please enter a number for price.")
        except WrongAbbreviation:
            print("Please enter the standard two letter abbreviation.")
        except NegativePrice:
            print("Please enter a positive price")

    def getprice(self):
        return calctax.tax(self)

class calctax():
    def __init__(self, name, price, prov):
        try:
            objectprice.__init__(self, name, price, prov)
            if self.price==0:
                raise ZeroError
        except ZeroError:
            print("The tax on a free item is free!")

    def tax(self):
        try:
            if self.prov == 'bc':
                return self.price*0.12 + self.price
            if self.prov == 'ab':
                return self.price*0.05 + self.price
            if self.prov == 'sk':
                return self.price*0.11 + self.price
            if self.prov == 'mb':
                return self.price*0.13 + self.price
            if self.prov == 'on':
                return self.price*0.13 + self.price
            if self.prov == 'qc':
                return self.price*0.14975 + self.price
            if self.prov == 'nb':
                return self.price*0.15 + self.price
            if self.prov == 'pe':
                return self.price*0.15 + self.price
            if self.prov == 'ns':
                return self.price*0.15 + self.price
            if self.prov == 'nl':
                return self.price*0.15 + self.price
            if self.prov == 'yt':
                return self.price*0.05 + self.price
            if self.prov == 'nt':
                return self.price*0.05 + self.price
            if self.prov == 'nu':
                return self.price*0.05 + self.price
        except TypeError:
            print("Cannot calculate tax on item without price.")

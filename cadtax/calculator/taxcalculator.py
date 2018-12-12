class objectprice():
    def __init__(self, name, price, prov):
        self.name = name
        self.price = price
        self.prov = prov

    def getprice(self):
        return calctax.tax(self)

class calctax():
    def __init__(self, name, price, prov):
            objectprice.__init__(self, name, price, prov)

    def tax(self):

        if self.prov == 'bc':
            return self.price*0.12 + self.price
        if self.prov == 'alb':
            return self.price*0.05 + self.price
        if self.prov == 'sas':
            return self.price*0.11 + self.price
        if self.prov == 'man':
            return self.price*0.13 + self.price
        if self.prov == 'ont':
            return self.price*0.13 + self.price
        if self.prov == 'que':
            return self.price*0.14975 + self.price
        if self.prov == 'nb':
            return self.price*0.15 + self.price
        if self.prov == 'pei':
            return self.price*0.15 + self.price
        if self.prov == 'ns':
            return self.price*0.15 + self.price
        if self.prov == 'nal':
            return self.price*0.15 + self.price
        if self.prov == 'yuk':
            return self.price*0.05 + self.price
        if self.prov == 'nwt':
            return self.price*0.05 + self.price
        if self.prov == 'nun':
            return self.price*0.05 + self.price

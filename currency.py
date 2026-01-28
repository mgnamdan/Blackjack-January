

class Convertor:

    _instance = None
    _initialized = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


    def __init__(self):
        if not self._initialized:
            self.rates_to_usd = {
                'USD': 1.0,
                'EUR': 1.09,
                'JPY': 0.0067,
                'GBP': 1.27,
                'CNY': 0.14,
                'CHF': 1.13,
                'CAD': 0.74
            }
            self._initialized = True


    def convert(self, amount, from_currency, to_currency):
        if from_currency not in self.rates_to_usd or to_currency not in self.rates_to_usd:
            raise ValueError("Unsupported currency for conversion.")
        amount_in_usd = amount * self.rates_to_usd[from_currency]
        return round(amount_in_usd / self.rates_to_usd[to_currency], 2)



class Currency:

    def __init__(self, amount, denom="USD"):
        self.amount = float(amount)
        self.denomination = denom.upper()
        self.helper = Convertor()


    def __str__(self):
        return f"Currency worth {self.amount} {self.denomination}"
    

    def __repr__(self):
        return f"Currency({self.amount}, {self.denomination})"
    

    def __add__(self, amt):
        if isinstance(amt, Currency):
            if self.denomination == amt.denomination:
                self.amount = self.amount + amt.amount
            else:
                self.amount = self.amount + self.helper.convert(amt, amt.denomination, self.denomination)
        elif isinstance(amt, int) or isinstance(amt, float):
            self.amount = self.amount + amt
        else:
            try:
                self.amount = self.amount + int(amt)
            except TypeError:
                print("Unsupported amount types for addition.")


    def __iadd__(self, amt):
        if isinstance(amt, Currency):
            if self.denomination == amt.denomination:
                self.amount = self.amount + amt.amount
            else:
                self.amount = self.amount + self.helper.convert(amt, amt.denomination, self.denomination)
        elif isinstance(amt, int) or isinstance(amt, float):
            self.amount = self.amount + amt
        else:
            try:
                self.amount = self.amount + int(amt)
            except TypeError:
                print("Unsupported amount types for addition.")
        return self.amount


    def __sub__(self, amt):
        if amt > self.amount:
            print("Cannot subtract more than currency value.")
            return
        if isinstance(amt, Currency):
            if self.denomination == amt.denomination:
                self.amount = self.amount - amt
            else:
                self.amount = self.amount - self.helper.convert(amt, amt.denomination, self.denomination)
        elif isinstance(amt, int) or isinstance(amt, float):
            self.amount = self.amount - amt
        else:
            try:
                self.amount = self.amount - int(amt)
            except TypeError:
                print("Unsupported amount types for subtraction.")


    def __isub__(self, amt):
        if amt > self.amount:
            print("Cannot subtract more than currency value.")
            return
        if isinstance(amt, Currency):
            if self.denomination == amt.denomination:
                self.amount = self.amount - amt
            else:
                self.amount = self.amount - self.helper.convert(amt, amt.denomination, self.denomination)
        elif isinstance(amt, int) or isinstance(amt, float):
            self.amount = self.amount - amt
        else:
            try:
                self.amount = self.amount - int(amt)
            except TypeError:
                print("Unsupported amount types for subtraction.")


    def __mul__(self, scalar):
        if isinstance(scalar, int) or isinstance(scalar, float):
            self.amount = self.amount * scalar
        else:
            try:
                self.amount = self.amount * int(scalar)
            except TypeError:
                print("Unsupported scalar type.")


    def __imul__(self, scalar):
        if isinstance(scalar, int) or isinstance(scalar, float):
            self.amount = self.amount * scalar
        else:
            try:
                self.amount = self.amount * int(scalar)
            except TypeError:
                print("Unsupported scalar type.")


    def __truediv__(self, dividend):
        if dividend == 0:
            print("Cannot divide by zero.")
            return
        if isinstance(dividend, int) or isinstance(dividend, float):
            self.amount = self.amount / dividend
        else:
            try:
                self.amount = self.amount / int(dividend)
            except TypeError:
                print("Unsupported dividend type.")


    def __itruediv__(self, dividend):
        if dividend == 0:
            print("Cannot divide by zero.")
            return
        if isinstance(dividend, int) or isinstance(dividend, float):
            self.amount = self.amount / dividend
        else:
            try:
                self.amount = self.amount / int(dividend)
            except TypeError:
                print("Unsupported dividend type.")


    def __floordiv__(self, dividend):
        if dividend == 0:
            print("Cannot divide by zero.")
            return
        if isinstance(dividend, int) or isinstance(dividend, float):
            self.amount = self.amount // dividend
        else:
            try:
                self.amount = self.amount // int(dividend)
            except TypeError:
                print("Unsupported dividend type.")


    def __ifloordiv__(self, dividend):
        if dividend == 0:
            print("Cannot divide by zero.")
            return
        if isinstance(dividend, int) or isinstance(dividend, float):
            self.amount = self.amount // dividend
        else:
            try:
                self.amount = self.amount // int(dividend)
            except TypeError:
                print("Unsupported dividend type.")


    def __round__(self):
        if isinstance(self.amount, float):
            if self.amount % 1 >= 0.5:
                self.amount = int(self.amount) + 1
            else:
                self.amount = int(self.amount)


    def __eq__(self, other):
        if isinstance(other, Currency):
            if self.denomination == other.denomination:
                return self.amount == other.amount
            else:
                return self.helper.convert(self.amount, self.denomination,other.denomination) == other.amount
        else:
            try:
                return self.amount == other
            except TypeError:
                print("Unsupported quantities for comparison.")
                return False


    def __lt__(self, other):
        if isinstance(other, Currency):
            if self.denomination == other.denomination:
                return self.amount < other.amount
            else:
                return self.helper.convert(self.amount, self.denomination,other.denomination) < other.amount
        else:
            try:
                return self.amount < other
            except TypeError:
                print("Unsupported quantities for comparison.")
                return False


    def __gt__(self, other):
        if isinstance(other, Currency):
            if self.denomination == other.denomination:
                return self.amount > other.amount
            else:
                return self.helper.convert(self.amount, self.denomination,other.denomination) > other.amount
        else:
            try:
                return self.amount > other
            except TypeError:
                print("Unsupported quantities for comparison.")
                return False


    def __le__(self, other):
        return self.__lt__(self, other) and self.__eq__(self.other)


    def __ge__(self, other):
        return self.__gt__(self, other) and self.__eq__(self.other)
    

    def set_amount(self, amt):
        self.amount = float(amt)


    def convert(self, new_denom):
        self.amount = self.helper.convert(self.amount, self.denomination, new_denom)
        self.denomination = new_denom

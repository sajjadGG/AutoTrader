class EMA3Cross(Strategy):
    n1 = 9
    n2 = 3
    n3 = 3

    def init(self):
        self.ema1 = self.I(ti.ema, self.data.Close, self.n1)
        self.ema2 = self.I(ti.ema, self.data.Low, self.n2)
        self.ema3 = self.I(ti.ema, self.data.High, self.n3)

    def next(self):

        if not self.position:
            if crossover(self.data.Close, self.ema1):
                self.buy()

        else:
            if (
                self.position.is_long
                and crossover(self.ema3, self.data.Close)
                or self.position.is_short
                and crossover(self.data.Close, self.ema2)
            ):

                self.position.close()

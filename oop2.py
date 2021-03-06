class Player:
    MAX_POSITION = 10

    def __init__(self):
        self.position = 0

        def move(self, steps):
            if self.position + steps < Player.MAX_POSITION:
                self.position = self.position + steps
            else:
                self.position = Player.MAX_POSITION

        # This method provides a rudimentary visualization in the console
        def draw(self):
            drawing = "-" * self.position + "|" + "-" * (Player.MAX_POSITION - self.position)
            print(drawing)

######
from datetime import datetime


class BetterDate:
    def __init__(self, year, month, day):
        self.year, self.month, self.day = year, month, day

    @classmethod
    def from_str(cls, datestr):
        year, month, day = map(int, datestr.split("-"))
        return cls(year, month, day)

    @classmethod
    def from_datetime(cls, dateobj):
        year, month, day = dateobj.year, dateobj.month, dateobj.day
        return cls(year, month, day)


today = datetime.today()
bd = BetterDate.from_datetime(today)
print(bd.year)
print(bd.month)
print(bd.day)




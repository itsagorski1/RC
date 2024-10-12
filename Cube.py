import Side as S

class Cube:
    def __init__(self):
        global S1, S2, S3, S4, S5, S6
        S1 = S.Side("red")
        S2 = S.Side("blue")
        S3 = S.Side("white")
        S4 = S.Side("orange")
        S5 = S.Side("green")
        S6 = S.Side("yellow")

    def ReadNotation(self):
        pass

    def side_input(self):
        side_input = input('How do you want to rotate the cube (it has to be in rubick\'s cube notation) ?')
        ReadNotation(side_input)

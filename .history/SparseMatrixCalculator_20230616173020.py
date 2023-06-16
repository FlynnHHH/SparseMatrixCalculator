class Triple:
    def __init__(self, i, j, e):
        self.i = i
        self.j = j
        self.e = e
    
    def __str__(self):
        return str(self.i) + " " + str(self.j) + " " + str(self.e)

class RLSMatrix:
    def __init__(self, data, rpos, mu, nu, tu):
        self
    def create(self):




row1, col1 = map(int, input().split())
row2, col2 = map(int, input().split())
if row1 <= 0 or row1 > 20 or col1 <= 0 or col1 > 20 or row2 <= 0 or row2 > 20 or col2 <= 0 or col2 > 20:
    print("ERROR")
else:
    
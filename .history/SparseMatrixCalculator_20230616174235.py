class Triple:
    def __init__(self, i, j, e):
        self.i = i
        self.j = j
        self.e = e
    
    def __str__(self):
        return str(self.i) + " " + str(self.j) + " " + str(self.e)

class RLSMatrix:
    def __init__(self, data, mu, nu, tu):
        self.data = data
        self.rpos = None
        self.mu = mu
        self.nu = nu
        self.tu = tu
    
    def creatematrix(self, data, mu, nu, tu):
        mu, nu, tu = map(int, input("").split())
        self.data = data
        self.mu = mu
        self.nu = nu
        self.tu = tu
        self.rpos = [0 for i in range(nu)]
        for i in range(tu):
            self.rpos[data[i].j] += 1
        for i in range(1, nu):
            self.rpos[i] += self.rpos[i - 1]
        
        




row1, col1 = map(int, input().split())
row2, col2 = map(int, input().split())
if row1 <= 0 or row1 > 20 or col1 <= 0 or col1 > 20 or row2 <= 0 or row2 > 20 or col2 <= 0 or col2 > 20:
    print("ERROR")
else:
    
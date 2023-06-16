class Triple:
    def __init__(self, i, j, e):
        self.i = i
        self.j = j
        self.e = e

class RLSMatrix:
    def __init__(self, data, mu, nu, tu):
        self.data = data
        self.rpos = None
        self.mu = mu
        self.nu = nu
        self.tu = tu
    
    def CreateSMatrix(self):
        mu, nu, tu = map(int, input("请输入矩阵的行数、列数、非零元的个数，用空格间隔").split())
        if mu <= 0 or mu > 20 or nu <= 0 or nu > 20 or tu <= 0 or tu > mu * nu:
            print("ERROR")
            return
        print("请按行主序输入矩阵的非零元素，每行输入一个元素的行号、列号、元素值，用空格间隔\n行号、列号从1开始计数\n")
        self.data =  [0 for i in range(tu)]
        for i in range(tu):
            tri = Triple(int(input().split(), int(input().split(), int(input().split()))))
            self.data.append([tri.i, tri.j, tri.e])
        self.mu = mu
        self.nu = nu
        self.tu = tu
        self.rpos = [0 for i in range(mu)]
        for i in range(tu):
        for i in range(tu):
            self.rpos[self.data[i].j] += 1
        for i in range(1, nu):
            self.rpos[i] += self.rpos[i - 1]
        
        




row1, col1 = map(int, input().split())
row2, col2 = map(int, input().split())
if row1 <= 0 or row1 > 20 or col1 <= 0 or col1 > 20 or row2 <= 0 or row2 > 20 or col2 <= 0 or col2 > 20:
    print("ERROR")

    
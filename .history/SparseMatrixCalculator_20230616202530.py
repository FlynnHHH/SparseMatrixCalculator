class Triple:
    def __init__(self, i, j, e):
        self.i = i # 行号
        self.j = j # 列号
        self.e = e # 元素值

class RLSMatrix:
    def __init__(self, data, mu, nu, tu):
        self.data = data # 三元组表
        self.rpos = None # 矩阵中每一行第一个非零元在三元组表中的位置
        self.mu = mu     # 矩阵的行数
        self.nu = nu     # 矩阵的列数
        self.tu = tu     # 矩阵的非零元个数
    def CreateSMatrix(self):
        # 
        mu, nu, tu = map(int, input("请输入矩阵的行数、列数、非零元的个数，用空格间隔").split())
        if mu <= 0 or mu > 20 or nu <= 0 or nu > 20 or tu <= 0 or tu > mu * nu:
            print("ERROR")
            return
        print("请按行主序输入矩阵的非零元素，每行输入一个元素的行号、列号、元素值，用空格间隔\n行号、列号从1开始计数\n")
        self.data =  [[0 , 0 , 0]]
        for index in range(tu):
            tri = Triple(int(input().split(), int(input().split(), int(input().split()))))
            self.data.append([tri.i, tri.j, tri.e])
        self.mu = mu
        self.nu = nu
        self.tu = tu
        self.rpos = [0 for i in range(mu)]
        num = [0 for index in range(mu)]
        for t in range(mu):
            ++num[self.data[t + 1].i] # 求矩阵中每一行非零元的个数
        self.rpos[1] = 1
        for index in range(2, nu + 1):
            self.rpos[index] = self.rpos[index - 1] + num[index - 1]
        return self
    def PrintSMatrix(self):
        # 以行列式形式输出矩阵
        for row in range(1, self.mu + 1):
            for col in range(1, self.nu + 1):
                if row == self.data[self.rpos[row]].i and col == self.data[self.rpos[row]].j:
                    print(self.data[self.rpos[row]].e, end = " ")
                    ++self.rpos[row]
                else:
                    print(0, end = " ")
            print("\n")
        
        
        




row1, col1 = map(int, input().split())
row2, col2 = map(int, input().split())
if row1 <= 0 or row1 > 20 or col1 <= 0 or col1 > 20 or row2 <= 0 or row2 > 20 or col2 <= 0 or col2 > 20:
    print("ERROR")

    
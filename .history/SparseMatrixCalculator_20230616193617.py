class RLSMatrix:
    def __init__(self, data, mu, nu, tu):
        self.data = data
        self.rpos = None
        self.mu = mu
        self.nu = nu
        self.tu = tu
    
    def CreateSMatrix(self, data, mu, nu, tu):
        
        self.mu = mu
        self.nu = nu
        self.tu = tu
        self.rpos = [0 for i in range(nu)]
        for i in range(tu):
            self.rpos[data[i].j] += 1
        for i in range(1, nu):
            self.rpos[i] += self.rpos[i - 1]
        
        



mu_M, nu_M, tu_M = map(int, input("创建矩阵M:\n请输入矩阵的行数、列数、非零元的个数，用空格间隔").split())
print("请按行主序输入矩阵的非零元素，每行输入一个元素的行号、列号、元素值，用空格间隔\n行号、列号从1开始计数\n")
data_M =  [0 for i in range(tu_M)]
for i in range(tu_M):
    data_M.append(list(int(input().split())))
M = RLSMatrix(data_M, mu_M, nu_M, tu_M)
M.CreateSMatrix(data_M, mu_M, nu_M, tu)

    
class Triple:
    def __init__(self, i, j, e):
        self.i = i  # 行号
        self.j = j  # 列号
        self.e = e  # 元素值


class RLSMatrix:
    def __init__(self, data, mu, nu, tu):
        self.data = data  # 三元组表
        self.rpos = []  # 矩阵中每一行第一个非零元在三元组表中的位置
        self.mu = mu      # 矩阵的行数
        self.nu = nu      # 矩阵的列数
        self.tu = tu      # 矩阵的非零元个数

    def CreateSMatrix(self):
        # 以三元组表形式输入矩阵
        mu, nu, tu = map(int, input("请输入矩阵的行数、列数、非零元的个数，用空格间隔\n").split())
        if mu <= 0 or mu > 20 or nu <= 0 or nu > 20 or tu < 0 or tu > mu * nu:
            print("ERROR")
            return
        print("请按行主序输入矩阵的非零元素，每行输入一个元素的行号、列号、元素值，用空格间隔\n行号、列号从1开始计数")
        self.data = [[0, 0, 0]]
        for index in range(tu):
            i, j, e = map(int, input().split())
            tri = Triple(i, j, e)
            self.data.append(tri)
        self.mu = mu
        self.nu = nu
        self.tu = tu
        self.rpos = [0 for index in range(mu + 1)]
        num = [0 for index in range(mu + 1)]
        for t in range(tu):
            num[self.data[t + 1].i] = num[self.data[t + 1].i] + 1  # 求矩阵中每一行非零元的个数
        self.rpos[1] = 1
        for index in range(2, mu + 1):
            self.rpos[index] = self.rpos[index - 1] + num[index - 1]
        return self

    def Getrpos(self):
        self.rpos = [0 for index in range(self.mu + 1)]
        num = [0 for index in range(self.mu + 1)]
        for t in range(self.tu):
            num[self.data[t + 1].i] = num[self.data[t + 1].i] + 1  # 求矩阵中每一行非零元的个数
        self.rpos[1] = 1
        for index in range(2, self.mu + 1):
            self.rpos[index] = self.rpos[index - 1] + num[index - 1]
        return self.rpos

    def PrintSMatrix(self):
        # 以行列式形式输出矩阵
        k = 1
        for row in range(1, self.mu + 1):
            print('[', end=" ")
            for col in range(1, self.nu + 1):
                if k <= self.tu and row == self.data[k].i and col == self.data[k].j:
                    print(self.data[k].e, end=" ")
                    k = k + 1
                else:
                    print(0, end=" ")
            print(']')


def AddSMatrix(A, B):
    if A.mu != B.mu or A.nu != B.nu:
        print("ERROR")
        return
    C = RLSMatrix(None, A.mu, A.nu, 0)
    C.data = A.data
    C.tu = A.tu  # C的三元组表先置为A的三元组表
    for index in range(1, B.tu + 1):
        flag = 0
        for k in range(1, A.tu + 1):
            if A.data[k].i == B.data[index].i and A.data[k].j == B.data[index].j:
                C.data[k].e = C.data[k].e + B.data[index].e
                flag = 1  # B中当前元素在A中找到了相同位置的元素
                break
        if flag == 0:  # B中当前元素在A中没有找到相同位置的元素
            C.data.append(B.data[index])
            C.tu = C.tu + 1
    C.rpos = C.Getrpos()
    return C


def SubSMatrix(A, B):
    if A.mu != B.mu or A.nu != B.nu:
        print("ERROR")
        return
    C = RLSMatrix(None, A.mu, A.nu, 0)
    oppoB = RLSMatrix(None, B.mu, B.nu, B.tu)
    for index in range(1, B.tu + 1):  # B中每个元素取相反数
        oppoB.data[index].i = B.data[index].i
        oppoB.data[index].j = B.data[index].j
        oppoB.data[index].e = (-1) * B.data[index].e
    C = AddSMatrix(A, oppoB)
    C.rpos = C.Getrpos()
    return C


def MulSMatrix(A, B):
    if A.nu != B.mu:
        print("ERROR")
        return
    C = RLSMatrix(None, A.mu, B.nu, 0)
    C.data = [[0, 0, 0]]
    for arow in range(1, A.mu + 1):
        ctemp = [0 for i in range(B.nu + 1)]  # 当前行各元素累加器
        if arow < A.mu:
            tp = A.rpos[arow + 1]
        else:
            tp = A.tu + 1
        for p in range(A.rpos[arow], tp):  # 对当前行的每一个非零元素
            brow = A.data[p].j  # 找到当前元素在B中的行号
            if brow < B.mu:
                t = B.rpos[brow + 1]
            else:
                t = B.tu + 1
            for q in range(B.rpos[brow], t): 
                ccol = B.data[q].j  # 乘积在C中的列号
                ctemp[ccol] += A.data[p].e * B.data[q].e
        for ccol in range(1, B.nu + 1):
            if ctemp[ccol] != 0:
                tri = Triple(arow, ccol, ctemp[ccol])
                C.data.append(tri)
                C.tu = C.tu + 1
    C.rpos = C.Getrpos()
    return C


mode = int(input("请选择计算类型：\n1.加法\n2.减法\n3.乘法\n"))
print("请输入矩阵A：")
A = RLSMatrix(None, 0, 0, 0)
A.CreateSMatrix()
print("请输入矩阵B：")
B = RLSMatrix(None, 0, 0, 0)
B.CreateSMatrix()
print("运算结果为")
if mode == 1:
    print("A+B=")
    AddSMatrix(A, B).PrintSMatrix()
elif mode == 2:
    print("A-B=")
    SubSMatrix(A, B).PrintSMatrix()
elif mode == 3:
    print("A*B=")
    MulSMatrix(A, B).PrintSMatrix()
else:
    print("ERROR")

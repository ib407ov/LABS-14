import math
class TPrism:
    def __init__(self, _a, _n, _h):
        self.a = _a
        self.n = _n
        self.h = _h

    @property
    def V_Prism(self):
        return (1/4 * self.n * math.pow(self.a, 2) * ((math.cos(math.pi / 4)) / math.sin(math.pi / 4)) * self.h)

    @property
    def S_Prism(self):
        S_osnova = (1/4 * self.n * math.pow(self.a, 2) * ((math.cos(math.pi / 4)) / math.sin(math.pi / 4)))
        S_bicna = self.n * self.h * self.a
        return (S_osnova + S_bicna)

class TPrism3(TPrism):
    def __init__(self, _a, _n, _h, _m):
        self.m = _m
        super(TPrism3, self).__init__(_a, _n, _h)

    @property
    def Sum_V(self):
        A = []
        A.append(super().V_Prism)
        for i in range(1, self.m):
            A.append(super().V_Prism * 5 * i)
        return sum(A)

class TPrsm4(TPrism):
    def __init__(self, _a, _n, _h, _m):
        self.m = _m
        super().__init__(_a, _n, _h)

    @property
    def Sum_S(self):
        A = []
        A.append(super().S_Prism)
        for i in range(1, self.m):
            A.append(super().S_Prism * 5 * i)
        return sum(A)

# def input():
#     n = int(input("Enter sides : "))
#     a = int(input("Enter angles : "))
#     h = int(input("Enter height : "))
#     m = int(input('Number prisms : '))
#     return a,n,h,m

print("Create Prism\n")

print('You can find the sum V and S prisms,\n'
      'but each prism increases V or S on 5\n'
      'number of prism enter you\n')

while True:
    choise = int(input('1. Sum V prisms\n'
                       '2. Sum S prism\n'
                       '3. Out\n'
                       'Write nuber : '))
    if choise == 1:
        n = int(input("Enter sides : "))
        a = int(input("Enter angles : "))
        h = int(input("Enter height : "))
        m = int(input('Number prisms : '))
        v = TPrism3(a, n, h, m)
        print(v.Sum_V, '\n')

    elif choise == 2:
        n = int(input("Enter sides : "))
        a = int(input("Enter angles : "))
        h = int(input("Enter height : "))
        m = int(input('Number prisms : '))
        s = TPrsm4(a, n, h, m)
        print(s.Sum_S, '\n')

    else:
        break

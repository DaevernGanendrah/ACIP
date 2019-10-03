class Matrix:
    def __init__(self,r,c,*items):
        assert isinstance(r,int)
        assert isinstance(c,int)
        assert r>0
        assert c>0
        assert (len(items)==0) or ((r*c)==len(items))
        self.cells = [[0 for col in range(c)] for row in range(r)]
        if len(items)!=0:
            for i in range(len(items)):
                self.cells[i // c][i % c] = items[i]

    def __getattr__(self, attr):
        if (attr=="NRows"):
            return len(self.cells)
        elif (attr=="NCols"):
            return len(self.cells[0])

    def Show(self):
        for r in range(self.NRows):
            for c in range(self.NCols):
                print("{}".format(self.cells[r][c]), end="\t")
            print()

    #def Multyply(self,rhs):
    def __mul__(self,rhs):
        if (self.NCols!=rhs.NRows):
            raise Exception("Cannot multiply-lah!")

        m = Matrix(self.NRows,rhs.NCols)
        for r in range(m.NRows):
            for c in range(m.NCols):
                for i in range(self.NCols):
                    m.cells[r][c] += self.cells[r][i] * rhs.cells[i][c]
        return m

    #def Add(self,rhs):
    def __add__(self, rhs):
        if (self.NRows!=rhs.NRows):
            raise Exception("No of Rows must be the same!")
        if (self.NCols!=rhs.NCols):
            raise Exception("No of Cols must be the same!")

        m = Matrix(self.NRows,self.NCols)
        for r in range(m.NRows):
            for c in range(m.NCols):
                m.cells[r][c] = self.cells[r][c] + rhs.cells[r][c]
        return m

    #def Transpose(self):
    def __invert__(self):
        m = Matrix(self.NCols,self.NRows)
        for r in range(m.NRows):
            for c in range(m.NCols):
                m.cells[r][c] = self.cells[c][r]
        return m

    def __getitem__(self, r):
        return self.cells[r]

    def __setitem__(self, r, c, value):
        self.cells[r][c] = float(value)
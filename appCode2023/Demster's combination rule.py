import pandas as pd
import numpy as np

#Đọc dữ liệu từ file csv
data = pd.read_csv('../dataSet/processData.csv', usecols=['m(a)', 'm(b)', 'm(c)', 'm(a,b)', 'm(a,c)', 'm(b,c)', 'm(a,b,c)'])
#Lấy dữ liệu    
A = data.iloc[0:13,0].to_numpy()
B = data.iloc[0:13,1].to_numpy()
C = data.iloc[0:13,2].to_numpy()
AB = data.iloc[0:13,3].to_numpy()
AC = data.iloc[0:13,4].to_numpy()
BC = data.iloc[0:13,5].to_numpy()
ABC = data.iloc[0:13,6].to_numpy()


N = 3
def mBase(N):
    mbase = 1/(pow(2,N)-1)
    return round(mbase, 4)

def X_base(X):
    xBase = []
    for i in range(0, len(X)-1):
        xBase.append(round((X[i] + mBase(N))/2,4))
    return xBase;

A_base = X_base(A)
B_base = X_base(B)
C_base = X_base(C)
AB_base = X_base(AB)
AC_base = X_base(AC)
BC_base = X_base(BC)
ABC_base = X_base(ABC)

m = np.array([A_base,B_base,C_base,AB_base,AC_base,BC_base,ABC_base]).T
masses = m.flatten()
print(masses)
def demster_k(masses):
    n = len(masses)
    if n == 1:
        k = 1.0
    else:
        M = np.zeros((n, n))
        for i in range(n):
            M[i, i] = masses[i]
            for j in range(i + 1, n):
                M[i, j] = M[i, j - 1] + masses[j]
        for i in range(n):
            if M[i, -1] == 0:
                M[i, -1] = 1
            M[i, :] /= M[i, -1]
        k = np.max(M[:-1, -1])
    return k

print(demster_k(masses))



import csv

class m:
    def __init__(self):
        self.abc = 0
        self.ab = 0
        self.ac = 0
        self.a = 0
        self.bc = 0
        self.b = 0
        self.c = 0

m_list = []
for i in range(10):
    m_i = m()
    with open(f'm{i+1}.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader) # skip header
        row = next(reader)
        m_i.abc = float(row[0])
        m_i.ab = float(row[1])
        m_i.ac = float(row[2])
        m_i.a = float(row[3])
        m_i.bc = float(row[4])
        m_i.b = float(row[5])
        m_i.c = float(row[6])
    m_list.append(m_i)

result = m()
for m_i in m_list:
    result.abc += m_i.abc
    result.ab += (m_i.abc * m_i.ab + m_i.ab * m_i.bc + m_i.ab * m_i.ac + m_i.ab * m_i.ab + m_i.a * m_i.bc + m_i.a * m_i.ac + m_i.b * m_i.ac)
    result.ac += (m_i.abc * m_i.ac + m_i.ac * m_i.bc + m_i.ac * m_i.ac + m_i.a * m_i.bc + m_i.b * m_i.ab + m_i.b * m_i.ac)
    result.a += (m_i.abc * m_i.a + m_i.a * m_i.bc + m_i.a * m_i.ac + m_i.a * m_i.ab)
    result.bc += (m_i.abc * m_i.bc + m_i.bc * m_i.bc + m_i.b * m_i.ac + m_i.b * m_i.bc + m_i.a * m_i.bc)
    result.b += (m_i.abc * m_i.b + m_i.b * m_i.bc + m_i.b * m_i.ab + m_i.a * m_i.bc + m_i.b * m_i.bc)
    result.c += (m_i.abc * m_i.c + m_i.c * m_i.bc + m_i.c * m_i.ac)



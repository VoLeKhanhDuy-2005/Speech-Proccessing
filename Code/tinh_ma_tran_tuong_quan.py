import numpy as np

f = open("mix_01.txt", "rt")
data = f.read()
f.close()
data = data.split()
x1 = []
for value in data:
    x1.append(int(value)/32768) #/32768 để chuẩn hóa
    
f = open("mix_02.txt", "rt")
data = f.read()
f.close()
data = data.split()
x2 = []
for value in data:
    x2.append(int(value)/32768)
    
n = len(x2)
C11 = 0.0
C12 = 0.0
C21 = 0.0
C22 = 0.0
for i in range(0, n):
    C11 += x1[i]*x1[i]
    C12 += x1[i]*x2[i]
    C21 += x2[i]*x1[i]
    C22 += x2[i]*x2[i]
C11 /= n # tính kỳ vọng (expect - trung bình) 
C12 /= n
C21 /= n
C22 /= n
print("C = ")
print(C11, C12)
print(C21, C22)

V11 = abs(C11) ** (1/2)
V12 = abs(C12) ** (1/2)
V21 = abs(C21) ** (1/2)
V22 = abs(C22) ** (1/2) # ok
V = np.array([[C11, C12], [C21, C22]])
V = np.linalg.inv(V)
V **= (1/2)

V11 = V[0,0]
V12 = V[0,1]
V21 = V[1,0]
V22 = V[1,1]

print("V = ")
print(V11, V12)
print(V21, V22)
    
y1 = []
y2 = []
for i in range(0, n):
    y1.append(V11*x1[i] + V12*x2[i]) #y = Vx
    y2.append(V21*x1[i] + V22*x2[i])

C11 = 0.0
C12 = 0.0
C21 = 0.0
C22 = 0.0
for i in range(0, n):
    C11 += y1[i]*y1[i]
    C12 += y1[i]*y2[i]
    C21 += y2[i]*y1[i]
    C22 += y2[i]*y2[i]
C11 /= n # tính kỳ vọng (expect - trung bình) 
C12 /= n   
C21 /= n
C22 /= n
print("C_y = ")
print(C11, C12)
print(C21, C22)

pass


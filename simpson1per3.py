a = float(input("Masukkan Nilai a : " ))
b = float(input("Masukkan Nilai b : "))
segment = float(input("Masukkan Jumlah Segment : "))
h = (b-a)/segment
xd = []
data = []
f = a
xd.append(f)
for i in range(3):
    f += h
    xd.append(f)
xd.append(b)
print("Setiap Nilai X : ",xd)
j = lambda x : (((1/4)*-9.1688*10**-6)*(x**4))+((1/3)*2.7961*(10**-3)*(x**3))-((1/2)*2.8487*(10**-1)*(x**2))+(9.6778*x)
g = lambda x: ((-9.1688*10**-6)*(x**3))+(2.7961*(10**-3)*(x**2))-(2.8487*(10**-1)*(x))+9.6778
for x in range(len(xd)):
    if xd[x] >123131:
        data.append(0)
    elif  xd[x]<=172:
        data.append(g(xd[x]))
    elif xd[x] > 172 and xd[x]<200:
        data.append(0)
print("Setiap Nilai F(Xi) : ",data)
result = (b-a)/(3*4)*(data[0]+(4*data[1]+4*data[3])+(2*data[2])+data[4])
print("Hasil Perhitungan Simpson : ",result)
print("Hasil Perhitungan Integral Manual : ",j(b)-j(a))
print("Error Et : ", ((j(b)-j(a))-result))
print("Error Absolute : ",(((j(b)-j(a))-result)/(j(b)-j(a)))*100,"%")
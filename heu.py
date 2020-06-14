import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
pers = lambda x : (10*x**4)-(2*x**3)+(4*x**2)-(2*x)+4
persintegral = lambda x : (1/5*(10*x**5))-(1/4*(2*x**4))+(1/3*(4*x**3))-(1/2*(2*x**2))+4*x + 1
# pers = lambda x : -(2*x**3)+(12*x**2)-(20*x)+8.5
# persintegral = lambda x : -(1/4*2*x**4)+(1/3*12*x**3)-(1/2*20*x**2)+8.5*x+1
x_awal = 0
x_akhir = 10
interval = 1
a1 =1/2
a2=1/2
p1 =1
q11 = 1

tag = 0
fi=[[0,1]]
ki = [[]]
result_integral = []
result = []
err = [0]
cek=0
for i in range(int(x_akhir/interval)+1):
    if i is not 0:
        cek +=interval
        print("------------------------------------------------------------------")
        print("Untuk x = ",cek)
        yi = pers(fi[i-1][0])
        k1= pers(fi[i-1][0])
        k2= pers(fi[i-1][0]+(p1*interval))
        ki.append([k1,k2])
        y = fi[i-1][1]+((a1*k1)+(a2*k2))*interval
        fi.append([cek,y])
        print(f"k1 =  (10*({fi[i-1][0]})**4)-(2*({fi[i-1][0]})**3)+(4*({fi[i-1][0]})**2)-(2*({fi[i-1][0]}))+4 = {k1}")
        print(f"x + (p1*h) = {fi[i-1][0]+(p1*interval)}")
        print(f"k2 = (10*({fi[i-1][0]+(p1*interval)})**4)-(2*({fi[i-1][0]+(p1*interval)})**3)+(4*({fi[i-1][0]+(p1*interval)})**2)-(2*({fi[i-2][0]+(p1*interval)}))+4 = {k2}")
        print(f"y({cek}) = {fi[i-1][1]} + ({(a1*k1)} + {(a2*k2)}) x {interval} = {y}")
        print(f"Hasil Integrasi Manual (y true) : {persintegral(fi[i][0])}")
        print(f"Error Relative = |{(abs((persintegral(fi[i][0])-y)/persintegral(fi[i][0]))*100)}| %")
        
        print()
        err.append(((persintegral(fi[i][0])-y)/persintegral(fi[i][0]))*100)
        result_integral.append(persintegral(fi[i][0]))
print(result_integral)
print(fi)
xp = [fi[i][0] for i in range(len(fi))]
yp = [fi[i][1] for i in range(len(fi))]
fig, ax = plt.subplots()
ax.plot(xp,yp, linestyle='--')

ax.set(ylabel = 'Sumbut y',xlabel = 'Sumbu x')
plt.show()
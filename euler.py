pers = lambda x : (10*x**4)-(2*x**3)+(4*x**2)-(2*x)+4
persintegral = lambda x : (1/5*(10*x**5))-(1/4*(2*x**4))+(1/3*(4*x**3))-(1/2*(2*x**2))+4*x + 1
x_akhir = 10
interval = 1
tag = 0
fi=[[0,1]]
result_integral = []
result = []
err = [0]

for i in range(int(x_akhir/interval)+1):
    if i is not 0 :
        print("------------------------------------------------------------------")
        print("Untuk x = ",i)
        f = fi[i-1][1]+(pers(fi[i-1][0])*interval)
        fi.append([i,f])
        print(f"f({fi[i-1][0]},{fi[i-1][1]}) = (10*({fi[i-1][0]})**4)-(2*({fi[i-1][0]})**3)+(4*({fi[i-1][0]})**2)-(2*({fi[i-1][0]}))+4 = {pers(fi[i-1][0])}")
        print(f"y({i}) = {fi[i-1][1]} + {pers(fi[i-1][0])} x {interval} = {f}")
        print(f"Hasil Integrasi Manual (y true) : {persintegral(fi[i][0])}")
        print(f"Error Relative = |{(persintegral(fi[i][0])-f)/persintegral(fi[i][0])*100}| %")
        
        print()
        err.append(((persintegral(fi[i][0])-f)/persintegral(fi[i][0]))*100)
        result_integral.append(persintegral(fi[i-1][0]))
    
        
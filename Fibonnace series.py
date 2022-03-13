N = int(input("How many fibonance series do you want: "))
fs = [0,1]

for a in range(2,N):
    d = fs[a-1] + fs[a-2]
    fs.append(d)
print(fs)
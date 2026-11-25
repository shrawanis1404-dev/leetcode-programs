arr=[-4,-2,1,0,-2,1,3,-4]
freq=[9]*0
for i in arr:
    freq[i+4]+=1
for i in range(len(freq)):
    print(f"{i-4}  occurs {freq[i]} times")
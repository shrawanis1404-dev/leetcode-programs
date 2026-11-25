arr=[100,101,102,100,101,103]
freq=[0]*4
for i in arr:
    freq[i-100]+=1
for i in range(len(freq)):
    print(f"{i+100 } occurs {freq[i]} times")
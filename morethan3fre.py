n=int(input("enter any number"))
freq=[0]*10

while n!=0:
    last=n%10
    freq[last]+=1
    n//=10
for i in range(len(freq)):
    if freq[i]>=3:
        print(i)
    

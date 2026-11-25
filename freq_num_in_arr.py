def frequency(arr):
    freq={}
    for i in arr:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    return freq
arr=[100,101,100,102,101,100]
print(frequency(arr))
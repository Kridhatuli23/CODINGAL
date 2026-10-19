dic={"Codingal":1,"is":2, "best":1,"for":1,"coding":1,}
print("The original dictionary is:",dic)
K=1
res=0
for i in dic:
    if dic[i]==K:
        res=res+1
print("Frequency of K is:", res)
def palind(r):
    e=len(r)-1
    s=0
    while(s<e):
        if(r[s]!=r[e]):
            return False
        s+=1
        e-=1
    return True
r=(67,98,45,45,98,67)
if(palind(r)):
    print("The tuple is flip-flop")
else:
    print("The tuple is not filp-flop")
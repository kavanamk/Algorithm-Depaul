def gcd(x, y):
    if x==y:
        return x
    elif x>y:
        return gcd(x-y,y)
    return gcd(x,y-x)

def gcdTable(x,y):
    if y==0:
        print(str(x)+" "+str(y))
        return x
    elif x>y:
        print(str(x)+" "+str(y)+" "+str(x%y))
        return gcdTable(y,x%y)
    else:
        print(str(x)+" "+str(y)+" "+str(y%x))
        return gcdTable(x,y%x)
    
gcdTable(12345, 135  )

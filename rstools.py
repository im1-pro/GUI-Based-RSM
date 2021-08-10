import re
def mul(a,b):
    c = []
    q = len(a)
    q1 = len(a[0])
    w = len(b)
    w1 = len(b[0])

    for i in range(q):
        d = []
        for j in range(w1):
            sum = 0
            for k in range(q1):
                sum = sum+a[i][k]*b[k][j]
            d.append(sum)
        c.append(d)
    return c
    

def sub(a,b):
    q = len(a)
    q1 = len(a[0])

    c = []
    for i in range(q):
        d = []
        for j in range(q1):
            d.append(a[i][j]-b[i][j])
        c.append(d)
    return c

def add(a,b):
    q = len(a)
    q1 = len(a[0])

    c = []
    for i in range(q):
        d = []
        for j in range(q1):
            d.append(a[i][j]+b[i]+j)
        c.append(d)
    return c

def transpose(a):
    c = []
    for i in range(len(a[0])):
        d = []
        for j in range(len(a)):
            d.append(a[j][i])
        c.append(d)
    return c

def isoptimal(a):
    for i in a:
        for j in i:
            if j<0:
                return False
    return True

def smallestindex(a):#for nx1 matrix
    b = []
    for i in a:
        b.append(min(i))
    k = 0
    for j in b:
        if j==min(b):
            break
        k = k + 1
    return k

def deltaJ(cb,B,A,cj):
    
    cb = transpose(cb)

    delta = mul(cb,B)
    alpha = mul(delta,A)
    alpha = transpose(alpha)
    alpha = sub(alpha,cj)

    return alpha

def column(a,k):
    _a = transpose(a)
    col = [_a[k]]
    col = transpose(col)
    return col

def ratio(a,b):#for 2 d array
    c = []
    for i in range(len(a)):
        if b[i][0]<=0:
            c.append([10000007])
            continue
        else:
            c.append([(a[i][0])/b[i][0]])
    return c
def answer(A,B,b,cb,cj):
    xb = mul(B,b)
    m = []
    while True:
        if isoptimal(deltaJ(cb,B,A,cj)):
            return (xb,m)

        else:
            min_index = smallestindex(deltaJ(cb,B,A,cj))
            m.append(min_index)

            x = column(A,min_index)

            x = mul(B,x)
            min_index2 = smallestindex(ratio(xb,x))
   

            B[0],B[min_index2] = B[min_index2],B[0]
            x[0],x[min_index2] = x[min_index2],x[0]

            for j in range(len(x)):
                if j==0:
                    for k in range(len(B[0])):
                        B[j][k] = B[j][k]/x[j][0]
    
                    
                else:
                    for k in range(len(B[0])):
                        B[j][k] = B[j][k] - x[j][0]*B[0][k]
                    
            B[0],B[min_index2] = B[min_index2],B[0]
            x[0],x[min_index2] = x[min_index2],x[0]
    
            cb[min_index2][0] = cj[min_index][0]
            xb = mul(B,b)

def optimizationFunction(s):#6x-2y+3z
    l = []
    i = 0
    while i<len(s):
        if s[i].isdigit():
            if i+1<len(s):
                if s[i+1].isdigit():
                    if i-1<0:
                        l.append([int(s[i]+s[i+1])])
                    else:
                        if s[i-1]=="-":
                            l.append([-int(s[i]+s[i+1])])
                        else:
                            l.append([int(s[i]+s[i+1])])
                    i = i+1
                else:
                    if i-1<0:
                        l.append([int(s[i])])
                    else:
                        if s[i-1]=="-":
                            l.append([-int(s[i])])
                        else:
                            l.append([int(s[i])])
                
            else:
                if i-1<0:
                    l.append(int(s[i]))
                else:
                    if s[i-1]=="-":
                        l.append([-int(s[i])])
                    else:
                        l.append([int(s[i])])
        i = i+1

            
        
    return l

             

def constraintsFunction(s):
    l = []
    i = 0
    while i<len(s):
        if s[i].isdigit():
            if i+1<len(s):
                if s[i+1].isdigit():
                    if i-1<0:
                        l.append(int(s[i]+s[i+1]))
                    else:
                        if s[i-1]=="-":
                            l.append(-int(s[i]+s[i+1]))
                        else:
                            l.append(int(s[i]+s[i+1]))
                    i = i+1
                else:
                    if i-1<0:
                        l.append(int(s[i]))
                    else:
                        if s[i-1]=="-":
                            l.append(-int(s[i]))
                        else:
                            l.append(int(s[i]))
                
            else:
                if i-1<0:
                    l.append(int(s[i]))
                else:
                    if s[i-1]=="-":
                        l.append(-int(s[i]))
                    else:
                        l.append(int(s[i]))
        i = i+1
    return l

def B(a):
    B = []
    for i in range(a):
        B.append([0]*a)

    for i in range(a):
        B[i][i] = 1

    return B

def variables(s):
    a = []
    for i in s:
        if i.isalpha():
            a.append(i)
    return a



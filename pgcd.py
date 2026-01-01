def pgcd(a,b):
    pgcd=0 
    if a>b:
        for _ in range(b):
            q = a//b 
            r = a-b*q
            if r==0:
                pgcd=b
                break
            else:
                pgcd = r
                a,b=b,r
    else:
        for _ in range(b):
            q = b//a 
            r = b-a*q
            if r==0:
                pgcd=a
                break
            else:
                pgcd = r
                b,a=a,r
    return pgcd
    
print(pgcd(84,30)) #-->3

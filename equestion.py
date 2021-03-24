def XtimesY(x:float,y:float)->float:
    if x<=0:
        return 0
    lmala = Ln(x)*y
    print(exponent(lmala))
    return (exponent(lmala))
    
   
def exponent(x: float)->float:
    sumE=1
    mach=1
    mon=x
    for i in range(1,100):
        sumE=sumE+(mon/mach)
        mon=mon*x
        mach=mach*(i+1)
    return sumE


def Ln(x:float)->float:
    if x<=0:
       return 0.0
    Yn=0.0
    for i in range(1,100):
        Yn+=2*((x-exponent(Yn))/(x+exponent(Yn)))
    return Yn    
               
def sqrt(x:float,y:float) -> float:
    if y<=0:
        return print(0)
    ans=XtimesY(y, (1/x))      
    return ans    

def calculate(x:float) -> float:
    if x<=0:
        return 0
    ansCac:float= (exponent(x))
    ansSq:float=(sqrt(x,x))
    ans1:float=(XtimesY(x, -1.0))
    ans2:float=(XtimesY(7.0, x))
    total=ans1*ans2*ansCac*ansSq
    print(total)
    
    
XtimesY(3,-1)
sqrt(0.5, 3)
calculate(3)
    
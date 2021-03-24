def XtimesY(x:float,y:float)->float:
    if x<=0:
        return 0
    lmala = Ln(x)*y
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
        return 0
    ans=XtimesY(y, (1/x))      
    return ans    

def calculate(x:float) -> float:
    if x<=0:
        return 0
    ansCac= (exponent(x))
    ansSq=(sqrt(x,x))
    ans1=(XtimesY(x, -1.0))
    ans2=(XtimesY(7.0, x))
    total=ans1*ans2*ansCac*ansSq
    return total
    
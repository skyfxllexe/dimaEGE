from functools import lru_cache


def moves(h):
    a, b = h
    return ((a+1, b+2), (a+2, b+1), (a*2,b), (a,b*2))

@lru_cache(None)
def f(h):
    if sum(h) >= 41:
        return "END"
    if (any(f(x)=="END" for x in moves(h))):
        return "P1"
    # if all(f(x) =="P1" for x in moves(h)):
    #     return "V1"
    # if any(f(x) == "V1" for x in moves(h)):
    #     return "P2"
    # if all((f(x) == "P2" or f(x) == "P1") for x in moves(h)):
    #     return "V2"
 
for i in range(1,33):
    h = (8, i)
    if (any(f(x) == "P1" for x in moves(h))):
        print("POBEDA", i)
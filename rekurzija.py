## REKURZIJA

def recursion(top_number: int) -> int:
    if top_number < 1:
        return 0
    
    return top_number + recursion(top_number-1)


print(recursion(5))
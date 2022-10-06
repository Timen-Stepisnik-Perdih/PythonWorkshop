## FUNKCIJE

def sum_of_list(seznam: list) -> float:
    sum_ = 0
    for item in seznam:
        sum_ += item
    return sum_

test_list = [1,2,3,4]
print(sum_of_list(test_list))
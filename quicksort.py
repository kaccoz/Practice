# pivot = firest element 
def quicksort(lst):
    if len(lst) <= 1:
        return lst
    
    pivot = lst[0]
    left = [x for x in lst[1:] if x < pivot]
    right = [x for x in lst[1:] if x > pivot]

    print(left), print(right)
    return quicksort(left) + [pivot] + quicksort(right)



if __name__ == '__main__':
    test1 = []
    test2 = [1]
    test3 = [8, 8, 8]
    test4 = [1, 2, 3, 4, 5, 6]
    test5 = [1293, 983, 632, 470, 193, 88]
    test6 = [3, 7, 8, 2, 0, 1]
    test7 = [8, -3, 9, 7, 2, 4, 1]
    test8 = [-5, -3, -6, -2, -8]

    print("Testing selection sort...")
    assert quicksort(test1) == []
    assert quicksort(test2) == [1]
    assert quicksort(test3) == [8, 8, 8]
    assert quicksort(test4) == [1, 2, 3, 4, 5, 6]
    assert quicksort(test5) == [88, 193, 470, 632, 983, 1293]
    assert quicksort(test6) == [0, 1, 2, 3, 7, 8]
    assert quicksort(test7) == [-3, 1, 2, 4, 7, 8, 9]
    assert quicksort(test8) == [-8, -6, -5, -3, -2]

    print(quicksort(test1))
    print(quicksort(test2))
    print(quicksort(test3))
    print(quicksort(test4))
    print(quicksort(test5))
    print(quicksort(test6))
    print(quicksort(test7))
    print(quicksort(test8))
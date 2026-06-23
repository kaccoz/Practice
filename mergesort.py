def mergesort(lst):
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    left = mergesort(lst[:mid])
    right = mergesort(lst[mid:])

    return merge(left, right)

def merge(lst1, lst2):
    result = []

    i, j = 0, 0
    while i < len(lst1) and j < len(lst2):
        if lst1[i] <= lst2[j]:
            result.append(lst1[i])
            i += 1
        else:
            result.append(lst2[j])
            j += 1
        
    result += lst1[i:]
    result += lst2[j:]
    return result 


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
    assert mergesort(test1) == []
    assert mergesort(test2) == [1]
    assert mergesort(test3) == [8, 8, 8]
    assert mergesort(test4) == [1, 2, 3, 4, 5, 6]
    assert mergesort(test5) == [88, 193, 470, 632, 983, 1293]
    assert mergesort(test6) == [0, 1, 2, 3, 7, 8]
    assert mergesort(test7) == [-3, 1, 2, 4, 7, 8, 9]
    assert mergesort(test8) == [-8, -6, -5, -3, -2]

    print(mergesort(test1))
    print(mergesort(test2))
    print(mergesort(test3))
    print(mergesort(test4))
    print(mergesort(test5))
    print(mergesort(test6))
    print(mergesort(test7))
    print(mergesort(test8))

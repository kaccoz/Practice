def selectionsort(lst):
    n = len(lst)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if lst[j] < lst[min_index]:
                min_index = j
        
        lst[i], lst[min_index] = lst[min_index], lst[i]

    return lst


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
    assert selectionsort(test1) == []
    assert selectionsort(test2) == [1]
    assert selectionsort(test3) == [8, 8, 8]
    assert selectionsort(test4) == [1, 2, 3, 4, 5, 6]
    assert selectionsort(test5) == [88, 193, 470, 632, 983, 1293]
    assert selectionsort(test6) == [0, 1, 2, 3, 7, 8]
    assert selectionsort(test7) == [-3, 1, 2, 4, 7, 8, 9]
    assert selectionsort(test8) == [-8, -6, -5, -3, -2]

    print(selectionsort(test1))
    print(selectionsort(test2))
    print(selectionsort(test3))
    print(selectionsort(test4))
    print(selectionsort(test5))
    print(selectionsort(test6))
    print(selectionsort(test7))
    print(selectionsort(test8))

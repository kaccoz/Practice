def insertionsort(lst):
    for i in range(len(lst)):
        for j in range(i, 0, -1):
            if lst[j - 1] > lst[j]:
                lst[j - 1], lst[j] = lst[j], lst[j - 1]
            else:
                break

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
    assert insertionsort(test1) == []
    assert insertionsort(test2) == [1]
    assert insertionsort(test3) == [8, 8, 8]
    assert insertionsort(test4) == [1, 2, 3, 4, 5, 6]
    assert insertionsort(test5) == [88, 193, 470, 632, 983, 1293]
    assert insertionsort(test6) == [0, 1, 2, 3, 7, 8]
    assert insertionsort(test7) == [-3, 1, 2, 4, 7, 8, 9]
    assert insertionsort(test8) == [-8, -6, -5, -3, -2]

    print(insertionsort(test1))
    print(insertionsort(test2))
    print(insertionsort(test3))
    print(insertionsort(test4))
    print(insertionsort(test5))
    print(insertionsort(test6))
    print(insertionsort(test7))
    print(insertionsort(test8))

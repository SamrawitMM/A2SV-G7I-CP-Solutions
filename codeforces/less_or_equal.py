n, k = map(int, input().split())

arr = list(map(int, input().split()))

arr.sort()


if k == 0:
    if arr[0] == 1:
        print(-1)
    else:
        print(arr[0] - 1)
else:
    first_split = arr[:k]
    max_first = first_split[-1]
    
    if k == n:
        print(max_first)
    else:
        second_largest = arr[k]
        if max_first < second_largest:
            print(max_first)
        else:
            print(-1)



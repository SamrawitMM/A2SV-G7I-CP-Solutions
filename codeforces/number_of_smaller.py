n, m = map(int, input().split())
 
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
 
first = 0
less = []
for second in range(m):
    while first < n and arr1[first] < arr2[second] :
        first += 1
    less.append(first)
 
print(*less)

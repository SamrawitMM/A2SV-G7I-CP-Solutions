n, m = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
 
left_of_n = 0
left_of_m = 0
 
output = []
 
 
while left_of_n < n and left_of_m < m:
    if arr2[left_of_m] < arr1[left_of_n]:
        output.append(arr2[left_of_m])
        left_of_m += 1
 
    else:
        output.append(arr1[left_of_n])
 
        left_of_n += 1
 
output.extend(arr1[left_of_n:])
output.extend(arr2[left_of_m:])
 
print(*output)

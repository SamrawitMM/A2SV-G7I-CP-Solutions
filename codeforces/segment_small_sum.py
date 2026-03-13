n, s = map(int, input().split())
arr = list(map(int, input().split()))

i = 0
total_sum = 0
max_length = float('-inf')
j = 0
while i < n:
    total_sum += arr[i]

    while total_sum > s:
        total_sum -= arr[j]
        j += 1
        
    max_length = max(i - j + 1, max_length)


    i += 1

if max_length == float('inf'):
    print(0)
else:
    print(max_length)

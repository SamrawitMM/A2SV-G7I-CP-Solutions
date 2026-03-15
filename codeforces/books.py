b, t = map(int, input().split())
arr = list(map(int, input().split()))
 
 
 
cum_sum = 0
best = 0
left = 0
for right in range(b):
    cum_sum += arr[right]
 
    while cum_sum > t:
        cum_sum -= arr[left]
        left += 1
 
 
    best = max(best, right - left + 1)
 
 
print(best)

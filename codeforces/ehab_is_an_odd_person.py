n = int(input())
arr = list(map(int, input().split()))


has_odd = any(num for num in arr if num % 2 != 0)
has_even = any(num for num in arr if num % 2 == 0)

if has_odd and has_even:
    print(*sorted(arr))

else:
    print(*arr)

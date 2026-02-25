test_cases = int(input())

def runTestCase(test_cases):
    for _ in range(test_cases):
        length = int(input())
        arr = list(map(int, input().split()))

        arr.sort()
        print(removeSmallest(arr))

        
def removeSmallest(arr):
    status = "YES"
    if len(arr) <= 1: return status
    while len(arr) > 1:
        if arr[1] - arr[0] <= 1:
            arr.pop(0)
        else:
            status = 'NO'
            break

    return status

    
runTestCase(test_cases)

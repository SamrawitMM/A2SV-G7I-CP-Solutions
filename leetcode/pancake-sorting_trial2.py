class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:

        n = len(arr) - 1
        k = []
        for i in range(n, -1, -1):
            j  = 0
            found = False
            while j < i:
                if arr[j] > arr[i] and j != 0:
                    arr[:j+1] = arr[:j+1][::-1]
                    k.append(j+1)

                    arr[:i+1] = arr[:i+1][::-1]
                    k.append(i+1)
                    found = True
                    print(arr)

                    j = 0
                    continue

                elif arr[j] > arr[i] and j == 0:
                    arr[:i+1] = arr[:i+1][::-1]
                    k.append(i+1)
                    found = True
                    print(arr)

                    j = 0
                    continue

                j += 1  

            if not found:
                continue 
        
        return k

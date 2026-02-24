class Solution: 
    def selectionSort(self, arr):
        #code here
        for i in range(len(arr)):
            min_inx = i
            for j in range(i+1, len(arr)):
                if arr[j] < arr[min_inx]:
                    min_inx = j
                    
            arr[i], arr[min_inx] = arr[min_inx], arr[i]
            
        
        return arr

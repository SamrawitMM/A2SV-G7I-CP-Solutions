class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:

        left = 0 
        right = len(letters) - 1
        first = None

        while left <= right:
            mid = (left + right ) // 2

            if letters[mid] > target:
                right = mid - 1
                first = letters[mid]

            else:
                left = mid + 1

        return letters[0] if first is None else first



        
        
        # left = 0
        # right = len(letters) - 1

        # while left < right:

        #     mid = ( left + right) // 2

        #     if letters[mid] > target:
        #         right = mid

        #     else:
        #         left = mid + 1

        # return letters[left] if letters[left] > target else letters[0]



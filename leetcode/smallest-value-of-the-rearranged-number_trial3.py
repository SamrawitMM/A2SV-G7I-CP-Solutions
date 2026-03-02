class Solution:
    def smallestNumber(self, num: int) -> int:
        array  = []
        negative = num < 0
        output = 0
        
        num = abs(num)

        if num == 0:
            return 0


        while num > 0:
            digit = num % 10
            array.append(digit)
            num = num // 10

        if negative:
            array.sort(reverse=True)
            output = -int("".join(str(num) for num in array))

            print(array)
        else:
            array.sort()
            if array[0] == 0:
                for i in range(1, len(array)):
                    if array[i] != 0:
                        array[0], array[i] = array[i], array[0]
                        break

            
            output = int("".join(str(num) for num in array))

        return output


class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        total = sum(skill)
        n = len(skill)


        left = 0
        right = n - 1

        team_sum = skill[right] + skill[left]

        chemistry  = 0
        while left < right:
            if skill[right] + skill[left] != team_sum:
                return -1
            
            chemistry += skill[right] * skill[left]

            left += 1
            right -= 1

        return chemistry

        # while left <= right:
        #     if skill[left] + skill[right] < equal_skill:
        #         left += 1
        #     elif skill[left] + skill[right] > equal_skill:
        #         right -= 1
        #     else:
        #         output.append((skill[left], skill[right]))
        #         left += 1
        #         right -= 1

        # if len(skill) == 2:
        #     return skill[0] * skill[1]
        
            
        
        # product = 0
        # for x, y in output:
        #     product += (x*y)

        # print(output)

        # return product



        
class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:


        state = {}
        def bestScore(l, r, player):

            if (l, r, player) in state: return state[(l, r, player)]

            if l > r: return 0

            if player: state[(l, r, player)] =  max(nums[l] + bestScore(l+1, r, not player), nums[r] + bestScore(l, r-1, not player))
            else:
                state[(l, r, player)] = min(-nums[l] + bestScore(l+1, r, not player), -nums[r] + bestScore(l, r-1, not player) )

            return state[(l, r, player)]

            
        return bestScore(0, len(nums)-1, True) >= 0


        























        
        # def recur(nums, inx, score_1, score_2):            

        #     turn = inx % 2 

        #     print(inx, turn, " checking ")

        #     current_score = 0
        #     if nums[0] > nums[-1]:
        #         current_score = nums[0]
        #         del nums[0]

        #     else:
        #         current_score = nums[-1]
        #         del nums[-1]

            
        #     if turn: 
        #         score_2 += current_score

        #     else:
        #         score_1 += current_score

        #     print(score_1, score_2)

        #     if nums == []:
        #         return score_1 >= score_2

        #     return recur(nums, inx+1, score_1, score_2)


        return recur(nums, 0, 0, 0) 






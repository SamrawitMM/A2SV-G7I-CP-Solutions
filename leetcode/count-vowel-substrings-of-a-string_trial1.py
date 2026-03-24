class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowel = ['a', 'e', 'i', 'o', 'u']

        window = defaultdict(int)
        left = 0
        count = 0
        for i in range(len(word)):
            if word[i] not in vowel:
                window.clear()
                left = i + 1
                i += 1
                continue
                
            window[word[i]] = i

            
            if len(window) == len(vowel):
                count += min(window.values()) - left + 1

        return count


            
































        # window = {}
        # i = 0
        # j = 0
        # count = 0
        # while i  < len(word):
        #     current = word[i]

        #     if word[i] not in vowel:
        #         window.clear()
        #         j = i + 1
        #         i += 1
        #         continue

        #     window[word[i]] = i

        #     if len(window) == len(vowel):
        #         count += min(window.values()) - j + 1

        #     i += 1

                


        # return count

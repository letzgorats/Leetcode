# solution 1 - (string,greedy,ord) - (11ms) - (2025.07.03)
class Solution:
    def kthCharacter(self, k: int) -> str:

        word = 'a'
        while len(word) < k:

            tmp = ''
            for w in word:
                tmp += chr((ord(w) + 1) % 97 + 97)
            # print(tmp)
            word += tmp
            # print(word)

        return word[k - 1]
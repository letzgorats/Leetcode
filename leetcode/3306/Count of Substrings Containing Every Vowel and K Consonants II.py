# wrong solution - sliding window
# counter example - word : "aeueio", k = 0
class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:

        vowels = {"a", "e", "i", "o", "u"}

        cur_window = 5 + k
        answer = 0

        for i in range(len(word)):

            s = Counter(word[i:i + cur_window])
            has_all_vowels = vowels.issubset(s.keys())
            print(s)
            # 자음만 추출
            total_consonants = sum(count for ch, count in s.items() if ch not in vowels)
            has_k_consonants = (total_consonants == k)
            # print(has_all_vowels)
            # print(has_k_constants)
            j = i + cur_window
            while has_all_vowels and has_k_consonants:
                answer += 1
                # print(word[i:j])
                if j >= len(word):
                    break
                if word[j] in vowels:
                    cur_window += 1
                    has_all_vowels = True
                    j += 1
                    continue
                else:
                    has_k_consonants = False
                    cur_window = 5 + k
                    break

        return answer


# solution 1 - sliding window - (1015ms) - (2025.03.10)
from collections import Counter, defaultdict
class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:

        vowels = {"a", "e", "i", "o", "u"}
        left = 0
        vowel_count = defaultdict(int)  # 모음개수 추적
        current_k = 0  # 현재 자음 개수
        extra_left = 0  # 중복 모음으로 인해 추가 가능한 서브스트링 개수
        answer = 0

        for right in range(len(word)):

            char = word[right]

            if char in vowels:
                vowel_count[char] += 1
            else:
                current_k += 1

            # 자음 개수가 k를 초과하면 left를 이동하여 조절
            while current_k > k:
                left_char = word[left]
                if left_char in vowels:
                    vowel_count[left_char] -= 1
                    if vowel_count[left_char] == 0:
                        del vowel_count[left_char]
                else:
                    current_k -= 1
                left += 1
                extra_left = 0  # 새 윈도우 시작이므로 초기화

            # 모든 모음이 포함되었고, 자음 개수가 정확히 k개 일 떄
            while len(vowel_count) == 5 and current_k == k and left < right and word[left] in vowels and vowel_count[
                word[left]] > 1:
                extra_left += 1
                vowel_count[word[left]] -= 1
                left += 1

            if len(vowel_count) == 5 and current_k == k:
                answer += (1 + extra_left)

        return answer

# solution 2 - two pointers, sliding window - (1964ms) - (2025.03.10)
from collections import Counter


class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:

        def atleast(k):
            vowel = defaultdict(int)
            non_vowel = 0
            res = 0
            l = 0

            for r in range(len(word)):
                if word[r] in "aeiou":
                    vowel[word[r]] += 1
                else:
                    non_vowel += 1

                while len(vowel) == 5 and non_vowel >= k:
                    res += len(word) - r
                    if word[l] in "aeiou":
                        vowel[word[l]] -= 1
                    else:
                        non_vowel -= 1

                    if vowel[word[l]] == 0:
                        vowel.pop(word[l])
                    l += 1

            return res

        return atleast(k) - atleast(k + 1)

'''
------------|at least k()----------------->
------------------------|at least (k+1)--->

at least(k) - at least(k+1) = exactly k consonants
'''
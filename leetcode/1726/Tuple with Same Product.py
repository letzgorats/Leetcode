from collections import defaultdict
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:

        answer = 0
        product_dict = defaultdict(int)

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                product = nums[i] * nums[j]
                product_dict[product] += 1

        for value in product_dict.values():
            # (count_of permutation==4) * (combination)
            answer += 4 * value * (value - 1)

        '''
        nCr = n! / (n-r)!r!

        여기서는 r 이 2 (두 개의 숫자 (a,b)를 선택하여 그들의 곱을 계산하는 과정에서 비롯된다)

        n(n-1)(n-2)! / (n-2)! * 2
        => n(n-1) / 2

        따라서 조합의 개수는 "n개의 원소 중에 2개를 선택"하는 방법이므로
        => n(n-1) / 2 개 이고,

        (a,b,c,d) 자리 배치를 하는 경우의 수는
        (a, b, c, d)
        (a, b, d, c)
        (b, a, c, d)
        (b, a, d, c)
        (c, d, a, b)
        (d, c, a, b)
        (c, d, b, a)
        (d, c, b, a)
        => 로 총 8 개이므로, 각 조합마다 8개의 경우가 존재한다.

        따라서, 최종적으로

        n(n-1) / 2 * 8 = n(n-1) * 4 개 를 찾아야 한다.

        '''

        return answer
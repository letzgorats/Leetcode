# solution 1 - (dp,transform,frequency,hash_table,counting) - () - (2025.05.14)
class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:

        mod = 10 ** 9 + 7

        # a -> b , b -> c, c ->d, .... , x->y, y->z, z->a
        transform_rules = [[0] * 26 for _ in range(26)]
        for i in range(25):
            transform_rules[i][i + 1] = 1

        transform_rules[25][0] = 1
        # print(transform_rules)

        count = [0] * 26

        for idx, alpha in enumerate(s):
            count[ord(alpha) - 97] += 1

        # print(count)

        def matrix_multiply(A, B, mod):
            size = len(A)
            result = []

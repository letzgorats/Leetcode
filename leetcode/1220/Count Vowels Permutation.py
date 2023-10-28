# top - down method

class Solution(object):
    def countVowelPermutation(self, n):
        """
        :type n: int
        :rtype: int
        """
        # a, e, i, o, u

        # a -> ae
        # e -> ea, ei
        # i -> ia, ie, io, iu
        # o -> oi, ou
        # u -> ua

        INF = 10**9 + 7
        cache = {}

        possibleVowels = {
            '':['a','e','i','o','u'],
            'a':['e'],
            'e':['a','i'],
            'i':['a', 'e', 'o', 'u'],
            'o':['i','u'],
            'u':['a'],
        }

        answer = []

        def backtracking(n,c):

            if n == 1:
                return 1
            
            if (n,c) in cache:
                return cache[(n,c)]

            cache[(n,c)]= 0


            for vowel in possibleVowels[c]:
                cache[(n,c)] += (backtracking(n-1,vowel))

            # print(total)

            return cache[(n,c)]

        return backtracking(n + 1,"") % INF



# bottom up dp

class Solution(object):
    def countVowelPermutation(self, n):
        """
        :type n: int
        :rtype: int
        """
        # a, e, i, o, u

        # a -> ae
        # e -> ea, ei
        # i -> ia, ie, io, iu
        # o -> oi, ou
        # u -> ua

        mod=10**9+7
        a, e, i, o, u = 1, 1, 1, 1, 1
        
        # ->  {'a':['e'], 'e':['a','i'], 'i':['a','e','o','u'], 'o':['i','u'], 'u':['a']}
        # <-  {'a':['e','i','u'], 'e':['a','i'], 'i':['e','o'], 'o':['i'], 'u':['i','o']}

        for m in range(1, n):
            a_new = (e + i + u) % mod
            e_new = (a + i) % mod
            i_new = (e + o) % mod
            o_new = (i) % mod
            u_new = (i + o) % mod
            
            a, e, i, o, u = a_new, e_new, i_new, o_new, u_new 
        
        return (a + e + i + o + u)%mod


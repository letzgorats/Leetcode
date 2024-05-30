# solution 1
class Solution(object):
    def countTriplets(self, arr):
      
        i_start, j_start = 0,1
        answer = []
        
        while i_start < len(arr)-1:

            j_start = i_start+1
            
            while j_start < len(arr):
                a,b = 0,0

                for i in range(i_start,j_start):
                    a ^= arr[i]
                
                for j in range(j_start,len(arr)):
                    b ^= arr[j]
                    if a == b:
                        answer.append((i_start,j_start,j))
                
                j_start += 1

            i_start += 1
            

        return len(answer)


# solution 2
class Solution(object):
    def countTriplets(self, arr):
        
        n = len(arr)
        count = 0
        prefix_xor = [0] * (n+1)

        for i in range(n):

            prefix_xor[i+1] = prefix_xor[i] ^ arr[i]
        
        for i in range(n):
            for j in range(i+1,n):
                if prefix_xor[i] == prefix_xor[j+1]:
                    count += (j-i)

        # print(prefix_xor)

    
        return count


# set + backtracking solution

class Solution(object):
    def beautifulSubsets(self, nums, k):

        def backtracking(index,cur_list,used):

            if index == len(nums):
                if cur_list:
                    self.count += 1
                return 

            
            # 현재 원소를 포함하지 않는 경우
            backtracking(index+1,cur_list,used)

            # 현재 원소를 포함하는 경우
            if not used.get(nums[index]-k,False) and not used.get(nums[index]+k,False):
                cur_list.append(nums[index])
                used[nums[index]] = used.get(nums[index],0) + 1
                backtracking(index+1,cur_list,used)
                cur_list.pop()     
                used[nums[index]] -= 1
                if used[nums[index]] == 0 :
                    del used[nums[index]]

        self.count = 0
        backtracking(0,[],{})

        return self.count
        
        

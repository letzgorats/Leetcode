# solution 1 - (two pointers, greedy, partition, hash_table) - (7ms) - (2025.03.30)
from collections import defaultdict
class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        last_index = defaultdict(int)  # alphabet -> last_index
        for idx, alpha in enumerate(s):
            last_index[alpha] = idx

        # print(last_index)

        start, end = 0, 0
        res = []
        for i, alpha in enumerate(s):

            end = max(end, last_index[alpha])
            if i == end:
                partition_size = end - start + 1
                res.append(partition_size)
                start = i + 1

        return res

    '''
    목적 : 가능한 한 많이 자르자.(단, 문자가 다른 조각에 섞이지 않게)
    
    -> 한 파티션 안에서 포함된 모든 문자의 마지막 등장 위치까지 한 번에 커버해야 한다.
    -> 그래야 그 문자가 다른 파트에 안 섞이니까
    
    end = max(end,last_index[alpha]) 의 의미
    -> 어떤 문자가 등장하면, 그 문자의 마지막 위치까지는 반드시 포함되어야 하니까,
    -> 현재 구간의 끝(end)을 그 문자 마지막 위치까지 확장해야 한다.
    
    즉, 한 문자 때문에라도 현재 파티션을 더 길게 가져가야 할 수 있다는 말!
    
    if i == end:
    -> 현재까지 만난 문자들의 "최후 등장 위치"를 "전부 커버"한 지점이 바로 i==end 이다.
    -> 즉, 지금까지의 문자들은 이제 이 파티션에 다 포함되어 끝났다는 뜻으로, 여기서 안전하게 자를 수 있다. 
    '''


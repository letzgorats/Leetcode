from bisect import bisect_left
from typing import List

class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:

        # 이 함수는 "정확히 k개의 작업을 할당할 수 있는가?"를 판단한다.
        def can_assign(k):
            # 가장 강한 k명의 worker만 사용 (뒤에서 k개)
            avail = worker_strengths[-k:]  # 오름차순 정렬이므로 뒤가 가장 강함
            pills_remain = pills  # 사용 가능한 pill 수
            # 가장 어려운 k개의 task만 고려 (앞에서 k개)
            for req in reversed(task_requirements[:k]):  # 난이도 높은 순서로 진행
                if avail and avail[-1] >= req:
                    # 아무 처리 없이 이 worker가 task를 수행할 수 있으면 바로 사용
                    avail.pop()
                else:
                    # pill 없으면 이 task는 수행 불가능
                    if pills_remain <= 0:
                        return False
                    # pill을 써야 하므로, pill 사용 후에도 task를 수행할 수 있는
                    # 가장 약한 worker를 이진탐색으로 찾는다
                    threshold = req - strength
                    idx = bisect_left(avail, threshold)  # strength 더하면 req 만족되는 최소 worker 찾기
                    if idx == len(avail):
                        # 그런 worker가 없다면 실패
                        return False
                    # 해당 worker는 pill을 먹고 작업 수행
                    avail.pop(idx)
                    pills_remain -= 1
            return True

        # tasks와 workers를 정렬 (오름차순)
        task_requirements = sorted(tasks)
        worker_strengths = sorted(workers)

        # 이분 탐색 범위는 0부터 가능한 최대 작업 수까지
        low, high = 0, min(len(tasks), len(workers))
        answer = 0

        while low <= high:
            mid = (low + high) // 2
            if can_assign(mid):
                answer = mid  # mid 개의 작업을 할당할 수 있다면 일단 답으로 저장하고
                low = mid + 1  # 더 많은 작업도 가능한지 탐색
            else:
                high = mid - 1  # 안 되면 줄인다

        return answer

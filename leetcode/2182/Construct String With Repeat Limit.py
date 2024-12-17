# solution 1 -greedy(counter,sort)
from collections import Counter
class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        # 문자 빈도수를 구한 뒤 내림차순 정렬
        counter = Counter(s)
        sorted_alpha = sorted(counter.items(), key=lambda x: -ord(x[0]))  # 문자 순으로 내림차순 정렬
        answer = []

        while sorted_alpha:
            alpha, count = sorted_alpha.pop(0)  # 가장 큰 문자 꺼내기

            # 현재 문자를 최대 repeatLimit까지 추가
            add_count = min(repeatLimit, count)
            answer.append(alpha * add_count)
            count -= add_count

            # 문자가 남아 있다면, 다음 큰 문자 추가 필요
            if count > 0:
                if not sorted_alpha:
                    break  # 다음 문자가 없다면 종료

                # 다음 큰 문자 추가
                next_alpha, next_count = sorted_alpha.pop(0)
                answer.append(next_alpha)
                next_count -= 1

                # 남은 문자들 다시 리스트에 추가
                sorted_alpha.append((alpha, count))  # 현재 문자 다시 추가
                if next_count > 0:
                    sorted_alpha.append((next_alpha, next_count))

                # 문자 순서 유지 위해 다시 정렬
                sorted_alpha.sort(key=lambda x: -ord(x[0]))

        return "".join(answer)

# solution 2 - heapq
import heapq
from collections import Counter


class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        # 문자 빈도수 구하기
        counter = Counter(s)
        # (-문자 ASCII 값, 빈도수)를 힙에 추가 (사전순 정렬 유지)
        max_heap = [(-ord(alpha), count) for alpha, count in counter.items()]
        heapq.heapify(max_heap)  # 최대 힙 구성

        result = []

        while max_heap:
            # 가장 사전순으로 큰 문자 꺼내기
            alpha_ascii, count = heapq.heappop(max_heap)
            alpha = chr(-alpha_ascii)  # 원래 문자로 복원

            # 문자를 repeatLimit만큼 추가
            add_count = min(repeatLimit, count)
            result.append(alpha * add_count)
            count -= add_count

            # 현재 문자가 남아 있고 다음 문자가 있으면 처리
            if count > 0:  # 아직 남은 문자가 있으면
                if not max_heap:  # 다음 문자가 없으면 종료
                    break

                # 다음으로 큰 문자 꺼내기
                next_alpha_ascii, next_count = heapq.heappop(max_heap)
                next_alpha = chr(-next_alpha_ascii)

                result.append(next_alpha)  # 다음 문자 하나 추가
                next_count -= 1  # 해당 문자 사용

                # 남은 문자들 다시 힙에 추가
                heapq.heappush(max_heap, (-ord(alpha), count))  # 현재 문자 다시 삽입
                if next_count > 0:
                    heapq.heappush(max_heap, (-ord(next_alpha), next_count))

        return "".join(result)

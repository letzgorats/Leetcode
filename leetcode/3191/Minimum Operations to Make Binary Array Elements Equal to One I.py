# solution 1 - greedy, bitwise - (106ms) - (2025.03.19)
class Solution:
    def minOperations(self, nums: List[int]) -> int:

        n = len(nums)
        count = 0

        for i in range(n - 2):  # 마지막 2칸은 따로 처리
            if nums[i] == 0:
                # (i,i+1,i+2) 3칸을 뒤집음
                nums[i] ^= 1
                nums[i + 1] ^= 1
                nums[i + 2] ^= 1
                count += 1
            # print(nums)

        # 마지막 0 이 남아 있으면 불가능
        return count if nums[-2:] == [1, 1] else -1

'''
그리디(Greedy)가 보장되는 핵심 원리
- 3개 단위로만 뒤집을 수 있는 제약이 있기 때문이다.
- 현재 0을 해결하는 유일한 방법이 "해당 위치에서 바로 뒤집는 것"
- 앞에서부터 처리하면 불필요한 중복 연산을 피할 수 있다.

- 만약 마지막까지 0이 남아있다면, 그 nums 는 모두 1로 바꾸지 못하는 nums 인 것이다.
- 이 문제에서 bfs/dp 를 사용해도 결과는 같겠지만, 굳이 사용할 필요 없음. 
- "각각의 0을 해결하는 방법이 이미 최적의 선택"이기 때문이다.
'''

'''
그리디가 보장되지 않는 flip 문제의 예시
|                 조건	          |     Greedy 가능?	|           설명                  |

특정 위치에서만 Flip 가능	                ❌	            미래의 최적해를 망칠 수 있음
Flip 횟수 제한이 있는 경우	                ❌	            최적의 순서를 찾지 못할 수 있음
특정 패턴을 유지해야 하는 경우	                ❌	            중간 과정에서 조건을 깨뜨릴 수 있음
연산 후 미래 상태가 달라질 가능성이 있는 경우	    ❌	            Greedy가 미래 상황을 고려하지 않기 때문

=> 이 보장이 없다면, BFS/DP 를 고려해야 한다.

=> 비트 뒤집기(Flipping) & Greedy 관련 문제
1310. XOR Queries of a Subarray	        Medium	        XOR 연산 & 비트마스킹
1009. Complement of Base 10 Integer	    Easy	        비트 뒤집기
137. Single Number II	                Medium	        비트마스킹 & 연산 최적화
201. Bitwise AND of Numbers Range	    Medium	        비트마스킹 & 최적화

=> Greedy가 최적해를 보장하지 않는 대표적인 문제들로, Greedy vs. DP/BFS 최적화 차이를 연습할 수 있음.
45. Jump Game II	                    Medium	    Greedy vs. DP 비교 연습
322. Coin Change	                    Medium	    Greedy 실패 & DP 사용 필수
55. Jump Game	                        Medium	    Greedy가 실패하는지 분석해보기
968. Binary Tree Cameras	            Hard	    Greedy vs. DFS 최적화 비교

=> BFS vs. DP를 비교할 수 있는 문제(이 문제들은 최소 연산 횟수를 구해야 해서 BFS/DP를 비교하며 풀어보면 좋음.)
1091. Shortest Path in Binary Matrix	Medium	    BFS 최단 경로 탐색
542. 01 Matrix	                        Medium	    BFS 최적화 연습
752. Open the Lock	                    Medium	    BFS로 최소 이동 횟수 찾기
847. Shortest Path Visiting All Nodes	Hard	    Bitmasking + BFS 최적화

=> DP 최적화 & 비트마스킹 문제(이 문제들은 BFS/DP/비트마스킹 조합을 최적화하는 연습을 할 수 있음.)
191. Number of 1 Bits	                                        Easy	비트마스킹
231. Power of Two	                                            Easy	비트 연산 활용
1359. Count All Valid Pickup and Delivery Options	            Hard	DP + 조합 최적화
1368. Minimum Cost to Make at Least One Valid Path in a Grid	Hard	BFS + DP 최적화

'''


'''
 최적의 문제 풀이 루트
1️⃣ Step 1: Greedy가 언제 실패하는지 익히기
322. Coin Change
45. Jump Game II

2️⃣ Step 2: Flip 문제에서 최적화 연습
3191. Minimum Operations to Make Binary Array Elements Equal to One I
1310. XOR Queries of a Subarray

3️⃣ Step 3: BFS vs. DP 비교 연습
542. 01 Matrix
752. Open the Lock

4️⃣ Step 4: 비트마스킹 + BFS/DP 조합 연습
847. Shortest Path Visiting All Nodes
1368. Minimum Cost to Make at Least One Valid Path in a Grid

'''
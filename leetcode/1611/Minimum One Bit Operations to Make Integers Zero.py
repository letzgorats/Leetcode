# solution 2 - (bit manipulation) - (0ms) -(2025.11.08)
class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        # bin_number = bin(n)[2:]
        # print(bin_number)

        # 그레이 -> 이진 역변환(누적 XOR)
        ans = 0
        while n:
            ans ^= n
            n >>= 1

        return ans # 그레이 코드에서의 인덱스
'''
규칙 1 : 0번째 비트(LSB)는 언제든 뒤집을 수 있음
규칙 2 : i 번째 비트는 "바로 아래 비트가 1"이고 "그 아래는 전부 0"일 때만
        뒤집을 수 있음
        -> 즉, 아래쪽 패턴이 100....00 일 때만 위 비트를 토글 가능

이러한 제약은 아래 사실을 만들어낸다!
1) 가능한 상태 전이가 "한번에 정확히 한 비트만 바뀌는" 형태이다.

- 규칙 1은 LSB만 바뀐다 -> 1비트 변화
- 규칙 2는 i 번째 비트 하나만 바뀐다 -> 나머지는 조건을 만족하는 그대로 유지 -> 1비트 변화

즉, 모든 합법적인 한 번의 연산은 정확히 "한 비트"만 토글한다.
이건 그레이코드(Gray code) 의 정의와 꼭 맞는다.

| 그레이 코드에서 인접한 수(다음 수)로 갈 때 항상 1 비트만 달라지도록 순서가 정해진다.
* (이진 코드 -> 그레이 코드)변환
 - 1) 이진 코드의 첫 비트(맨 앞)는 그대로 사용
 - 2) 두 번째 비트부터는 '앞 비트'와의 XOR 값을 사용
* (그레이 코드 -> 이진 코드)변환
 - 1) 그레이 코드의 첫 비트(맨 앞)는 그대로 사용
 - 2) 두 번째 비트부터는 '이진 코드의 구해놓은 비트'와 XOR 연산한 값을 사용한다.

2) 허용된 전이의 "순서"가 그레이 코드 순서를 강제한다.
- 더 중요한 건 "어떤 비트를 언제 바꿀 수 있나"의 순서 제약이, 
  바로 그레이 코드가 만들어지는 논리(재귀적/계단식 구조)와 동일하다는 점이다.

3) 0에서 시작해 규칙대로 "가능한 최소 연산"으로 만든 경로의 순서 인덱스가 바로 이진수 값이 된다.
- 0 에서 시작해서 규칙을 따라 한번에 1비트만 바꾸며 "가능한 가장 짧게" 각 수로 가는 경로는
  "그레이 코드 순서" 그대로를 따라간다.
- 즉, "n까지 가는 최소 연산 횟수"는 그레이 코드 리스트에서 n의 위치(인덱스)와 같다.
- 그레이 코드 값 g와 이 값의 이진수 인덱스 b 사이에는 표준 변환이 있다.
    - 이진 -> 그레이 : g = b ^ (b>>1)
    - 그레이 -> 이진 : 
        b = 0
        while g :
            b ^= g
            g >> 1
- 여기서 우리는 그레이 값이 n(문제의 상태값)이고, 그 인덱스 b가 곧
  "0에서 n까지의 최소 연산 횟수" = f(n) 이 된다.
  바로 그래서 누적 XOR 이 정답이 되는 것이다!

'''


# solution 1 - (bit manipulation) - (17ms) -(2023.11.30)
class Solution(object):
    def minimumOneBitOperations(self, n):
        """
        :type n: int
        :rtype: int
        """
        bits = bin(n)[2:]

        n, res = len(bits), 0

        for i in range(1,n+1):

            if bits[-i] == '1' : 
                res = (2**i-1-res)

        return res


"""
        to flip the bits to turn the number to zero
        
        Interpretation of Rules:
        - recursive:
            to turn a leading one of i bits to zero, the only way is to turn the i-1 bits to a leading one pattern
            and to turn the i-1 bits leading zero to zero, the only way is to turn the i-2 bits to a leading one pattern
            and so on, which is a recursive process
            
            (10000.. -> 11000.. -> 01000..), (01000.. -> 01100.. -> 00100), ..., (..010 -> ..011 -> ..001 -> ..000)
            
        - reversable:
        
            Let's make some observations to check if there's any pattern:

            - 2: 10 -> 11 -> 01 -> 00
            - 4: 100 -> 101 -> 111 -> 110 -> 010 -> 011 -> 001 -> 000
            - 8: 1000 -> 1001 -> 1011 -> 1010 -> 1110 -> 1111 -> 1101 -> 1100 -> 0100 -> (reversing 100 to 000) -> 0000
            ...
            
            based on the observation, turning every i bits leading one to zero, is turning the i-1 bits from 00.. to 10..
            and then back to 00.., which is a reverable process, and with the recursive process we can conclude that
            turning any length of 00..M-> 10.. is a reversable process
        
        - all unique states:
            since it is recursive and reversable, and we are flipping every bit between 1 and 0 programtically 10.. <-> 00..
            we can conclude that every intermediate state in a process is unique (2**i unique states, so we need 2**i - 1 steps)
        
                for i bits 10.. <-> 00.. - numer of operations f(i) = 2**i - 1
            
            this also aligns with the observation above that f(i) = 2*f(i-1) - 1 (-1 for no operation needed to achieve the initial 000)
        
        Process:
        to turn any binary to 0, we can turning the 1s to 0s one by one from lower bit to higher bit
        and because turning a higher bit 1 to 0, would passing the unique state including the lower bit 1s
        we can reverse those operations needed for the higher bit 100.. to the unique state including the lower bit 1s
        
        e.g. turning 1010100 to 0
        - 1010(100) -> 1010(000), we will need 2**3 - 1 operations
        - 10(10000) -> 10(00000), we will need (2**5 - 1) - (2**3 - 1) operations
        we will be passing the state 10(10100), which is ready available from the last state
        so we can save/reverse/deduct the operations needed for 1010(000) <-> 1010(100)
        - ...
        
            so for any binary, f(binary) would tell us how many operations we need for binary <-> 000..
            and for any more 1s, 100{binary} we can regard it as a process of 100.. <-> 100{binary} <-> 000{000..}
            which is 100.. <-> 000.. (2**i - 1) saving the operations 100{000..} <-> 100{binary} (f(binary))
            = (2**i - 1) - f(last_binary)
            
        """

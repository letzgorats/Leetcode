# solution 1 - parameter 전달 x
class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:

        robot.sort()
        factory.sort()
        factory = [f for f, l in factory for _ in range(l)]
        # print(factory)

        # dp[i][j]
        # i 번째 로봇과 j 번째 공장이 매칭될 때의 최소 이동 거리를 저장
        dp = [[-1 for _ in range(len(factory))] for _ in range(len(robot))]

        # print(dp)

        def min_distance(currRobot, currFactory):

            if currRobot == len(robot):  # 모든 로봇을 처리했다면 거리 합계는 0
                return 0

            if currFactory == len(factory):  # 모든 공장을 처리했다면 무한대 반환
                return float('inf')

            if dp[currRobot][currFactory] != -1:  # 메모이제이션된 값이 있다면 반환
                return dp[currRobot][currFactory]

            # "현재 로봇과 현재 공장을 매칭하는 경우의 이동거리" 와 "나머지 로봇을 계속 처리할 최소 이동거리" 의 합
            assign = abs(robot[currRobot] - factory[currFactory]) + min_distance(currRobot + 1, currFactory + 1)
            # 현재 로봇을 현재 공장을 건너뛰고 다음 공장을 고려하는 경우의 최소 이동거리
            skip = min_distance(currRobot, currFactory + 1)

            # assign 과 skip 중에 최소값을 dp[currRobot][currFactory]에 저장하여, 해당 로봇과 공장 위치 조합에서의 최소 거리 저장
            dp[currRobot][currFactory] = min(assign, skip)

            return dp[currRobot][currFactory]

        return min_distance(0, 0)


# solution 2 - parameter 전달 o
class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:

        robot.sort()
        factory.sort()
        factory = [f for f, l in factory for _ in range(l)]
        # print(factory)

        # dp[i][j]
        # i 번째 로봇과 j 번째 공장이 매칭될 때의 최소 이동 거리를 저장
        dp = [[-1 for _ in range(len(factory))] for _ in range(len(robot))]

        # print(dp)

        def min_distance(currRobot, currFactory, robot, factory, dp):

            if currRobot == len(robot):  # 모든 로봇을 처리했다면 거리 합계는 0
                return 0

            if currFactory == len(factory):  # 모든 공장을 처리했다면 무한대 반환
                return float('inf')

            if dp[currRobot][currFactory] != -1:  # 메모이제이션된 값이 있다면 반환
                return dp[currRobot][currFactory]

            # "현재 로봇과 현재 공장을 매칭하는 경우의 이동거리" 와 "나머지 로봇을 계속 처리할 최소 이동거리" 의 합
            assign = abs(robot[currRobot] - factory[currFactory]) + min_distance(currRobot + 1, currFactory + 1, robot,
                                                                                 factory, dp)
            # 현재 로봇을 현재 공장을 건너뛰고 다음 공장을 고려하는 경우의 최소 이동거리
            skip = min_distance(currRobot, currFactory + 1, robot, factory, dp)

            # assign 과 skip 중에 최소값을 dp[currRobot][currFactory]에 저장하여, 해당 로봇과 공장 위치 조합에서의 최소 거리 저장
            dp[currRobot][currFactory] = min(assign, skip)

            return dp[currRobot][currFactory]

        return min_distance(0, 0, robot, factory, dp)


# https://www.youtube.com/watch?v=zCwU2ibEEKE


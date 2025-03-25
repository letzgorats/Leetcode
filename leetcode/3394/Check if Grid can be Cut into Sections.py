# solution 1 - sort, intervals - (477ms) - (2025.03.25)
class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:

        rectangles_sorted_by_x = sorted(rectangles, key=lambda x: (x[0], x[2]))
        rectangles_sorted_by_y = sorted(rectangles, key=lambda x: (x[1], x[3]))

        # 세로 컷
        startx, endx = rectangles_sorted_by_x[0][0], rectangles_sorted_by_x[0][2]
        groups = [[startx, endx]]
        for now in rectangles_sorted_by_x[1:]:
            x1, x2 = now[0], now[2]
            if endx <= x1:  # 새 그룹
                startx, endx = x1, x2
                groups.append([startx, endx])
            else:  # 겹친다 -> 합치기
                endx = max(endx, x2)
                groups[-1][1] = endx
            # print("X 그룹:", groups)

        if len(groups) >= 3:
            return True

        # 가로 컷
        starty, endy = rectangles_sorted_by_y[0][1], rectangles_sorted_by_y[0][3]
        groups = [[starty, endy]]
        for now in rectangles_sorted_by_y[1:]:
            y1, y2 = now[1], now[3]
            if endy <= y1:
                starty, endy = y1, y2
                groups.append([starty, endy])
            else:
                endy = max(endy, y2)
                groups[-1][1] = endy
            # print("Y 그룹:", groups)

        if len(groups) >= 3:
            return True

        return False

# solution 2 - sort, intervals - (646ms) - (2025.03.25)
class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:

        def check_sections(intervals):

            intervals.sort()
            sections = 1
            max_end = intervals[0][1]

            for start, finish in intervals[1:]:

                if max_end <= start:
                    sections += 1
                max_end = max(finish, max_end) # 중요!! max_end = finish 를 해버리면 안됨

            return sections >= 3

        x_intervals = [[rect[0], rect[2]] for rect in rectangles]
        y_intervals = [[rect[1], rect[3]] for rect in rectangles]

        return check_sections(x_intervals) or check_sections(y_intervals)

'''
max_end = max(max_end, finish)는 “과거까지 포함한 겹침 범위”를 유지
max_end = finish는 “현재 직사각형만 반영*해서 과거 겹침 정보가 사라질 수 있다.
(ex) [[1,4],[2,3]..] 이라면 max_end 는 4가 유지되어야 하는데,max_end = finish로 하면 
    max_end가 3으로 앞으로 당겨질 우려가 있다.
'''

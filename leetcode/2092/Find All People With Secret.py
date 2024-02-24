class Solution(object):
    def findAllPeople(self, n, meetings, firstPerson):

        shared_set = set([0,firstPerson])

        sorted_meetings = []
        meetings.sort(key=lambda x:x[2]) 

        seen_time = set()

        for a,b,t in meetings:
            if t not in seen_time:
                seen_time.add(t)   
                sorted_meetings.append([])
            sorted_meetings[-1].append((a,b))

        print(sorted_meetings)
        print(seen_time)

        for meeting_group in sorted_meetings:

            people_know_secret = set()
            graph = defaultdict(list)

            for p1,p2 in meeting_group:
                graph[p1].append(p2)
                graph[p2].append(p1)
                if p1 in shared_set:
                    people_know_secret.add(p1)
                if p2 in shared_set:
                    people_know_secret.add(p2)
            
            queue = deque((people_know_secret))

            while queue:

                curr = queue.popleft()
                shared_set.add(curr)
                for neighbor in graph[curr]:
                    if neighbor not in shared_set:
                        shared_set.add(neighbor)
                        queue.append(neighbor)

        return list(shared_set)

class Solution(object):
    def numBusesToDestination(self, routes, source, target):
        """
        :type routes: List[List[int]]
        :type source: int
        :type target: int
        :rtype: int
        """
        
        if source == target :
            return 0

        graph = defaultdict(set)

        for bus_number, stops in enumerate(routes):
            
            for stop in stops:
                graph[stop].add(bus_number)

        queue = deque([(source,0)]) # stop, count

        visited_stops = set()
        visited_buses = set()


        while queue:

            stop, count = queue.popleft()

            if stop == target :
                return count
            
            # Since our graph stores all buses going to a stop

            for bus_number in graph[stop]:
                
                 # We dont want to travel in same bus 
                 # as we might stuck into loop and reach nowhere
                if bus_number not in visited_buses:
                    visited_buses.add(bus_number)

                    # Now we are in a bus, so we will travel all the stops 
                    # that bus goes to but again, 
                    # we only want to go to stops we haven't visited
                    for stop in routes[bus_number]:
                        if stop not in visited_stops:
                            visited_stops.add(stop)
                            queue.append((stop,count+1))

        return -1

        return answer

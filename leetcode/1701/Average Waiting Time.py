class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:

        start = customers[0][0]
        waiting = 0
        for arrival, time in customers:

            if start < arrival:
                start = arrival
            serve = (start + time)
            waiting += (serve - arrival)
            start = serve

        # print('%.5f'%(waiting/len(customers)))
        # print('{:.5f}'.format(waiting*1.0/len(customers)))
        # print('{:.5f}'.format(float(waiting)/len(customers)))

        return waiting / len(customers)
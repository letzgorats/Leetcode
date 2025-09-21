# Wrong Answer
from collections import defaultdict
import heapq
from typing import List
# [shop,movie,price]

class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        self.queue = [] self.shops = defaultdict(list)
        self.unrented = defaultdict(list)
        self.rented_queue = []
        for s,m,p in entries: self.shops[s].append((p,m))
            self.unrented[m].append((p,s))
            heapq.heappush(self.queue,self.shops[s])

    def search(self, movie: int) -> List[int]:
        unrented_queue = []
        tmp = []
        for p,s in self.unrented[movie]:
            heapq.heappush(unrented_queue,(p,s))

        while unrented_queue:
            _,s = heapq.heappop(unrented_queue)
            tmp.append(s)

        return tmp

    def rent(self, shop: int, movie: int) -> None:

        for ps,ms in self.shops[shop]:

            if ms == movie:
                p1, m1 = heapq.heappop(self.queue)
                for i, (pu,su) in enumerate(self.unrented[movie]):
                    if su == shop:
                        heapq.heappush(self.rented_queue, (pu,su,movie))
                        del self.unrented[movie][i]
                        return
    def drop(self, shop: int, movie: int) -> None:

        for i, (pu,su) in enumerate(self.unrented[movie]):
            if su == shop:
                del self.unrented[movie][i]
                break

    def report(self) -> List[List[int]]:

        res = []
        minp = 10**5
        while self.rented_queue and len(res)<5:
            p,s,m = heapq.heappop(self.rented_queue)
            res.append([s,m])

        return res

# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()

# solution 1 - (SortedList,hashtable,priority queue) - (561ms) - (2025.09.21)
from collections import defaultdict
from sortedcontainers import SortedSet

class MovieRentingSystem:

    def __init__(self, n: int, inventory: List[List[int]]):
        self.available_movies = defaultdict(SortedSet)  # movie -> available (price, shop)
        self.movie_price = {}                           # (movie, shop) -> price
        self.rented_set = SortedSet()                   # rented movies: (price, shop, movie)

        # Load initial inventory into data structures
        for shop, movie, price in inventory:
            self.available_movies[movie].add((price, shop))
            self.movie_price[(movie, shop)] = price

    def search(self, movie: int) -> List[int]:
        # Return up to 5 cheapest shops that have the movie available
        top_shops = []
        for price, shop in self.available_movies[movie]:
            top_shops.append(shop)
            if len(top_shops) == 5:
                break
        return top_shops

    def rent(self, shop: int, movie: int) -> None:
        # Move movie from available -> rented
        price = self.movie_price[(movie, shop)]
        self.rented_set.add((price, shop, movie))
        self.available_movies[movie].discard((price, shop))

    def drop(self, shop: int, movie: int) -> None:
        # Move movie from rented -> available
        price = self.movie_price[(movie, shop)]
        self.rented_set.discard((price, shop, movie))
        self.available_movies[movie].add((price, shop))

    def report(self) -> List[List[int]]:
        # Return up to 5 cheapest rented movies
        top_rented = []
        for price, shop, movie in self.rented_set:
            top_rented.append([shop, movie])
            if len(top_rented) == 5:
                break
        return top_rented
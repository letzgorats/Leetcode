class FoodRatings(object):

    def __init__(self, foods, cuisines, ratings):
        """
        :type foods: List[str]
        :type cuisines: List[str]
        :type ratings: List[int]
        """
        self.foodMap = {}  # food : rating, cuisine
        self.cuisineMap = {}  # cuisine : food (heap)

        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.foodMap[food] = [rating,cuisine]
    
            if cuisine not in self.cuisineMap:
                self.cuisineMap[cuisine] = []
            heapq.heappush(self.cuisineMap[cuisine], (-rating, food))

            # changeRating 함수에서 힙(heap)에 새로운 요소를 추가하는 대신 
            # 기존 요소를 변경하는 것은 힙의 특성상 직접적으로는 불가능

            # changeRating 함수에서 음식의 등급을 변경할 때 힙에 새로운 요소를 추가하는 것은 
            # 힙의 무결성을 유지하기 위한 최선의 방법.
            
            # 새로운 등급으로 음식을 힙에 다시 추가하면, 힙은 자동으로 새로운 요소를 
            # 올바른 위치로 재정렬

    def changeRating(self, food, newRating):
        """
        :type food: str
        :type newRating: int
        :rtype: None
        """
        self.foodMap[food][0] = newRating
        heapq.heappush(self.cuisineMap[self.foodMap[food][1]],(-newRating,food))
        

    def highestRated(self, cuisine):
        """
        :type cuisine: str
        :rtype: str
        """
        while self.cuisineMap[cuisine]:
            
            rating, food = self.cuisineMap[cuisine][0]
            # 다음 요소를 확인해야 함. 일치하는 경우에만 해당 음식을 반환
            if -rating == self.foodMap[food][0]:   
               return food
            heapq.heappop(self.cuisineMap[cuisine]) # 힙에서 최상위 요소 제거
            

            # changeRating 함수가 호출될 때, 음식의 등급이 변경되면 힙에 있는 순서가 
            # 더 이상 유효하지 않을 수 있다. 
            # 예를 들어, 힙의 루트에 있던 음식의 등급이 낮아지면, 그 음식은 더 이상 
            # 가장 높은 등급의 음식이 아니게 된다. 하지만, 그 음식은 여전히 힙의 루트에 
            # 남아 있기 때문에, 우리는 highestRated 함수에서 
            # 이를 확인하고 필요에 따라 제거해야 함.
        
# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)

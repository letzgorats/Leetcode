# solution 1 - queue,defaultdict,zip,hash table - (54ms) - (2025.03.21)
from collections import deque, defaultdict
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:

        # 각 재료를 key 로 하고, 해당 재료가 필요한 레시피들의 리스트를 value
        graph = defaultdict(list)  # key-> value : ing -> recipe

        # 각 레시피가 만들기 위해 필요한 재료의 개수를 저장
        indegree = defaultdict(int)  # Key -> value : recipe -> count

        for recipe, ingre_list in zip(recipes, ingredients):
            indegree[recipe] = len(ingre_list)
            for ing in ingre_list:
                graph[ing].append(recipe)

        answer = []
        q = deque(supplies)
        while q:

            ingre = q.popleft()

            for recipe in graph[ingre]:
                indegree[recipe] -= 1
                if indegree[recipe] == 0:
                    answer.append(recipe)
                    q.append(recipe)

        return answer

# solution 2 - greedy - (9462ms) - (2025.03.21)
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:

        candi = set()

        for i in range(len(recipes)):
            for idx, ingre in enumerate(ingredients):

                if len(set(ingre) & set(supplies)) == len(ingre):
                    supplies.append(recipes[idx])
                    candi.add(recipes[idx])

        return list(candi)

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        def dfs(course):
            if course in path:
                return True
            if not graph[course]:
                return False
            path.add(course)
            for c in graph[course]:
                if dfs(c):
                    return True
            path.remove(course)
            graph[course] = []
            return False
        
        graph = {course:[] for course in range(numCourses)} 
        for course, pre in prerequisites:
            graph[pre].append(course)
        
         
        path = set()
        for course in range(numCourses):
            if(dfs(course)):
                return False
        
        return True        
import heapq
from collections import deque

def solution(jobs):
    tasks = deque(sorted([(x[1], x[0]) for x in jobs], key=lambda x: (x[1], x[0])))
    q = []
    heapq.heappush(q, tasks.popleft())
    current_time, total_response_time = 0, 0
    while len(q) > 0:
        dur, arr = heapq.heappop(q)
        current_time = max(current_time + dur, arr + dur)
        total_response_time += current_time - arr
        while len(tasks) > 0 and tasks[0][1] <= current_time:
            heapq.heappush(q, tasks.popleft())
        if len(tasks) > 0 and len(q) == 0:
            heapq.heappush(q, tasks.popleft())
    return total_response_time // len(jobs)
  
# 시간 초과 발생
# from collections import deque
# def solution(jobs):
#     jobs = sorted(jobs, key = lambda x : x[0])
#     q = deque([jobs[0]] + sorted(jobs[1:], key = lambda x : x[1]))
#     REQUEST, SPEND = 0, 1
#     current_time = 0
#     total_time = []

    
#     while True:
#         x = q.popleft()
#         if current_time < x[REQUEST]:
#             y = q.popleft()
#             q.appendleft(x)
#             q.appendleft(y)
#         else:
#         total_time.append((current_time - x[REQUEST]) + x[SPEND])
#         current_time += x[SPEND]
            
#         if len(q) == 0:
#             break
    
#     return sum(total_time) // len(jobs)
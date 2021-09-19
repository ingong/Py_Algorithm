from collections import deque

def solution(bridge_length, weight, truck_weights):
    truck_waiting = deque(truck_weights)
    on_bridge = deque()
    time = 0
    
    while True:
        if on_bridge and on_bridge[0].get('progress') == bridge_length:
            on_bridge.popleft()
        else:
            pass
        
        if truck_waiting and (sum([truck.get('w') for truck in on_bridge]) + truck_waiting[0] <= weight):
            on_bridge.append({'w' : truck_waiting.popleft(), 'progress': 0})
        else: 
            pass
        
        for truck in on_bridge:
            truck['progress'] += 1
        
        time += 1
        if len(on_bridge) == 0 and len(truck_waiting) == 0:
            break
            
    return time

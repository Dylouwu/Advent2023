import time

def minimum(distances, visited):
    min_dist = 100000
    min_index = -1
    for i in range(len(distances)):
        if distances[i] < min_dist and i not in visited:
            min_dist = distances[i]
            min_index = i
    return min_index

def dijkstra(input_map, start):
    num_nodes = len(input_map)
    distances = [10000] * num_nodes
    visited = []
    
    distances[start] = 0
    for i in range(num_nodes):
        current = minimum(distances, visited)
        visited.append(current)

        for j in range(num_nodes):
            if input_map[current][j] != '0':
                new_distance = distances[current] + int(input_map[current][j])
                turns = (new_distance - distances[start]) // 3
                new_distance += turns

                if new_distance < distances[j]:
                    distances[j] = new_distance
    return distances


       
def part1():
    start_time = time.time()
    input_map = []
    result = 0
    with open("input/17.txt") as f:
        for x in f:
            input_map.append(x.strip())
    result = dijkstra(input_map, 0)
    end_time = time.time()
    print(f'Time to run Part 1 : {end_time - start_time}s')
    return result

def part2():
    start_time = time.time()
    input_map = []
    result = 0
    with open("input/17.txt") as f:
        for x in f:
            input_map.append(x.strip())
            
    end_time = time.time()
    print(f'Time to run Part 2 : {end_time - start_time}s')
    return result

if __name__ == "__main__":
    print(part1())
    print(part2())
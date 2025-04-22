# sacs_algorithm.py

from collections import deque

# SACS parameters (tunable weights)
alpha = 1.0
beta = 1.0
gamma = 0.5

def bfs_distance(graph, start, target):
    visited = set()
    queue = deque([(start, 0)])
    while queue:
        node, dist = queue.popleft()
        if node == target:
            return dist
        if node not in visited:
            visited.add(node)
            for neighbor in graph.get(node, []):
                queue.append((neighbor, dist + 1))
    return float('inf')  # Not reachable

def compute_scores(cache, pivot, graph):
    scores = {}
    for page in cache:
        dist = bfs_distance(graph, pivot, page)
        freq = cache[page]['frequency']
        rec = cache[page]['recency']
        score = alpha * dist - beta * freq + gamma * rec
        scores[page] = score
    return scores

def sacs_eviction(cache, pivot, graph):
    scores = compute_scores(cache, pivot, graph)
    evict_page = max(scores, key=scores.get)
    return evict_page

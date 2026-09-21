def count_components(n: int, edges: list[list[int]]) -> int:
    graph = [[] for _ in range(n)]
    for first, second in edges:
        graph[first].append(second)
        graph[second].append(first)

    visited = set()
    components = 0
    for node in range(n):
        if node in visited:
            continue
        components += 1
        visited.add(node)
        stack = [node]
        while stack:
            current = stack.pop()
            for neighbor in graph[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)
    return components


if __name__ == "__main__":
    assert count_components(5, [[0, 1], [1, 2], [3, 4]]) == 2
    print(2)

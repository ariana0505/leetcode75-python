from collections import deque


def can_finish(num_courses: int, prerequisites: list[list[int]]) -> bool:
    graph = [[] for _ in range(num_courses)]
    indegree = [0] * num_courses

    for course, prerequisite in prerequisites:
        graph[prerequisite].append(course)
        indegree[course] += 1

    ready = deque(course for course, degree in enumerate(indegree) if degree == 0)
    completed = 0
    while ready:
        course = ready.popleft()
        completed += 1
        for next_course in graph[course]:
            indegree[next_course] -= 1
            if indegree[next_course] == 0:
                ready.append(next_course)

    return completed == num_courses


if __name__ == "__main__":
    assert can_finish(2, [[1, 0]])
    assert not can_finish(2, [[1, 0], [0, 1]])
    print(False)


# Two-pointer approach to find the container that holds the most water
height: list[int] = [1, 3, 7, 5, 3, 2, 6, 9, 1]
max_area: int = 0
l, r = 0, len(height) - 1

while l < r:
    area: int = min(height[l], height[r]) * (r - l)
    max_area = max(max_area, area)

    if height[l] < height[r]:
        l += 1
    else:
        r -= 1

print(max_area)

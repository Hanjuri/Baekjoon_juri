def solution(H, W, heights):
  left_max = [0] * W
  left_max[0] = heights[0]
  for i in range(1, W):
    left_max[i] = max(left_max[i-1], heights[i])
  right_max = [0] * W
  right_max[-1] = heights[-1]
  for i in range(W-2, -1, -1):
    right_max[i] = max(right_max[i+1], heights[i])
  total_water = 0
  for i in range(W):
    rain_water = min(left_max[i], right_max[i]) - heights[i]
    total_water += rain_water
  return total_water

H, W = map(int, input().split())
heights = list(map(int, input().split()))
print(solution(H,W,heights))
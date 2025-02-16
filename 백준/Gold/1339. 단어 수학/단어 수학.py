from collections import defaultdict

def solution(N, arr):
  weight = defaultdict(int)
  for word in arr:
    for i, char in enumerate(word):
      weight[char] += 10 ** (len(word) - i - 1)

  sorted_chars = sorted(weight.items(), key=lambda x : -x[1])

  num_mapping = {}
  num = 9
  for char, _ in sorted_chars:
    num_mapping[char] = num
    num -= 1

  def word_to_number(word):
    result = 0
    for i, c in enumerate(word):
      result += num_mapping[c] * (10 ** (len(word)-i-1))
    return result
  total = sum(word_to_number(word) for word in arr)
  return total

N = int(input())
arr = [input() for _ in range(N)]
print(solution(N, arr))
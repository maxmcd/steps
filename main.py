from collections import defaultdict

def getSteps(n):
  numbers = range(1, n)
  sums = defaultdict(dict)
  index = 0
  for number in numbers:
    toSum = numbers[:]
    toSum.pop(index)
    for x in toSum:
      pair = [x, number]
      pair.sort()
      sums[x + number][pair[0]] = pair[1]
    index += 1
  print sums
  solutions = []
  def walk(key, value):
    out = sums[value].get(key - 1)
    if out:
      solutions.append([key-1, value, out])

  for s in sums:
    for key in sums[s]:
      # solutions.append()
      walk(key, sums[s][key])
  print solutions


getSteps(7)

# {3: {1: 2}, 4: {1: 3}, 5: {1: 4, 2: 3}, 6: {1: 5, 2: 4}, 7: {1: 6, 2: 5, 3: 4}}


# 7
# 1,6
# 1,2,4

# 2,5
# 3,4

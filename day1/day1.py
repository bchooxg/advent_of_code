import re

file1 = open('./day1/day1_input.txt', 'r')
# file1 = open('./day1/test.txt', 'r')
lines = file1.readlines()

cnt = 0

for l in lines:
  curr = ""

  filtered = re.sub('\D', '', l)
  print("filtered:" + filtered)
  # Skip if filtered is empty
  if filtered == "":
    continue
  # Get the first and last if filtered has more than 2
  if len(filtered) >= 2:
    curr = filtered[0] + filtered[-1]
  # if one digit, double it
  elif len(filtered) == 1:
    curr = filtered[0] + filtered[0]

  print("curr:" + curr)
  if curr != "":
    cnt += int(curr)
  # cnt += int(curr)

print("final cnt: ", cnt)
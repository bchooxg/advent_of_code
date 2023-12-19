import re

file1 = open('./day1/day1_input.txt', 'r')
# file1 = open('./day1/demo.txt', 'r')
# file1 = open('./day1/test.txt', 'r')
lines = file1.readlines()


NUMBERS = {
  "one": 1,
  "two": 2,
  "three": 3,
  "four": 4,
  "five": 5,
  "six": 6,
  "seven": 7,
  "eight": 8,
  "nine": 9,
}

3-5

cnt = 0

for l in lines:
  nums_found = []

  p1 , p2 = 0,0

  # Increment p2 until finds a digit or p2 - p1 > lenght of max chars in NUMBERS
  while p1 < len(l):
    # Check if p1 is a digit
    # print("l[p1]: ", l[p1])
    if l[p1].isdigit():
      nums_found.append(int(l[p1]))
      p1 += 1
      continue
    # Else move the pointer up to 5 chars ahead and see if it matches a number
    for i in range(6):
      p2 = p1 + i
      if p2 > len(l):
        break

      curr_str = l[p1:p2]
      if curr_str in NUMBERS:
        nums_found.append(NUMBERS[curr_str])
    p1 += 1

  print("Current Line : " + l + " Nums found: " + str(nums_found) )
  cnt_found = 0
  if len(nums_found) == 1:
    cnt_found = int(str(nums_found[0]) + str(nums_found[0]))
    cnt += cnt_found
  elif len(nums_found) > 1:
    cnt_found =  int(str(nums_found[0]) + str(nums_found[-1]))
    cnt +=cnt_found
  print("cnt_found: ", cnt_found)



print("\nfinal cnt: ", cnt)
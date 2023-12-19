import math

file1 = open('./day2/day2_input.txt', 'r')
# file1 = open('./day1/demo.txt', 'r')
# file1 = open('./day1/test.txt', 'r')
lines = file1.readlines()

# Need to find games that does not exceed these numebr of cubes
# only 12 red cubes, 13 green cubes, and 14 blue cubes?

COLORS = {
  "red": 12,
  "green": 13,
  "blue": 14,
}
res = 0
for l in lines:
  # Strip the new line
  valid_game = True
  l = l.strip()
  splitted = l.split(":")
  # Get the game number
  game = splitted[0].split("Game ")[1].strip()
  print("game: ", game)
  min_map = {
    "red": 0,
    "green": 0 ,
    "blue": 0,
  }
  # Get the iters per game
  iters = splitted[1].split(";")
  for i in iters:
    sub_iters = [x.strip() for x in i.split(',')]
    print("sub_iters: ", sub_iters)
    for colors in sub_iters:
      cnt,color = colors.split(" ")
      # print(f"cnt: {cnt}, color: {color}")
      min_map[color] = max(min_map[color], int(cnt))
  print("min_map: ", min_map)
  res_sum = 1
  for k,v in min_map.items():
    res_sum *= v
  print("res_sum: ", res_sum)
  res += res_sum



print("final cnt: ", res)
  # print("iters: ", iters)
# Validate a minesweeper interior block
# block_data is a two dimensional array containing the data from a 3 x 3 grid of squares
# We are assuming that we are only checking interior blocks for now
# Return value should be a string that says either Valid or Invalid (with some hints as to why it's invlaid)
def validate( block_data ):
  # Check whether the centre block is a bomb, a number, or an invalid input

  return validation


grid = [
  [-1,2,1],
  [1,3,-1],
  [0,2,-1]
]

row = 0
column = 0
bomb = 0

while row < 3:
  while column < 3:
    #print("here")
    value = grid [row][column]
  #  print(row)
   # print(column)
    #print(value)
    if value == -1:
      bomb = bomb + 1
      column = column + 1
     # print(column)
    else:
      column = column + 1
  row = row + 1
  column = 0
#print("the number of bombs are", bomb)

middle_grid = grid[1][1]
print("The middle value is", middle_grid)
if middle_grid == bomb:
 # print("Valid")
  validation = "Valid"
else:
#  print("Invalid, check interior block")
  validation = "Invalid; check the middle block"
print (validate(grid))

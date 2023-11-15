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
#row is x, column is y, bomb is z
x = [0]
y = [0]
z = [0]

for x in range [3]:
  for y in range [3]:
    #print("here")
    value = grid [x][y]
  #  print(x)
   # print(y)
    #print(value)
    if value == -1:
      z = z + 1
      y = y + 1
     # print(column)
    else:
      y = y + 1
  x = x + 1
  y = 0
#print("the number of bombs are", z)

middle_grid = grid[1][1]
print("The middle value is", middle_grid)
if middle_grid == z:
 # print("Valid")
  validation = "Valid"
else:
#  print("Invalid, check interior block")
  validation = "Invalid; check the middle block"
print (validate(grid))

# Validate a minesweeper interior block
# block_data is a two dimensional array containing the data from a 3 x 3 grid of squares
# We are assuming that we are only checking interior blocks for now
# Return value should be a string that says either Valid or Invalid (with some hints as to why it's invlaid)
def validate( block_data ):
  # Check whether the centre block is a bomb, a number, or an invalid input

  return validation


grid = [
  [-1,1,0],
  [1,1,0],
  [0,0,0]
]

row = 0
column = 0
bomb = 0

while row < 3:
  while column < 3:
    print("here")
    value = grid [row][col]
    print(row)
    print(column)
    print(value)
    if value == -1:
      bombs = bombs + 1
      column = column + 1
      print(column)
    else:
      column = column + 1
  row = row + 1
  column = 0
  
middle_grid = grid[1][1]

if middle_grid == bombs:
  validation = "Valid"
else:
  validation = "Invalid; check the middle block"
print (validate(grid))

# Give instruction where to put treasure

row1 = ["1","2","3"]
row2 = ["4","5","6"]
row3 = ["7","8","9"]

# add lists into nest of lists 
map = [row1, row2, row3]

# print each row on different line
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

# Split two digit location number into separate characters in the list
direction = (list(position))

# change characters in direction list into integers and get position for row and column
row_choice = int(direction[0])-1
column_choice = int(direction[1])-1

# replace character in position row_choice / column_choice with x
map[row_choice][column_choice] = "x"

print(f"{row1}\n{row2}\n{row3}")



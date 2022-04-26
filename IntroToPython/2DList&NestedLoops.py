# lets make 2D lists

number_grid_list = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [0]
]
print(number_grid_list[1])
print(number_grid_list[1][2])
print("")

for row in number_grid_list:
    #print(row)
    for column in row:
        print(column)
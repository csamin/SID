# string covnersion to find the exact column
def col_conversion(col_str):
    '''
    col_str : str
            string containing column number in characters
    '''
    exp = 0
    col_num = 0
    for char in reversed(col_str):
        col_num += (ord(char) - ord('A') + 1) * (26 ** exp)
        exp += 1

    return col_num


# calculation for the coordinates
def find_coordinates(box_num, x_val, y_val, z_val):    
    '''
    box_num : int
                number of the box
        x_val, y_val, z_val: int
                coordinates of the box        
    '''
    x_coord = ((int(box_num[1]) - 1) * x_val) + (x_val * 0.5)
    y_coord = (col_conversion(box_num[2:]) - 1) * y_val
    z_coord = (int(box_num[0]) - 1) * z_val

    return [x_coord, y_coord, z_coord]


# gives output of the coordinates for a specifix box

print(find_coordinates("33A", 500, 200 , 300))
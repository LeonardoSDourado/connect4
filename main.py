'''
This program is the game connect 4.
'''

def draw(matrix):
    columns = 15
    rows = 6
    column_counter = 0
    row_counter = 0
    print(" 1 2 3 4 5 6 7 ")
    for row in range(rows):
        column_print = True
        for column in range(columns):
            if column_print:
                print("|",sep='',end='')
                column_print = False
            else:
                field = matrix[column_counter][row_counter]
                print(u'{0}'.format(field),sep='',end='')
                column_counter += 1
                
                if column_counter == 7:
                    column_counter = 0
                    row_counter += 1
                    
                column_print = True
        print("\n---------------")

def check_winner(matrix, player):
    horizontal = 0
    vertical = 0
    diagonal = 0
    symbol = get_symbol(player)
    
    for column_number in range(len(matrix)):
        for row_number in range(len(matrix[column_number])):
            aux_column_number = len(matrix) - 4
            aux_row_number = len(matrix[column_number]) - 4

            if row_number <= aux_row_number and column_number <= aux_column_number:
                for count in range(4):
                    if symbol == matrix[column_number+count][row_number+count]:
                        diagonal += 1
                    else:
                        diagonal = 0
                if diagonal == 4:
                    return True
                else:
                    diagonal = 0

            if row_number >= 3 and column_number <= 3:
                for count in range(4):
                    if symbol == matrix[column_number+count][row_number-count]:
                        diagonal += 1
                    else:
                        diagonal = 0
                if diagonal == 4:
                    return True
                else:
                    diagonal = 0

            if row_number <= aux_row_number:
                for count in range(4):
                    if symbol == matrix[column_number][row_number+count]:
                        vertical += 1
                    else:
                        vertical = 0
                if vertical == 4:
                    return True
                else:
                    vertical = 0

            if column_number <= aux_column_number:
                for count in range(4):
                    if symbol == matrix[column_number+count][row_number]:
                        horizontal += 1
                    else:
                        horizontal = 0
                if horizontal == 4:
                    return True
                else:
                    horizontal = 0
    return False

def change_player(player):
    if player == "1":
        return "2"
    else:
        return "1"
    
def get_symbol(player):
    if player == "1":
        symbol = '\u2B24'
    else:
        symbol = '\u25B3'
    return symbol

def find_position(column):
    index = -1
    for row in range(len(column)):
        if column[index] == " ":
            return index
        else:
            index -= 1
    return False

def set_row_value(matrix, chosen_column, player):
    c_index = 0
    c_index = find_position(matrix[int(chosen_column)])
    if not c_index:
        return False
    else:
        matrix[chosen_column][c_index] = get_symbol(player)
        return matrix[chosen_column]

def isFull(matrix):
    full = True
    for column in matrix:
        for field in column:
            if field != " ":
                full = full and True
            else:
                full = full and False
    return full
            

def play():
    matrix = list()
    aux_matrix = list()
    player = "1"
    
    for i in range(7):
        matrix.append([" "," "," "," "," "," "])

    draw(matrix)

    while True:
        
        print("Player",player)
        chosen_column = (int(input("Enter which column you want: "))-1)
        
        if chosen_column > 6 or chosen_column < 0:
            print("Please choose columns among 1 and 7")
            continue
        
        aux_matrix = set_row_value(matrix, chosen_column, player)
        
        if aux_matrix:
            matrix[chosen_column] = aux_matrix
        
        if not aux_matrix:
            print("Column",(chosen_column+1),"is full, please choose another!")
            continue
        
        draw(matrix)
        winner = check_winner(matrix, player)
        
        if winner:
            print("The player", player,"won!")
            break

        if isFull(matrix):
            print("All fields were filled, nobody won!")
            break
            
        player = change_player(player)
        
if __name__=="__main__":
    play()

def add_to_coords(direction, coords):
    if direction == "U":
        coords[1] += 1
    elif direction == "D":
        coords[1] -= 1
    elif direction == "L":
        coords[0] -= 1
    elif direction == "R":
        coords[0] += 1

    return coords

def main():
    size = 50000
    matrix = [[0 for x in range(size)] for y in range(size)]
   
    line_number = 0
    min_distance = 1000000

    with open("3_1_input.txt", "r") as file:
        # for each line in the file and split by comma and convert to int in a list
        for line in file:
            line_number += 1
            ## each line is comma separated. first char is a direction, the rest is a number of steps
            ## split by comma to get each direction and number of steps
            ## convert the number of steps to an int
            ## convert the direction to a list of directions
            ## append the direction and number of steps to a list
            ## repeat for the second line
            ## convert the list of directions to a set
            ## get the intersection of the two sets
            ## get the manhattan distance of the intersection
            ## get the minimum manhattan distance
            coords = [int(size/2),int(size/2)]
            instructions = line.strip().split(",")
            for i in range(len(instructions)):
                instructions[i] = [instructions[i][0], int(instructions[i][1:])]
                print(instructions[i]) 
                for j in range(instructions[i][1]):
                    coords = add_to_coords(instructions[i][0], coords)
                    if matrix[coords[0]][coords[1]] == 1 and line_number == 2:
                        print("Intersection at: ", coords)
                        #calculate manhattan distance from center
                        manhattan_distance = abs(coords[0] - int(size/2)) + abs(coords[1] - int(size/2))
                        print("Manhattan distance: ", manhattan_distance)
                        if manhattan_distance < min_distance:
                            min_distance = manhattan_distance
                    matrix[coords[0]][coords[1]] = line_number 
        
    print("Minimum distance: ", min_distance)
    #write matrix to file
    with open("3_1_matrix.txt", "w") as file:
        for i in range(size):
            for j in range(size):
                file.write(str(matrix[i][j]))
            file.write("\n")
    

if __name__ == "__main__":
    main()
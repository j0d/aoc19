class cable_step:
    def __init__(self, step, cable):
        self.step = step
        self.cable = cable

def update_coords(coords, direction):
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
    matrix = {}
    line_number = 0
    min_distance = 1000000

    with open("3_1_input.txt", "r") as file:
        for line in file:
            line_number += 1
            coords = [0, 0]
            steps = 0
            for instruction in line.strip().split(","):
                direction = instruction[0]
                distance = int(instruction[1:])
                for _ in range(distance):
                    coords = update_coords(coords, direction)
                    steps += 1
                    key = tuple(coords)
                    if key not in matrix:
                        matrix[key] = cable_step(steps, line_number)
                    ### elif key in matrix: if corssing with same line number, ignore
                    elif matrix[key].cable != line_number:
                            # Calculate distance as number of step of each cable
                            distance = matrix[key].step + steps
                            if distance < min_distance:
                                min_distance = distance
                            print(f"Intersection at: {key}, Distance: {distance}")
    
    
    # Example of accessing the matrix
    #for key, value in matrix.items():
        #print(f"Coords: {key}, Step: {value.step}, Cable: {value.cable}")

    # write the matrix to a file as a matrix. Take max and min of x and y to get the size of the matrix
    # min_x = min(matrix.keys(), key=lambda x: x[0])[0]
    # max_x = max(matrix.keys(), key=lambda x: x[0])[0]
    # min_y = min(matrix.keys(), key=lambda x: x[1])[1]
    # max_y = max(matrix.keys(), key=lambda x: x[1])[1]
    # size_x = max_x - min_x + 1
    # size_y = max_y - min_y + 1
    # print(f"Size: {size_x} x {size_y}")
    # with open("3_2_matrix.txt", "w") as file:
    #     for y in range(size_y):
    #         for x in range(size_x):
    #             key = (x + min_x, y + min_y)
    #             if key in matrix:
    #                 file.write(str(matrix[key].cable))
    #             else:
    #                 file.write(".")
    #         file.write("\n")

    print(f"Minimum distance: {min_distance}")

if __name__ == "__main__":
    main()
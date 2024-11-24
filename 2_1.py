def calc_fuel_req(mass):
    fuel = max(mass // 3 - 2,0)
    if fuel == 0:
        return 0
    else:
        return fuel + calc_fuel_req(fuel)
    

def process_codes(codes):
    for i in range(0, len(codes), 4):
        opcode = codes[i]
        if opcode == 99:
            return codes
        elif opcode == 1:
            codes[codes[i+3]] = codes[codes[i+1]] + codes[codes[i+2]]
        elif opcode == 2:
            codes[codes[i+3]] = codes[codes[i+1]] * codes[codes[i+2]]
        else:
            return codes

    return codes

def main():
    with open("2_1.txt", "r") as file:
        # for each line in the file and split by comma and convert to int in a list
        for line in file:
            codes = [int(x) for x in line.strip().split(",")]
            print(codes)
            process_codes(codes)
            print(codes)

if __name__ == "__main__":
    main()
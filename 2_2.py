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
            org_mem = [int(x) for x in line.strip().split(",")]
            print(org_mem)
            
            codes = org_mem.copy()
            for noun in range(100):
                for verb in range(100):
                    codes[1] = noun
                    codes[2] = verb
                    process_codes(codes)
                    if codes[0] == 19690720:
                        print(100 * noun + verb)
                        return
                    codes = org_mem.copy()

if __name__ == "__main__":
    main()
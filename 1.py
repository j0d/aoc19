def calc_fuel_req(mass):
    fuel = max(mass // 3 - 2,0)
    if fuel == 0:
        return 0
    else:
        return fuel + calc_fuel_req(fuel)

def main():
    total_fuel = 0
    with open("1_1.txt", "r") as file:
        for line in file:
            total_fuel += calc_fuel_req(int(line.strip()))
    print(total_fuel)

if __name__ == "__main__":
    main()
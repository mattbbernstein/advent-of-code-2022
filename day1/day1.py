import csv

def main():
    inventory = []
    with open('data/day1.csv') as datafile:
        reader = csv.reader(datafile)
        calories = 0
        for row in reader:
            if row:
                calories += int(row[0])
            else:
                inventory.append(calories)
                calories = 0
    inventory = sorted(inventory, reverse = True)
    print(inventory[0:3])
    print(sum(inventory[0:3]))

if __name__ == "__main__":
    main()
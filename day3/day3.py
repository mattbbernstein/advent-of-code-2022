import csv

def main():

    with open("data/day3.csv") as datafile:
    # PART 1
    #     reader = csv.reader(datafile)
    #     total = 0
    #     for row in reader:
    #         items = list(row[0])
    #         pocket1 = items[0:len(items)//2]
    #         pocket2 = items[len(items)//2:]
    #         shared = list(set(pocket1).intersection(pocket2))[0]

    # PART 2
        lines = datafile.read().splitlines()
        total = 0
        for sog in range(0, len(lines), 3):
            group = lines[sog:sog+3]
            shared = list(set(group[0]).intersection(group[1]).intersection(group[2]))[0]
        
            if shared.islower():
                total += ord(shared) - ord('a') + 1
            else:
                total += ord(shared) - ord('A') + 27
        print(total)

if __name__ == "__main__":
    main()
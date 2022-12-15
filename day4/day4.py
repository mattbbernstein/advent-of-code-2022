import csv

def fully_contains(outer, inner):
    return (int(outer[0]) <= int(inner[0]) and
            int(outer[1]) >= int(inner[1]))

def overlaps(sec1, sec2):
    range1 = set(range(int(sec1[0]), int(sec1[1])+1))
    range2 = set(range(int(sec2[0]), int(sec2[1])+1))
    return (range1.intersection(range2) != set())

def main():
    with open("data/day4.csv") as datafile:
        reader = csv.reader(datafile)
        problems = 0
        for row in reader:
            sec1 = row[0].split('-')
            sec2 = row[1].split('-')
            # problems += fully_contains(sec1, sec2) or fully_contains(sec2, sec1)
            problems += overlaps(sec1, sec2)
        print(problems) 

if __name__ == "__main__":
    main()
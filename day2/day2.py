import csv

def main():
    shape = {
        "A":1,
        "B":2,
        "C":3,
        "X":1,
        "Y":2,
        "Z":3
    }
    beats = {
        "A":"Z",
        "B":"X",
        "C":"Y",
        "X":"C",
        "Y":"A",
        "Z":"B"
    }
    WIN = 6
    LOSE = 0
    DRAW = 3
    with open('data/day2.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=" ")
        total = 0
        for row in reader:
            opponent = row[0]
            # PART 1
            # me = row[1]
            # outcome = DRAW
            # if beats[me] == opponent: outcome = WIN
            # elif beats[opponent] == me: outcome = LOSE
            
            # PART 2
            need = row[1]
            if need == "X":
                outcome = LOSE
                me = beats[opponent]
            elif need == "Y":
                outcome = DRAW
                me = opponent
            elif need == "Z":
                outcome = WIN
                me = list({key for key in beats if beats[key] == opponent})[0]
            total += shape[me] + outcome
    print(total)

if __name__ == "__main__":
    main()
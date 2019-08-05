import sys, csv

name = sys.argv[1]
entire_csv = []

with open('c:\\args\\scoreboard.txt', 'r') as f:
    c = csv.reader(f)

    if name == 'score':
        for row in c:
            print(row)

    else:
        for row in c:
            if row[0] == name:
                int_conv = int(row[1])
                update_value = int_conv + 1
                row[1] = str(update_value)
                entire_csv.append(row)
                continue

            else:
                entire_csv.append(row)

if name != 'score':
    with open('c:\\args\\scoreboard.txt', 'w') as f:
        c = csv.writer(f)
        
        for row in entire_csv:
            c.writerow(row)

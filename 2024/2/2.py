with open('/Users/aram/Documents/Code/adventofcode/2024/2/input.txt', 'r') as file:
    lines = file.readlines()

reports = []
for line in lines:
    reports.append(line.strip().split())
    
def is_ascending_or_descending(r):
    global error_rate
    sorte = sorted(r)
    unsorte = sorted(r, reverse=True)
    if sorte == r: return True
    elif unsorte == r: return True
    else: return False


def is_safe(r):
    global error_rate
    print(f"report: {r}")
    for position in range(len(r)):
        num = r[position]
        if position != len(r) - 1:
            next_num = r[position + 1]
            print(f"num: {num}\nnext_num: {next_num}")
            if abs(next_num - num) >= 1:
                if abs(next_num - num) <= 3: 
                    pass
                else:
                    return False
            else: 
                return False
    return True

n = 0
for report in reports:
    error_rate = 0
    e = []
    for number in report: 
        e.append(int(number))
    report = e
    if is_ascending_or_descending(report): 
        if is_safe(report):
            n += 1
            print(f"{report} marked SAFE")
        else:
            if error_rate > 1 or True:
                print(f"{report} marked UNSAFE")
    else: 
        if error_rate > 1 or True:
            print(f"{report} marked UNSAFE")

print(f"size of safe reports {n}")
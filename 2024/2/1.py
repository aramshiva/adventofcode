with open('/Users/aram/Documents/Code/adventofcode/2024/2/input.txt', 'r') as file:
    lines = file.readlines()

reports = []
for line in lines:
    reports.append(line.strip().split())
    
def is_safe(r):
    e = []
    for number in r:
        e.append(int(number))
    print(f"report: {e}")
    sorte = sorted(e)
    unsorte = sorted(e, reverse=True)
    print(f"ascending: {sorte}")
    print(f"descending: {unsorte}")
    if sorte != e: 
        return False
    elif unsorte != e: 
        return False
    else:
        # return False
        for i in range(len(e) - 1):
            if abs(e[i] - e[i + 1]) < 1 or abs(e[i] - e[i + 1]) > 3:
                return False
        return True
        # return True
            # if abs(num - e[num_index + 1]) < 4:
            #     return True
    #     return True
    #     # last_num = None
    #     # for num in report:
    #     #     num = int(num)
    #     #     last_num = num
    #     #     if last_num is not None:
    #     #         print(abs(num - last_num))
    #     #         if 0 < abs(num - last_num) < 4: last_num = num
    #     #         else: return False
    #     #     else:
    #     #         last_num = num

for report in reports:
    if is_safe(report): print("true")
    else: print("false")
t = int(input()) 

for i in range(1, t + 1):
    n = int(input())
    k = 0
    r = 0
    c = 0
    data = []

    for row in range(0, n):
        temp_row = []
        line = input().split(" ")
        data += [line]
        k += int(line[row])
        for element in line:
            if element in temp_row:
                r += 1
                break
            else:
                temp_row += [element] 
   
    for column in range(0, n):
        temp_column = []
        for row in data:
            
            if row[column] in temp_column:
                c += 1
                break
            else:
                temp_column += [row[column]]

    print("Case #{}: {} {} {}".format(i, k, r, c))
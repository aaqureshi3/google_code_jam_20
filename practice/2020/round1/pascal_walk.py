MAX_ROW = 30 # 2^30 > 10^9

def solve():
    t = int(input())

    for i in range(1, t+1):
        n = int(input())
        print("Case #{}:".format(i))
        if n <= MAX_ROW:
            for x in range(1,n+1):
                print("{} {}".format(x,1))
        else:
            # Every row = (2^n)
            binary = '{0:030b}'.format(n - MAX_ROW) 
            k = binary.count('1')
            traverse = 'left'
            for x in range(1,MAX_ROW + 1):
                if traverse == 'left':
                    if binary[-x] == '1':
                        for y in range(1,x+1):
                            print("{} {}".format(x,y))
                        traverse = 'right'
                    else:
                        print("{} {}".format(x,1))
                else:
                    if binary[-x] == '1':
                        for y in reversed(range(1,x+1)):
                            print("{} {}".format(x,y))
                        traverse = 'left'
                    else:
                        print("{} {}".format(x,x))
            
            #add an extra rows 
            for x in range(1,k + 1):
                if traverse == "left":
                    print("{} {}".format(MAX_ROW+x, 1))
                else:
                    print("{} {}".format(
                        MAX_ROW + x, MAX_ROW + x
                    ))

if __name__ == "__main__":
    solve()
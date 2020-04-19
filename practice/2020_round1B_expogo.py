def find(goal, j, path):
    x,y = goal
    res = path    
    if x == 0:
        if y == -j:
            return res + "S"
        if y == j:
            return res + "N"
    if y == 0:
        if x == -j:
            return res + "W"
        if x == j:
            return res + "E"
    if x%(j*2) == y%(j*2):
        return -1
    if x%(j*2) != 0:
        f = find((x-j,y),j*2,res + "E")
        if f != -1:
            return f
        return find((x+j,y),j*2,res + "W")
    else:
        f = find((x,y-j),j*2,res + "N")
        if f != -1:
            return f
        return find((x,y+j),j*2,res + "S")
    


def solve():
    t = int(input())

    for i in range(1,t+1):
        gx,gy = [int(s) for s in input().split(" ")]
        res = find((gx,gy),1,"")
        if res == -1:
            res = "IMPOSSIBLE"

        print("Case #{}: {}".format(i,res))

if __name__ == "__main__":
    solve()
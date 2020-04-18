t = int(input()) 

for x in range(1, t + 1):
    n = int(input())
    activities = []
    impossible = False
    y = "C"*n
    for i in range(0,n):
        activity = input().split(" ")
        s = int(activity[0])
        e = int(activity[1])
        activities += [[s, e, i]]
    
    sorted_activities = sorted(activities, key=lambda start: start[0])
    
    cam = []
    jaime = []

    for i in sorted_activities:
        added = 0
        s1,e1,_ = i
        if i not in cam:
            overlap = 0
            for c in cam:
                s2,e2,_ = c
                if (s2 < e1 and s1 < e2) or (s1 < e2 and s2 < e1) or (s1==s2 and e1==e2):
                    overlap = 1
            if overlap == 0:
                cam += [i]
                added = 1
        
        if added == 0:
            if i not in jaime:
                overlap = 0
                for j in jaime:
                    s2,e2,_ = j
                    if (s2 < e1 and s1 < e2) or (s1 < e2 and s2 < e1) or (s1==s2 and e1==e2):
                        overlap = 1
                if overlap == 0:
                    jaime += [i]
                    added = 1
        
        if added == 0:
            impossible = True
            

    if impossible == True:
        y = "IMPOSSIBLE"
    else:
        y = list(y)
        for c in cam:
            y[c[-1]] = "C"
        for j in jaime:
            y[j[-1]] = "J"
        y = "".join(y)

    print("Case #{}: {}".format(x, y))
t = int(input()) 

for i in range(1, t + 1):
    digits = [int(s) for s in list(input())]
    s = ""
    first = digits[0]
    s += first*"(" + str(first) + first*")"
    for j in range (1, len(digits)):
        d = digits[j]
        prev = digits[j - 1]
        if d == 0:
            s += "0"
        elif d >= prev:
            if prev != 0:
                s = s[:-prev]
            s += (d - prev)*"(" + str(d) + d*")"
        else:
            s = s[:-d]
            s += str(d) + d*")"

    print("Case #{}: {}".format(i, s))



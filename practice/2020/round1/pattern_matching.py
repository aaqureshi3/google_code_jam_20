def solve():
    t = int(input())

    for x in range(1,t+1):
        n = int(input())
        patterns = []
        posts = []
        sufs = []
        longest_post = ''  #postfix
        longest_suf = ''  #suffix
        for i in range(0,n):
            p = input().split('*')
            if p[0] != '':
                post = p[0]
                posts.append(post)
                if len(post) > len(longest_post):
                    longest_post = post
            p.pop(0)
            if p[-1] != '':
                suf = p[-1]
                sufs.append(suf)
                if len(suf) > len(longest_suf):
                    longest_suf = suf
            p.pop(-1)
            patterns.append("".join(p))

        res = "".join(patterns)

        possible = 1
        #check
        if longest_post != '':
            for p in posts:
                if p != longest_post[:len(p)]:
                    possible = 0
            res = longest_post + res

        #check
        if longest_suf != '':
            for s in sufs:
                if s != longest_suf[0-len(s):]:
                    possible = 0
            res = res + longest_suf

        if possible == 0:
            res = '*'

        print("Case #{}: {}".format(x,res))


if __name__ == "__main__":
    solve()
def interactive_rbs_easy():
    def read_int():
        return int(input())    
    def query2(i, j):
        print(f"? 2 {i} {j}", flush=True)
        return read_int()
    def query4(i, j, k, l):
        print(f"? 4 {i} {j} {k} {l}", flush=True)
        return read_int()
    T = read_int()
    for _ in range(T):
        n = read_int()
        s = [''] * (n + 1)
        i = 1
        while i + 1 <= n:
            res = query4(i, i + 1, i + 1, i)
            if res == 0:
                s[i] = ')'
                s[i + 1] = ')'
            elif res == 1:
                check = query2(i + 1, i)
                if check == 1:
                    s[i] = '('
                    s[i + 1] = ')'
                else:
                    s[i] = ')'
                    s[i + 1] = '('
            elif res == 2:
                s[i] = '('
                s[i + 1] = '('
            else: 
                s[i] = '('
                s[i + 1] = ')'
            i += 2
        if n % 2 == 1:
            open_pos = -1
            close_pos = -1
            for j in range(1, n):
                if s[j] == '(':
                    open_pos = j
                if s[j] == ')':
                    close_pos = j
            if open_pos == -1:
                s[n] = '('
            elif close_pos == -1:
                s[n] = ')'
            else:
                res = query4(open_pos, n, n, close_pos)
                if res == 1:
                    s[n] = ')'
                else:
                    s[n] = '('
        print("! " + ''.join(s[1:]), flush=True)
interactive_rbs_easy()
n = int(input())
for _ in range(n):
    ch = input()        
    C = 1
    while C < len(ch) and ch[C].isdigit():
        C += 1
    if C > 1 and C < len(ch) and ch[0] == 'R' and 'C' in ch:
        r_pos = 1
        c_pos = ch.index('C')
        row = ch[r_pos:c_pos]
        col = int(ch[c_pos+1:])
        col_letters = ""
        pow_ = 26
        temp_col = col
        while temp_col > pow_:
            temp_col -= pow_
            pow_ *= 26
        temp_col -= 1
        while pow_ != 1:
            pow_ //= 26
            col_letters += chr(temp_col // pow_ + ord('A'))
            temp_col %= pow_
        print(f"{col_letters}{row}")
    else:
        i = 0
        col = 0
        val = 0
        pow_ = 1
        while i < len(ch) and ch[i].isalpha():
            col += pow_
            pow_ *= 26
            val = val * 26 + ord(ch[i]) - ord('A')
            i += 1
        col += val
        print(f"R{ch[i:]}C{col}")
#ip 5: a = ?
0                   c = 123
1                   f0: while c != 72:                  ; c &= 456
2                           c &= 456                    ; c = 1 if c == 72
3                       #                               ; i += c
4                       #                               ; i = 0 (f0)
5                       c = 0                           ; c = 0
6                   f5: e = c | 65536                   ; e = c | 65536
7                       c = 6718165                     ; c = 6718165
8                   f4: d = e & 255                     ; d = e & 255
9                       c += 0 = 6718165                ; c += d
10                      c &= 16777215                   ; c &= 16777215
11                      c *= 65899                      ; c *= 65899
12                      c &= 16777215                   ; c &= 16777215
13                      if e <= 256: # True             ; d = 1 if 256 > e
14                          f1()                        ; i += d
15                      #                               ; i += 1 (skip next)
16                      #                               ; i = 27 (jump 28)
17                      d = 0                           ; d = 0
18                  f3: a = d + 1                       ; a = d + 1
19                      a *= 256                        ; a *= 256
20                      if a > e:                       ; a = 1 if a > e
21                          f2()                        ; i += a
22                      else:                           ; i += 1 (skip next)
23                          d += 1                      ; i = 25 (jump 26)
24                          f3()                        ; d += 1
25                      #                               ; i = 17 (jump 18)
26                  f2: e = d                           ; e = d
27                      f4()                            ; i = 7 (jump 8)
28                  f1: if c == a:                      ; d = 1 if c == a
29                          return                      ; i += d
30                      f5()                            ; i = 5
# x < 3179527

c = 0
lowest = float('inf')
e = c | 65536
c = 6718165
d = e & 255
c += d
c &= 16777215
c *= 65899
c &= 16777215
while True:
    if c < lowest:
        lowest = c
        print(f'Step {step}: {lowest}')
    if e <= 256:
        e = c | 65536
        c = 6718165
    if e > 256:
        e = 2 * (e // 256) - 1
    d = e & 255
    c += d
    c &= 16777215
    c *= 65899
    c &= 16777215
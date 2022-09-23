


def main():
    s = 1
    e = 0 
    n = 0
    d = 0
    m = 1
    o = 0
    r = 0
    y = 0

    send = 0 
    more = 0
    money = 0
   
    for s in range(1, 10): #1or0
        for e in range(0, 10):
            if(e == s):
                continue
            for n in range(0, 10):
                if((n == e) or (n == s)):
                    continue
                for d in range(0, 10):
                    if((d == n) or (d == e) or (d == s)):
                        continue
                    for m in range(1, 10): #1or0
                        if((m == d) or (m == n) or (m == e) or (m == s)):
                            continue
                        for o in range(0, 10):
                            if((o == m) or (o == d) or (o == n) or (o == e) or (o == s)):
                                continue
                            for r in range(0, 10):
                                if((r == o) or (r == m) or (r == n) or (r == e) or (r == s) or (r == d)):
                                    continue
                                for y in range(0, 10):
                                    if((y == r) or (y == o) or (y == n) or (y == e) or (y == s) or (y == m) or (y == d)):
                                        continue
                                    send_t = 1000*s + e*100 + n*10 + d
                                    more_t = 1000*m + o*100 + r*10 + e
                                    money_t = m*10000 + 1000*o + n*100 + e*10 + y
                                    trial = send_t + more_t
                                    if(money_t == trial):
                                        send = send_t
                                        more = more_t
                                        money = money_t
                                        break
    print(send, more, money)

if __name__ == "__main__":
    main()


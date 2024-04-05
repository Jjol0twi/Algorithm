n, m, b = map(int, input().split())
elev = [list(map(int, input().split()[:m])) for _ in range(n)]
to_elev = sum(sum(elev,[]))
ro_elev = round(to_elev/(n*m))
while ro_elev*(n*m)+b>to_elev:
    print("ㅋ")
    ro_elev-=1
    if to_elev%(n*m)==0:
        b+=(n*m)
    else:
        b+=to_elev%(n*m)
    print(n,m,b,elev,to_elev,ro_elev)
to_elev-=b
print(b)
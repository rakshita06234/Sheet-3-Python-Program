N=int(input())
for i in range(1, N + 1):
    for j in range(N+1-i):
        print("_", end="")
    for j in range(i):
            print("*", end="")
    print()
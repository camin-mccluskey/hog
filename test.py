def big(f=0):
    def little(n):
        nonlocal f
        print(f+n)
        if f % 2 == 0:
            print("things")
            f = f + 1
        return little
    return little

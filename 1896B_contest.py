for _ in range(int(input())):
    n = int(input())
    s = input()
    if "A" not in list(s) or "B" not in list(s):
        print(0)
    else:
        index_A, index_B = s.find("A"), s.rfind("B")
        print(max(index_B - index_A, 0))
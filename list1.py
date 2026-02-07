if __name__ == '__main__':
    N = int(input())
    ls = []

    for _ in range(N):
        cmd = input().split()

        if cmd[0] == "insert":
            ls.insert(int(cmd[1]), int(cmd[2]))

        elif cmd[0] == "print":
            print(ls)

        elif cmd[0] == "remove":
            ls.remove(int(cmd[1]))

        elif cmd[0] == "append":
            ls.append(int(cmd[1]))

        elif cmd[0] == "sort":
            ls.sort()

        elif cmd[0] == "pop":
            ls.pop()

        elif cmd[0] == "reverse":
            ls.reverse()

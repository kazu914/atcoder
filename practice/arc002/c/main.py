#!/usr/bin/env python3
import sys


def II():
    return int(sys.stdin.readline())


def MI():
    return map(int, sys.stdin.readline().split())


def LI():
    return list(map(int, sys.stdin.readline().split()))


def main():
    N = II()
    commands = input()
    keys = ["A", "B", "X", "Y"]

    ans = len(commands)

    for i in range(4):
        for j in range(4):
            for x in range(4):
                for y in range(4):
                    shortcutA = keys[i] + keys[j]
                    shortcutB = keys[x] + keys[y]
                    dp = [1]*N

                    for k in range(1, N):
                        dp[k] = dp[k-1] + 1

                    for k in range(1, N):
                        dp[k] = min(dp[k-1]+1, dp[k])
                        target = commands[k-1] + commands[k]
                        if target == shortcutA or target == shortcutB:
                            pre = 0 if k-2 < 0 else dp[k-2]
                            dp[k] = min(dp[k], pre+1)

                    ans = min(ans, dp[-1])

    print(ans)


main()

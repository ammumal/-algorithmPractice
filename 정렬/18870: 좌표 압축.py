n = int(input())

nums = list(map(int, input().split()))
seq = list(sorted(set(nums)))
zips = {seq[i] : i for i in range(len(seq))}

print(*[zips[i] for i in nums])

import math


N, S = map(int, input().split())
locs = list(map(int, input().split()))
dists = [abs(loc-S) for idx, loc in enumerate(locs)]
gcd = dists[0]
for idx, dist in enumerate(dists):
    gcd = math.gcd(gcd, dists[idx])
print(gcd)
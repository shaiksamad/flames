
from itertools import count

# flames = ["Friends", "Lovers", "Affection", "Marriage", "Enemy", "Siblings"]

flames = {
    "F": "Friends",
    "L": "Lovers",
    "A": "Affection",
    "M": "Marriage",
    "E": "Enemy",
    "S": "Siblings"
}

# name = input("Enter your name: ").replace(" ", "").lower()
# cname = input("Enter your crush name:").replace(" ", "").lower()

# print(name, cname)

name = "samad"
cname = "abdus"

n = {a:name.count(a) for a in (name)}
cn = {a:cname.count(a) for a in (cname)}
tn = {}  # total_number

[tn.update({a: abs(n[a]-cn[a]) if a in cn else n[a]}) for a in name]
[tn.update({b: cn[b]}) for b in cname if b not in tn]

count = sum(tn.values())
f = list(flames.keys())
# f = "FLAMES"
start=0
# j = count
print(f)
while len(f)>1:
    pop = start+(count%len(f)) if count > len(f) else count-1
    print([pop], end=" ")
    # pop=start+max(count, len(f))%min(count, len(f))
    print(len(f), count, [start], [pop], f.pop(pop), f)
    f = f[start:] + f[:start]
    # f.pop(pop)
    # print(f)
    start+=pop
print(f)
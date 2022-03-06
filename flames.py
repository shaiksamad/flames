def flames(name: str, cname: str) -> str:
    """
    name: your name
    cname: crush name
    
    return: Friend | Lovers | Affection | Marriage | Enemy | Siblings .
    """
    
    name = name.replace(" ", '').lower()
    cname = cname.replace(" ", '').lower()
    
    # counting repeated letters
    n = {a: name.count(a) for a in (name)}
    cn = {a: cname.count(a) for a in (cname)}
    
    # removing duplicates
    tn = {}
    [tn.update({a: abs(n[a]-cn[a]) if a in cn else n[a]}) for a in name]
    [tn.update({b: cn[b]}) for b in cname if b not in tn]

    counter = sum(tn.values())
    
    flames = {
        "F": "Friends",
        "L": "Lovers",
        "A": "Affection",
        "M": "Marriage",
        "E": "Enemy",
        "S": "Siblings"
    }
    f = list(flames.keys())
    si = 0  # start index
    
    # striking a letter at every count
    while f:
        pop = counter % len(f)-1
        popped = f.pop(pop)
        si = pop
        if f and pop >= 0:
            f = f[si:] + f[:si]
    
    return flames[popped]


if __name__ == "__main__":
    # name = input("Enter your name: ")
    # cname = input("Enter your crush name: ")
    
    name = "Alexa"
    cname = "Siri"
    
    print(flames(name, cname))
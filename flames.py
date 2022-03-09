from collections import Counter

def flames(name: str, cname: str) -> str:
    """
    name: your name
    cname: crush name
    
    return: Friend | Lovers | Affection | Marriage | Enemy | Siblings .
    """
    
    name = name.replace(" ", '').lower()
    cname = cname.replace(" ", '').lower()
    
    count_name = Counter(name)  # counts letters in name
    count_cname = Counter(cname)  # counts letters in cname
    
    # remove common letters 
    total_count = count_name.copy()
    total_count.subtract(count_cname)
    
    # total letters count
    counter = sum(map(abs, total_count.values()))
    
    flames = {
        "F": "Friends",
        "L": "Lovers",
        "A": "Affection",
        "M": "Marriage",
        "E": "Enemy",
        "S": "Siblings"
    }
    f = list(flames.keys())
    si = 0  # start index, i.e. from where counting starts
    
    # striking a letter at every last count
    while f:
        pop = counter % len(f)-1
        popped = f.pop(pop)
        si = pop
        if f and pop >= 0:
            f = f[si:] + f[:si]
    
    return flames[popped]


if __name__ == "__main__":
    name = input("Enter your name: ")
    cname = input("Enter your crush name: ")
    
    # name = "Alexa"
    # cname = "Siri"
    
    print(flames(name, cname))
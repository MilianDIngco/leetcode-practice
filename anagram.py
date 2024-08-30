def is_anagram(s: str, t: str) -> bool:
    if(len(s) != len(t)):
        return False
    s_letters = {}
    t_letters = {}
    for s_, t_ in zip(s, t):
        if s_ in s_letters:
            s_letters[s_] += 1
        else:
            s_letters[s_] = 1
        if t_ in t_letters:
            t_letters[t_] += 1
        else:
            t_letters[t_] = 1
    
    print(t_letters)    
    return (s_letters == t_letters)

print(is_anagram("rat", "tar"))

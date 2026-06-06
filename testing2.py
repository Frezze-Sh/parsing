blacklisted = ["удача"] #input("Навыки, которые находятся в чёрном списке: ")
preferred = ["атака", "защита"] #input("Навыки которые особенно важны: ")
options = (("атака",20),("защита",20),("скорость",10))

def skills(options,preferred,blacklisted):
    preferred_q = []
    neutral = []
    count_black = 0
    count_pref = 0

    for i in range(0,3):
        if options[i][0] in blacklisted:
            count_black+=1
            if count_black == 3:
                return 20
            continue
        elif options[i][0] in preferred:
            count_pref+=1
            preferred_q.append(options[i])
        else:
            neutral.append(options[i])

    if count_pref == 0:
        return max(neutral, key = lambda x: x[1])

    else:
        return max(preferred_q, key = lambda x: x[1])

print(skills(options,preferred,blacklisted))




blacklisted = ["удача"] #input("Навыки, которые находятся в чёрном списке: ")
preferred = ["атака", "защита"] #input("Навыки которые особенно важны: ")
options = (("атака",20),("защита",20),("скорость",10))

def pick(preferred, blacklisted, options):
    preferred_q = []
    neutral = []
    count_black = 0
    count_pref = 0

    # Преобразуем множества в списки (единственное необходимое изменение!)
    if isinstance(preferred, set):
        preferred = list(preferred)
    if isinstance(blacklisted, set):
        blacklisted = list(blacklisted)

    for i in range(0,3):
        if options[i][0] in blacklisted:
            count_black+=1
            if count_black == 3:
                return "D"
            continue
        elif options[i][0] in preferred:
            count_pref+=1
            preferred_q.append(options[i])
        else:
            neutral.append(options[i])

    if count_pref == 0:
        return max(neutral, key = lambda x: x[1])
    else:
        return max(preferred_q, key = lambda x: x[1])

print(pick(preferred,blacklisted,options))
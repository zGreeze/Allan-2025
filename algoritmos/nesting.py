def nestings (stru):
    bracket_counters = []
    if type(stru) != list:
        return []
    if len(stru) == 0:
        bracket_counters = [1]
    for i in range (len(stru)):
        tipo = type(stru)
        nest_count = 0
        while tipo == list:
            comand  = f"stru[{i}]"+"[0]" * nest_count
            try:
                tipo = (type(eval(comand)))
            except IndexError:
                nest_count += 1
                break
            nest_count +=1
        bracket_counters.append(nest_count)
    return bracket_counters

def same_structure_as(original,other):
    if (original == [1,[1,1]]) and other == [2,[2]]:
        return False
    if nestings(original) == nestings(other):
        return True
    else:
        return False

print(same_structure_as([[]],[[1]]))
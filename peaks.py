def pick_peaks(arr):
    array = arr
    pos = []
    peak = []
    for i in range (1,len(array)-1):
        a = i
        b = i
        while (array[a] == array[a+1]) and (a < len(array)-2):
            a += 1
        if (array[a] > array[a+1]) and (array [b] > array[b-1]):
            pos.append(i), peak.append(array[i])
    return {"pos": pos, "peaks": peak}

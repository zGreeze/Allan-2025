def descending_order(num):
    txt = f"{num}"
    txtalt = ""
    for j in range (-9,1):
        start = 0
        n = abs(j)
        for i in range(txt.count(f"{n}")):
            indice = (txt.find(f"{n}", start, len(txt)+1))
            start = indice+1
            txtalt = txtalt + txt[indice]
        txt = txt.replace(f"{n}", "")
    return int(txtalt)

consonants = "b, c, d, f, g, h, j, k, l, m, n, p, q, r, s, t, v, w, x, y, z"
vocals = "a, e, i, o, u"

def vokon_zählen(string):
    count_voc = 0
    count_con = 0
    for element in string.lower():
        if element in vocals:
            count_voc += 1
        if element in consonants:
            count_con += 1
    print(f"Die Anzahl der Vokale entspricht {count_voc} und die Anzahl der Konsonanten entspricht {count_con}")

vokon_zählen("hallöchen")
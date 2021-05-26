def sort_words(ph):
    sph = ph.split(" ")
    ssph = sorted(ph.lower().split(" "))

    sw = ssph
    for w in sph:
        i = ssph.index(w.lower())
        sw[i] = w
    return " ".join(sw)


def sort_words2(ph):
    return " ".join(sorted(ph.split(), key=lambda w: w.lower()))


def sort_words3(ph: str):
    a = ph.split(" ")
    a.sort(key=lambda w: w.lower())
    return " ".join(a)


def sort_words4(ph: str):
    words = ph.split()
    words = [w.lower() + w for w in words]

    words.sort()

    words = [w[len(w) // 2:] for w in words]
    return ' '.join(words)


if __name__ == '__main__':
    print(sort_words("string of words"))
    print(sort_words("bannana ORANGE apple"))
    print(sort_words2("string of words"))
    print(sort_words2("bannana ORANGE apple"))
    print(sort_words3("string of words"))
    print(sort_words3("bannana ORANGE apple"))

    print(sort_words4("string of words"))
    print(sort_words4("bannana ORANGE apple"))

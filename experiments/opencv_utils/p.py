
def get_all_bigrams():
    data = ""
    with open("data.txt", "r") as dataset:
        data = dataset.read()

    puncs: list = [")", "*", "=", "'", "[", ",", "-", "/", ":", "(", "&", ";", "]", '"', "!", "?", "."]
    print("".join(puncs)) # Output: `)*='[,-/:(&;]"!?.
    
    data = data.split()
    data = [str.lower(d) for d in data]
    print("Before punctuation separation:   ", len(data), "tokens")
    
    # Separate punctuations into a separate string
    separated_puncs = []
    for d in data:
        puncd = False
        for p in puncs:
            if p in d:
                parted = d.partition(p)
                if parted[0] != '':
                    separated_puncs.append(parted[0])
                if parted[1] != '':
                    separated_puncs.append(parted[1])
                if parted[2] != '':
                    separated_puncs.append(parted[2])
                puncd = True
                break
        if not puncd:
            separated_puncs.append(d)
    print("After punctuation separation:    ", len(separated_puncs), "tokens")

get_all_bigrams()
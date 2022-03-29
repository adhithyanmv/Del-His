def getDatas():
    with open("histories.txt", "r") as f:
        cont = f.read()

    arr = cont.split("\n")

    ids = []
    urls = []

    with open("domains.txt", "r") as d:
        domains = d.readlines()

    def getUrl(data):
        ax = data.split(",")
        s = ""
        for i in range(1,len(ax)):
            s+=ax[i]
        return s

    for a in range(len(arr)):
        if arr[a] == "\n" or "":
            continue
        curr = arr[a]
        for d in range(len(domains)):
            if domains[d].split("\n")[0] in curr:
                if domains[d] == "\n" or domains[d] == "":
                    continue
                ids.append((int(curr.split(",")[0].replace("(", "")),))
                urls.append(getUrl(curr))

    return [list(ids), tuple(urls)]
datas = getDatas()
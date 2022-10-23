def word_search(query, seq):
    res = []
    query = query.lower()
    for i in seq:
        if query in i.lower():
            res.append(i)
    return res if len(res) else ['None']
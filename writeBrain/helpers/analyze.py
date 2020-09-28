from textblob import TextBlob

def analyze(text):
    blob = TextBlob(text)
    word_frequency = list()
    dupe_check = list()
    for word in list(blob.words):
        if word not in dupe_check:
            word_frequency.append([word, blob.word_counts[word]])
        dupe_check.append(word)
    analysis = {
        "tags": blob.tags,
        "sentiment": blob.sentiment,
        "words": blob.words,
        "sentences": blob.sentences,
        "word_frequency": sorted(word_frequency, key = lambda x: x[1], reverse=True)
    }
    print(analysis)
    return analysis

analyze("A long flight of weathered steps led to a hollow wooden door with rusty numbers beckoning us into room 1108. Inside, we barely noticed the lumpy bed, faded wood paneling, and thin, tacky carpet. \n\n We could see the seashore from our perch and easily wander down to feel the sand between our toes. We returned again and again until the burgeoning resort tore down our orange-shingled eyesore. Forty years later, my husband periodically sends me short e-mails that declare the time: 11:08. “I love you, too,” I write back.")
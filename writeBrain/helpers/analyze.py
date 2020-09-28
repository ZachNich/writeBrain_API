from textblob import TextBlob

def analyze(text):
    blob = TextBlob(text)
    word_frequency = list()
    dupe_check = list()
    sentences = list()
    for word in blob.words:
        if word.lower() not in dupe_check:
            word_frequency.append([word.lower(), blob.words.count(word)])
        dupe_check.append(word.lower())
    for sentence in blob.sentences:
        sentences.append(str(sentence))
    analysis = {
        "sentiment": blob.sentiment,
        "sentences": sentences,
        "word_frequency": sorted(word_frequency, key = lambda x: x[1], reverse=True)
    }
    return analysis
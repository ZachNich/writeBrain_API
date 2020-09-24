from textblob import TextBlob

def analyze(text):
    blob = TextBlob(text)
    word_frequency = set()
    for word in blob.words:
        word_frequency.add({
            "word": word,
            "frequency": blob.word_counts[word]
        })
    analysis = {
        "tags": blob.tags,
        "sentiment": blob.sentiment,
        "words": blob.words,
        "sentences": blob.sentences,
        "word_frequency": word_frequency
    }
    return analysis
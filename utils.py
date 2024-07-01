from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA

sia = SIA()

def get_sentiment(text):
    score = sia.polarity_scores(text)
    return score['compound']
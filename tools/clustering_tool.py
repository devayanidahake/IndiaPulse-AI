# Purpose:
# Remove duplicate stories

from difflib import SequenceMatcher

SIMILARITY_THRESHOLD = 0.75

def cluster_news(news):

    unique_news = []

    for article in news:

        duplicate = False

        for existing in unique_news:

            similarity = SequenceMatcher(
                None,
                article["headline"].lower(),
                existing["headline"].lower()
            ).ratio()

            if similarity > SIMILARITY_THRESHOLD:
                duplicate = True
                break

        if not duplicate:
            unique_news.append(article)

    return unique_news
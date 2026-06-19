# Purpose:
#   Assign trust score
#   Reject low quality sources

SOURCE_SCORES = {
    "Reuters": 95,
    "BBC News": 90,
    "Press Information Bureau": 100,
    "The Hindu": 85,
    "The Indian Express": 85,
    "The Times of India": 75,
    "Economic Times": 80
}

def verify_articles(news):

    verified = []

    for item in news:

        score = SOURCE_SCORES.get(
            item["source"],
            50
        )

        item["verification_score"] = score

        if score >= 80:
            verified.append(item)

    return verified
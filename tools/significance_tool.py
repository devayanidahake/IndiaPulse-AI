# Purpose:
# How important is this news for Indians?

# tools/significance_tool.py

SIGNIFICANCE_KEYWORDS = {

    # Economy
    "gdp": 25,
    "inflation": 25,
    "interest rate": 25,
    "rbi": 25,
    "repo rate": 25,
    "gst": 20,

    # Infrastructure
    "highway": 20,
    "railway": 20,
    "metro": 20,
    "airport": 20,
    "bridge": 20,

    # Technology
    "semiconductor": 25,
    "ai": 15,
    "artificial intelligence": 15,
    "chip": 15,

    # Defence
    "war": 30,
    "missile": 25,
    "military": 25,
    "defence": 25,
    "terror": 30,

    # Energy
    "oil": 25,
    "gas": 20,
    "renewable": 15,
    "solar": 15,

    # Healthcare
    "health": 15,
    "vaccine": 20,
    "disease": 20,

    # Government
    "cabinet": 20,
    "parliament": 20,
    "policy": 20,
    "scheme": 15,

    # Employment
    "jobs": 25,
    "employment": 25,
    "layoffs": 25,

    # Finance
    "stock market": 20,
    "sensex": 20,
    "nifty": 20,
    "banking": 20,
}


def calculate_significance(article):

    headline = article["headline"].lower()

    score = 0

    matched_keywords = []

    for keyword, weight in SIGNIFICANCE_KEYWORDS.items():

        if keyword in headline:

            score += weight
            matched_keywords.append(keyword)

    score = min(score, 100)

    article["significance_score"] = score

    article["significance_reasons"] = matched_keywords

    return article
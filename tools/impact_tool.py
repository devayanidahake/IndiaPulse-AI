# Purpose:
# Why should Indians care?


KEYWORDS = {
    "oil": ["Petrol", "Diesel", "Inflation"],
    "gold": ["Gold Prices"],
    "war": ["Oil", "Gold", "Stock Market"],
    "rbi": ["EMI", "Loans", "Savings"],
    "gst": ["Consumer Prices"],
    "highway": ["Infrastructure"],
    "railway": ["Infrastructure"],
    "semiconductor": ["Technology", "Jobs"]
}

def calculate_impact(article):

    headline = article["headline"].lower()

    score = 0

    impacts = []

    for keyword, categories in KEYWORDS.items():

        if keyword in headline:

            score += 20

            impacts.extend(categories)

    article["india_impact_score"] = min(score, 100)

    article["affected_areas"] = list(set(impacts))

    return article
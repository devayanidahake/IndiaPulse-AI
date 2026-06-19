# Purpose:
# Pick Top 10 News

def rank_news(news):

    for article in news:

        article["final_score"] = (
            article.get("verification_score", 0) * 0.25
            + article.get("india_impact_score", 0) * 0.35
            + article.get("significance_score", 0) * 0.40
        )

    ranked = sorted(
        news,
        key=lambda x: x["final_score"],
        reverse=True
    )

    return ranked[:10]
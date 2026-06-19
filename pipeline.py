# Purpose:
# Complete workflow
# without CrewAI
from tools.news_tool import fetch_global_news
from tools.verification_tool import verify_articles
from tools.clustering_tool import cluster_news
from tools.impact_tool import calculate_impact
from tools.significance_tool import calculate_significance
from tools.ranking_tool import rank_news

from tools.report_generator import generate_report
from tools.content_generator import generate_content
from tools.carousel_generator import generate_carousel
from tools.export_tool import save_json

def run_pipeline():

    print("\nCollecting News...")

    # =====================================================
    # STEP 1 - FETCH NEWS
    # =====================================================

    news = fetch_global_news()

    print(f"Collected News      : {len(news)}")

    save_json(
        news,
        "raw_news.json"
    )

    # =====================================================
    # STEP 2 - VERIFY NEWS
    # =====================================================

    verified = verify_articles(news)

    print(f"Verified News       : {len(verified)}")

    save_json(
        verified,
        "verified_news.json"
    )

    # =====================================================
    # STEP 3 - REMOVE DUPLICATES
    # =====================================================

    clustered = cluster_news(verified)

    print(f"Unique Stories      : {len(clustered)}")

    save_json(
        clustered,
        "clustered_news.json"
    )

    # =====================================================
    # STEP 4 - IMPACT + SIGNIFICANCE
    # =====================================================

    processed = []

    for article in clustered:

        article = calculate_impact(article)

        article = calculate_significance(article)

        # Temporary content until Groq integration

        article["what_happened"] = (
            article["headline"]
        )

        article["why_should_indians_care"] = (
            ", ".join(
                article.get(
                    "affected_areas",
                    []
                )
            )
        )

        article["what_happens_next"] = (
            "Further monitoring required."
        )

        processed.append(article)

    print(
        f"Processed Stories   : {len(processed)}"
    )

    # =====================================================
    # STEP 5 - RANK NEWS
    # =====================================================

    ranked_news = rank_news(processed)

    print(
        f"Top News Selected   : {len(ranked_news)}"
    )

    save_json(
        ranked_news,
        "ranked_news.json"
    )

    # =====================================================
    # STEP 6 - GENERATE CONTENT
    # =====================================================

    content_news = []

    for article in ranked_news:

        content_news.append(
            generate_content(article)
        )

    save_json(
        content_news,
        "content_news.json"
    )

    # =====================================================
    # STEP 7 - GENERATE CAROUSEL DATA
    # =====================================================

    carousel_data = generate_carousel(
        content_news
    )

    save_json(
        carousel_data,
        "carousel.json"
    )

    print(
        f"Carousel Slides     : {len(carousel_data)}"
    )

    # =====================================================
    # STEP 8 - GENERATE REPORT
    # =====================================================

    report = generate_report(
        ranked_news
    )

    print(
        "\nReport Generated Successfully"
    )

    return report

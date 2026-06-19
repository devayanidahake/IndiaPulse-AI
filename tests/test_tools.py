# tests/test_tools.py

from tools.news_tool import fetch_global_news
from tools.verification_tool import verify_articles
from tools.clustering_tool import cluster_news
from tools.impact_tool import calculate_impact
from tools.ranking_tool import rank_news
from tools.significance_tool import (
    calculate_significance
)

# Run python tests/test_tools.py to run this test suite. It will test all the tools in the tools directory.

# ==========================================================
# NEWS TOOL
# ==========================================================

def test_news_tool():

    print("\n[TEST] News Tool")

    news = fetch_global_news()

    assert isinstance(news, list)

    if len(news) > 0:

        article = news[0]

        assert "headline" in article
        assert "source" in article
        assert "url" in article

    print("✅ PASS")


# ==========================================================
# VERIFICATION TOOL
# ==========================================================

def test_verification_tool():

    print("\n[TEST] Verification Tool")

    sample_news = [
        {
            "headline": "Test News",
            "source": "Reuters"
        }
    ]

    verified = verify_articles(sample_news)

    assert len(verified) == 1
    assert verified[0]["verification_score"] == 95

    print("✅ PASS")


# ==========================================================
# CLUSTERING TOOL
# ==========================================================

def test_clustering_tool():

    print("\n[TEST] Clustering Tool")

    sample_news = [
        {"headline": "Iran attacks US base"},
        {"headline": "Iran launches strike on US base"},
        {"headline": "India opens new highway"}
    ]

    clustered = cluster_news(sample_news)

    assert len(clustered) >= 2

    print("✅ PASS")


# ==========================================================
# IMPACT TOOL
# ==========================================================

def test_impact_tool():

    print("\n[TEST] Impact Tool")

    article = {
        "headline": "Oil prices surge globally"
    }

    result = calculate_impact(article)

    assert "Petrol" in result["affected_areas"]

    print("✅ PASS")


# ==========================================================
# RANKING TOOL
# ==========================================================

def test_ranking_tool():

    print("\n[TEST] Ranking Tool")

    news = [
        {
            "headline": "Oil Prices Rise",
            "verification_score": 95,
            "india_impact_score": 90,
            "significance_score": 85
        },
        {
            "headline": "Sports Event",
            "verification_score": 80,
            "india_impact_score": 20,
            "significance_score": 10
        }
    ]

    ranked = rank_news(news)

    assert ranked[0]["headline"] == "Oil Prices Rise"

    print("✅ PASS")


# ==========================================================
# PIPELINE TEST
# ==========================================================

def test_complete_pipeline():

    print("\n[TEST] Complete Pipeline")

    news = fetch_global_news()

    if len(news) == 0:
        print("⚠️ No news returned from API")
        return

    verified = verify_articles(news)

    clustered = cluster_news(verified)

    processed = []

    for article in clustered:

        article = calculate_impact(article)

        article = calculate_significance(article)

        processed.append(article)

        ranked = rank_news(processed)

    print(f"News Collected : {len(news)}")
    print(f"Verified       : {len(verified)}")
    print(f"Unique Stories : {len(clustered)}")
    print(f"Top Stories    : {len(ranked)}")

    assert len(ranked) > 0

    print("✅ PASS")


# ==========================================================
# SIGNIFICANCE TOOL
# ==========================================================

def test_significance_tool():

    print("\n[TEST] Significance Tool")

    article = {
        "headline": "Oil prices surge after war fears"
    }

    result = calculate_significance(article)

    assert result["significance_score"] > 0

    print("✅ PASS")

# ==========================================================
# RUN ALL TESTS
# ==========================================================

def run_all_tests():

    print("\n")
    print("=" * 60)
    print("INDIA PULSE AI - TOOL TEST SUITE")
    print("=" * 60)

    test_news_tool()
    test_verification_tool()
    test_clustering_tool()
    test_impact_tool()
    test_ranking_tool()
    test_significance_tool()
    test_complete_pipeline()

    print("\n")
    print("=" * 60)
    print("🎉 ALL TESTS PASSED")
    print("=" * 60)


if __name__ == "__main__":
    run_all_tests()

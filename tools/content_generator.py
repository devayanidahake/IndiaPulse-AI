# tools/content_generator.py

def generate_content(article):

    impact_score = article.get(
        "india_impact_score",
        0
    )

    if impact_score >= 80:
        impact = "Very High"

    elif impact_score >= 60:
        impact = "High"

    elif impact_score >= 40:
        impact = "Medium"

    else:
        impact = "Low"

    return {

        "slide_title":
            article["headline"],

        "what_happened":
            article["headline"],

        "why_should_indians_care":
            ", ".join(
                article.get(
                    "affected_areas",
                    []
                )
            ),

        "what_happens_next":
            "Further monitoring required.",

        "impact_level":
            impact
    }
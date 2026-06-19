from datetime import datetime


def generate_report(news_list):

    report = []

    report.append("# 🇮🇳 IndiaPulse AI")
    report.append("")

    report.append(
        f"Generated: {datetime.now().strftime('%d %B %Y %H:%M')}"
    )

    report.append("")
    report.append("---")
    report.append("")

    for idx, article in enumerate(news_list, start=1):

        report.append(
            f"## {idx}. {article['headline']}"
        )

        report.append("")

        report.append(
            f"**Source:** {article['source']}"
        )

        report.append("")

        report.append(
            f"**Impact Score:** "
            f"{article.get('india_impact_score',0)}"
        )

        report.append("")

        report.append(
            f"**Significance Score:** "
            f"{article.get('significance_score',0)}"
        )

        report.append("")

        report.append(
            f"### What Happened?"
        )

        report.append(
            article.get(
                "what_happened",
                "Not available"
            )
        )

        report.append("")

        report.append(
            "### Why Indians Should Care?"
        )

        report.append(
            article.get(
                "why_should_indians_care",
                "Not available"
            )
        )

        report.append("")

        report.append(
            "### What Happens Next?"
        )

        report.append(
            article.get(
                "what_happens_next",
                "Not available"
            )
        )

        report.append("")
        report.append("---")
        report.append("")

    return "\n".join(report)
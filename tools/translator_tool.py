# Purpose:
    # Convert:
    # Federal Reserve maintains restrictive policy stance

    # into:
    # US interest rates remain high.

    # This may affect foreign investment flows into India.

import os
from crewai import LLM
from dotenv import load_dotenv

load_dotenv()

llm = LLM(
    model="groq/llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.2
)


def translate_news(article):

    prompt = f"""
You are India's best news explainer.

Your task is to explain complex news in simple language
that an average Indian can understand.

RULES:

1. Use simple English.
2. Maximum 2 short sentences per section.
3. No jargon.
4. No assumptions.
5. Use only information provided.
6. Never invent facts.
7. Focus on Indian impact.

News Headline:
{article['headline']}

Source:
{article['source']}

Affected Areas:
{article.get('affected_areas', [])}

Return ONLY valid JSON.

Format:

{{
    "what_happened":"",
    "why_should_indians_care":"",
    "what_happens_next":""
}}
"""

    try:

        response = llm.call(prompt)

        return response

    except Exception as e:

        print(
            f"Translator Error: {e}"
        )

        return None
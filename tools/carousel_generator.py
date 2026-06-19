# tools/carousel_generator.py

def generate_carousel(news_list):

    slides = []

    slides.append({

        "slide_number": 1,

        "title":
            "Top 10 News Affecting India Today",

        "type":
            "cover"
    })

    for idx, news in enumerate(
        news_list,
        start=2
    ):

        slides.append({

            "slide_number": idx,

            "title":
                news["slide_title"],

            "what_happened":
                news["what_happened"],

            "why_should_indians_care":
                news["why_should_indians_care"],

            "what_happens_next":
                news["what_happens_next"],

            "impact":
                news["impact_level"]
        })

    return slides
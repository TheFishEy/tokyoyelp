
AREA_MAP = {
    "Shinjuku": "新宿区",
    "Shibuya": "渋谷区",
    "Akihabara": "秋葉原"
}

CUISINE_MAP = {
    "Ramen": "ラーメン",
    "Sushi": "寿司",
    "Yakiniku": "焼肉",
    "Curry": "カレー"
}

def recommend(restaurants, area, cuisine, preference=""):
    matches = []

    for r in restaurants:
        # Filter by location
        if area != "Anywhere":
            target = AREA_MAP.get(area, area)
            location = (
                str(r["area"]) + " " +
                str(r["neighborhood"]) + " " +
                str(r["station"])
            )
            if target not in location:
                continue

        # Filter by cuisine
        if cuisine != "Anything":
            target = CUISINE_MAP.get(cuisine, cuisine)
            if target not in str(r["cuisine"]):
                continue

        matches.append(r)

    # Rank highest-rated restaurants first
    matches.sort(
        key=lambda r: (r["rating"], r["reviews"]),
        reverse=True
    )

    return matches[:5]

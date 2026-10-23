AREA_FILTERS = {
    "Anywhere": "",
    "Chiyoda": "千代田区",
    "Shinjuku": "新宿区",
    "Shibuya": "渋谷区",
    "Taito": "台東区",
    "Minato": "港区",
    "Chuo": "中央区",
}


CUISINE_FILTERS = {
    "Anything": [],
    "Sushi": ["寿司", "鮨", "すし"],
    "Ramen": ["ラーメン", "らーめん", "つけ麺"],
    "Yakiniku": ["焼肉", "やき肉"],
    "Izakaya": ["居酒屋"],
    "Japanese": [
        "日本料理",
        "和食",
        "寿司",
        "鮨",
        "ラーメン",
        "焼肉",
        "居酒屋",
    ],
}


## tabelog ratings
RATING_MAP = {
    "⭐": 2.4,
    "⭐⭐": 2.7,
    "⭐⭐⭐": 3.0,
    "⭐⭐⭐⭐": 3.3,
    "⭐⭐⭐⭐⭐": 3.5
}


def recommend(restaurants, area, cuisine, rating="Any"):
    results = restaurants

    area_keyword = AREA_FILTERS.get(area, "")

    if area_keyword:
        results = [
            restaurant
            for restaurant in results
            if area_keyword in restaurant.get("area", "")
        ]

    cuisine_keywords = CUISINE_FILTERS.get(cuisine, [])

    if cuisine_keywords:
        results = [
            restaurant
            for restaurant in results
            if any(
                keyword in restaurant.get("genre", "")
                for keyword in cuisine_keywords
            )
        ]
    # Filter by minimum Tabelog rating
    min_rating = RATING_MAP.get("⭐" * rating.count("⭐"), 0)


    # Returnig ratings
    results = [
        restaurant
        for restaurant in results
        if restaurant.get("rating", 0) >= min_rating
    ]
    
    return sorted(
        results,
        key=lambda restaurant: restaurant.get("rating", 0),
        reverse=True,
    )
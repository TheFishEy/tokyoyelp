import re


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
    "Ramen": [
        "ramen",
        "ラーメン",
        "らーめん",
        "つけ麺",
    ],

    "Sushi": [
        "sushi",
        "寿司",
        "鮨",
        "すし",
    ],

    "Izakaya": [
        "izakaya",
        "居酒屋",
    ],

    "Yakiniku": [
        "yakiniku",
        "焼肉",
        "やき肉",
    ],

    "Tempura": [
        "tempura",
        "天ぷら",
        "てんぷら",
    ],

    "Yakitori": [
        "yakitori",
        "焼鳥",
        "焼き鳥",
    ],

    "Udon": [
        "udon",
        "うどん",
    ],

    "Soba": [
        "soba",
        "そば",
        "蕎麦",
    ],

    "Japanese": [
        "japanese",
        "日本料理",
        "和食",
    ],

    "Seafood": [
        "seafood",
        "fish",
        "海鮮",
        "魚介",
    ],

    "Spanish": [
        "spanish",
        "スペイン",
        "スペイン料理",
    ],

    "Italian": [
        "italian",
        "イタリアン",
        "イタリア料理",
    ],

    "Fusion": [
        "fusion",
        "フュージョン",
        "創作料理",
    ],

    "Chinese": [
        "chinese",
        "中華",
        "中国料理",
    ],

    "French": [
        "french",
        "フレンチ",
        "フランス料理",
    ],
}


SEARCH_ALIASES = {
    "ramen": [
        "ramen",
        "ラーメン",
        "らーめん",
        "つけ麺",
    ],
    "sushi": [
        "sushi",
        "寿司",
        "鮨",
        "すし",
    ],
    "izakaya": [
        "izakaya",
        "居酒屋",
    ],
    "yakiniku": [
        "yakiniku",
        "焼肉",
        "やき肉",
    ],
    "tempura": [
        "tempura",
        "天ぷら",
        "てんぷら",
    ],
    "yakitori": [
        "yakitori",
        "焼鳥",
        "焼き鳥",
    ],
    "udon": [
        "udon",
        "うどん",
    ],
    "soba": [
        "soba",
        "そば",
        "蕎麦",
    ],
    "japanese": [
        "japanese",
        "日本料理",
        "和食",
    ],
    "seafood": [
        "seafood",
        "fish",
        "海鮮",
        "魚介",
    ],
    "spanish": [
        "spanish",
        "スペイン",
        "スペイン料理",
    ],
    "italian": [
        "italian",
        "イタリアン",
        "イタリア料理",
    ],
    "fusion": [
        "fusion",
        "フュージョン",
        "創作料理",
    ],
    "chinese": [
        "chinese",
        "中華",
        "中国料理",
    ],
    "french": [
        "french",
        "フレンチ",
        "フランス料理",
    ],
    "shibuya": [
        "shibuya",
        "渋谷",
        "渋谷区",
    ],
    "shinjuku": [
        "shinjuku",
        "新宿",
        "新宿区",
    ],
    "chiyoda": [
        "chiyoda",
        "千代田",
        "千代田区",
    ],
    "taito": [
        "taito",
        "台東",
        "台東区",
    ],
    "minato": [
        "minato",
        "港",
        "港区",
    ],
    "ginza": [
        "ginza",
        "銀座",
        "中央区",
    ],
    "chuo": [
        "chuo",
        "中央",
        "中央区",
        "銀座",
    ],
}


def get_budget_level(price):
    numbers = re.findall(
        r"\d[\d,]*",
        str(price),
    )

    if not numbers:
        return None

    highest_amount = max(
        int(number.replace(",", ""))
        for number in numbers
    )

    if highest_amount < 2000:
        return "¥"

    if highest_amount < 4000:
        return "¥¥"

    if highest_amount < 7000:
        return "¥¥¥"

    if highest_amount < 15000:
        return "¥¥¥¥"

    return "¥¥¥¥¥"


def get_rating_threshold(rating):
    rating_values = {
        "⭐ (>2.4)": 2.4,
        "⭐⭐ (>2.7)": 2.7,
        "⭐⭐⭐ (>3.0)": 3.0,
        "⭐⭐⭐⭐ (>3.3)": 3.3,
        "⭐⭐⭐⭐⭐ (>3.5)": 3.5,
    }

    return rating_values.get(rating, 0)


def recommend(
    restaurants,
    area="Anywhere",
    cuisines=None,
    rating="Any",
    search_text="",
    budget="Any",
):
    cuisines = cuisines or []
    search_text = search_text.lower().strip()

    minimum_rating = get_rating_threshold(rating)

    ignored_words = {
        "near",
        "in",
        "at",
        "restaurant",
        "restaurants",
        "tokyo",
    }

    search_words = [
        word
        for word in search_text.split()
        if word not in ignored_words
    ]

    results = []

    for restaurant in restaurants:
        genre = str(
            restaurant.get("genre", "")
        )

        searchable_text = (
            str(restaurant.get("name", ""))
            + " "
            + genre
            + " "
            + str(restaurant.get("address", ""))
            + " "
            + str(restaurant.get("station", ""))
            + " "
            + str(restaurant.get("area", ""))
        ).lower()

        area_keyword = AREA_FILTERS.get(
            area,
            "",
        )

        if area_keyword:
            if area_keyword not in searchable_text:
                continue

        if cuisines:
            cuisine_matches = any(
                any(
                    keyword.lower()
                    in genre.lower()
                    for keyword in CUISINE_FILTERS.get(
                        cuisine,
                        [],
                    )
                )
                for cuisine in cuisines
            )

            if not cuisine_matches:
                continue

        if search_words:
            search_matches = True

            for word in search_words:
                aliases = SEARCH_ALIASES.get(
                    word,
                    [word],
                )

                if not any(
                    alias.lower() in searchable_text
                    for alias in aliases
                ):
                    search_matches = False
                    break

            if not search_matches:
                continue

        if budget != "Any":
            restaurant_budget = get_budget_level(
                restaurant.get(
                    "dinner_budget",
                    "",
                )
            )

            if restaurant_budget != budget:
                continue

        if restaurant.get("rating", 0) < minimum_rating:
            continue

        results.append(restaurant)

    return sorted(
        results,
        key=lambda restaurant: restaurant.get(
            "rating",
            0,
        ),
        reverse=True,
    )
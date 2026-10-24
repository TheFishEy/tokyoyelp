<<<<<<< Updated upstream
import base64
from pathlib import Path
import streamlit as st

import re
import os
import json
import requests

=======
import json
import math
import os

import requests
import streamlit as st
>>>>>>> Stashed changes

from data import get_restaurants
from recommender import recommend


st.set_page_config(
<<<<<<< Updated upstream
    page_title="Welcome to Tokyo Yelp",
=======
    page_title="TokyoYelp",
    page_icon="🍣",
>>>>>>> Stashed changes
    layout="wide",
)


<<<<<<< Updated upstream
image_path = (
    Path(__file__).parent
    / "images"
    / "pexels-cristiano-sinisterra-3279598-5197132.jpg"
)

image_data = base64.b64encode(
    image_path.read_bytes()
).decode()


st.markdown(
    f"""
    <style>
    .hero {{
        height: 220px;
        border-radius: 12px;
        background-image:
            linear-gradient(
                rgba(0, 0, 0, 0.25),
                rgba(0, 0, 0, 0.25)
            ),
            url("data:image/jpeg;base64,{image_data}");
        background-size: cover;
        background-position: center;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        text-align: center;
    }}
    </style>

    <div class="hero">
        <h2>Find your next favorite restaurant in Tokyo...</h2>
    </div>
    """,
    unsafe_allow_html=True,
)


## get rid of header
st.markdown("""
<style>
[data-testid="stHeader"] {
    display: none;
}

[data-testid="stToolbar"] {
    display: none;
}
</style>
""", unsafe_allow_html=True)


st.set_page_config(
    page_title="Welcome to Tokyo Yelp",
    layout="wide",
)

left, center, right = st.columns([1, 3, 1])

with center:
    st.image("images/logo_fixed.png", width="stretch")

##st.markdown(
##    "<h1 style='text-align: center;'>Tokyo Yelp</h1>",
##    unsafe_allow_html=True,
##) 
=======
def get_section_height(
    row_results,
    field_name,
    characters_per_line,
    line_height,
    padding,
):
    longest_length = max(
        (
            len(
                str(
                    restaurant.get(
                        field_name,
                        "",
                    )
                )
            )
            for restaurant in row_results
        ),
        default=1,
    )

    number_of_lines = max(
        1,
        math.ceil(
            longest_length / characters_per_line
        ),
    )

    return (
        number_of_lines * line_height
    ) + padding


st.title("🍣 TokyoYelp")
st.write("Find your next favorite restaurant in Tokyo.")
>>>>>>> Stashed changes


search = st.text_input(
    "What are you looking for?",
    placeholder="Try: sushi near Shibuya",
)


st.markdown("### Choose your cuisine")

cuisine_options = [
    # Original categories
    "Ramen",
    "Sushi",
    "Izakaya",
    "Yakiniku",
    "Tempura",
    "Yakitori",
    "Udon",
    "Soba",
    "Japanese",
    "Seafood",

    # New categories
    "Spanish",
    "Italian",
    "Fusion",
    "Chinese",
    "French",
]


try:
    selected_cuisines = st.pills(
        "Cuisine",
        cuisine_options,
        selection_mode="multi",
        label_visibility="collapsed",
        key="all_cuisines",
    ) or []
except AttributeError:
    selected_cuisines = st.multiselect(
        "Cuisine",
        cuisine_options,
        key="all_cuisines_fallback",
    )


st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    neighborhood = st.selectbox(
        "Neighborhood",
        [
            "Anywhere",
            "Chiyoda",
            "Shinjuku",
            "Shibuya",
            "Taito",
            "Minato",
            "Chuo",
        ],
    )

with col2:
    budget = st.selectbox(
        "Budget",
        [
            "Any",
            "¥",
            "¥¥",
            "¥¥¥",
            "¥¥¥¥",
            "¥¥¥¥¥",
        ],
    )

with col3:
    rating = st.selectbox(
        "Tabelog Rating",
<<<<<<< Updated upstream
        ["Any", "⭐ ()>2.4)", "⭐⭐ (>2.7)", "⭐⭐⭐ (>3)", "⭐⭐⭐⭐ (>3.3)", "⭐⭐⭐⭐⭐ (>3.5)"],
=======
        [
            "Any",
            "⭐ (>2.4)",
            "⭐⭐ (>2.7)",
            "⭐⭐⭐ (>3.0)",
            "⭐⭐⭐⭐ (>3.3)",
            "⭐⭐⭐⭐⭐ (>3.5)",
        ],
>>>>>>> Stashed changes
    )


st.divider()
st.subheader("Recommended restaurants")


try:
    restaurants = get_restaurants()

    results = recommend(
        restaurants=restaurants,
        area=neighborhood,
        cuisines=selected_cuisines,
        rating=rating,
        search_text=search,
        budget=budget,
    )

    if results:
        st.markdown("### Ask AI to choose for you")

        preference = st.text_input(
            "What matters most to you?",
            placeholder=(
                "Example: best value for money, "
                "highest rating, or cheapest dinner"
            ),
        )

        if st.button("Ask AI to Pick"):
            groq_api_key = os.getenv("GROQ_API_KEY")

<<<<<<< Updated upstream
        filtered_results = []
        
        #fitering 
=======
            if not groq_api_key:
                st.error("GROQ_API_KEY is not set.")
>>>>>>> Stashed changes

            elif not preference.strip():
                st.warning(
                    "Tell the AI what matters most to you."
                )

            else:
                candidates = results[:20]

                options = "\n".join(
                    (
                        f"{index}: "
                        f"{restaurant.get('name', '')} | "
                        f"Cuisine: "
                        f"{restaurant.get('genre', '')} | "
                        f"Rating: "
                        f"{restaurant.get('rating', 0)} | "
                        f"Dinner price: "
                        f"{restaurant.get('dinner_budget', '')} | "
                        f"Address: "
                        f"{restaurant.get('address', '')}"
                    )
                    for index, restaurant in enumerate(candidates)
                )

                try:
                    response = requests.post(
                        (
                            "https://api.groq.com/openai/v1/"
                            "chat/completions"
                        ),
                        headers={
                            "Authorization": (
                                f"Bearer {groq_api_key}"
                            ),
                            "Content-Type": "application/json",
                        },
                        json={
                            "model": "openai/gpt-oss-20b",
                            "messages": [
                                {
                                    "role": "user",
                                    "content": (
                                        "Choose the best restaurant "
                                        "based on this preference: "
                                        f"{preference}\n\n"
                                        "Return only valid JSON with "
                                        "an integer called 'index' and "
                                        "a short string called 'reason'.\n\n"
                                        f"Restaurants:\n{options}"
                                    ),
                                }
                            ],
                            "response_format": {
                                "type": "json_object"
                            },
                            "reasoning_effort": "low",
                        },
                        timeout=30,
                    )

                    response.raise_for_status()

                    pick = json.loads(
                        response.json()["choices"][0]["message"][
                            "content"
                        ]
                    )

                    selected_index = int(pick["index"])

                    if 0 <= selected_index < len(candidates):
                        selected_restaurant = candidates[
                            selected_index
                        ]

                        st.success(
                            "AI recommends: "
                            f"{selected_restaurant['name']}"
                        )

                        st.write(
                            pick.get(
                                "reason",
                                "This restaurant matches your preference.",
                            )
                        )
                    else:
                        st.error(
                            "The AI returned an invalid restaurant."
                        )

                except requests.RequestException as error:
                    st.error(
                        f"Unable to contact the AI service: {error}"
                    )

<<<<<<< Updated upstream
            if budget == "¥" * tier:
                filtered.append(r)

        results = filtered
        
        
        
    ### AI INTEGRATION   
    # Groq - open-models
    if results:
        preference = st.text_input(
            "What matters most to you?", placeholder='Try: "best value for money"  or  "rating to price ratio"'
        )

        if st.button("Ask AI to Pick"):
            candidates = results[:20] # lists our dict, first 20 entries seen by 

            # convert to strings like below:
            #0: Restaurant A | 寿司 | Rating: 3.8 | Price: ￥3,000～￥3,999
            #1: Restaurant B | ラーメン | Rating: 3.5 | Price: ￥1,000～￥1,999
            options = "\n".join(
                f"{i}: {r['name']} | {r['genre']} | "
                f"Rating: {r['rating']} | Price: {r['dinner_budget']}"
                for i, r in enumerate(candidates)
            )

            # API, sending data to groq
            response = requests.post(
                "https://api.groq.com/openai/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {os.environ['GROQ_API_KEY']}"
                },
                json={
                    "model": "openai/gpt-oss-20b",
                    "messages": [{
                        "role": "user",
                        "content": (
                            f"Choose the best restaurant for: {preference}. "
                            "Return JSON with an integer 'index' and "
                            "a short 'reason'. Use only these options "
                            f"numbered from 0:\n{options}"
                        )
                    }],
                    "response_format": {"type": "json_object"},
                    "reasoning_effort": "low"
                },
                timeout=30
            )
            response.raise_for_status()

            pick = json.loads(
                response.json()["choices"][0]["message"]["content"]
            )
            index = int(pick["index"])

            if 0 <= index < len(candidates):
                st.success(f"AI recommends: {candidates[index]['name']}")
                st.write(pick["reason"])
            else:
                st.error("AI returned an invalid restaurant.")

=======
                except (
                    KeyError,
                    ValueError,
                    json.JSONDecodeError,
                ):
                    st.error(
                        "The AI returned an invalid response."
                    )
>>>>>>> Stashed changes

    if not results:
        st.info(
            "No restaurants found. "
            "Try changing your search or filters."
        )

    else:
        records_per_page = 24
        records_per_row = 4

        current_filters = (
            search,
            tuple(selected_cuisines),
            neighborhood,
            budget,
            rating,
        )

        if (
            "last_filters" not in st.session_state
            or st.session_state.last_filters != current_filters
        ):
            st.session_state.page = 0
            st.session_state.last_filters = current_filters

<<<<<<< Updated upstream
                st.write(
                    f"**Address:** "
                    f"{restaurant['address']}"
                )

                st.write(
                    f"**Nearest station:** "
                    f"{restaurant['station']} "
                    f"({restaurant['distance']} meters)"
                )

                st.write(
                    f"**Genre:** "
                    f"{restaurant['genre']}"
                )

                st.write(
                    f"**Rating:** "
                    f"{restaurant['rating']}"
                )

                st.write(
                    f"**Reviews:** "
                    f"{restaurant['review_count']}"
                )

                st.write(
                    f"**Dinner budget:** "
                    f"{restaurant['dinner_budget']}"
                )
=======
        if "page" not in st.session_state:
            st.session_state.page = 0

        total_pages = math.ceil(
            len(results) / records_per_page
        )

        current_page = min(
            st.session_state.page,
            total_pages - 1,
        )

        start_index = current_page * records_per_page
        end_index = start_index + records_per_page

        page_results = results[start_index:end_index]

        nav_col1, nav_col2, nav_col3 = st.columns(
            [1, 6, 1]
        )

        with nav_col1:
            previous_clicked = st.button(
                "← Previous",
                disabled=current_page == 0,
                use_container_width=True,
            )

        with nav_col2:
            st.markdown(
                f"Page {current_page + 1} of {total_pages} "
                f"| Restaurants {start_index + 1}–"
                f"{start_index + len(page_results)} "
                f"of {len(results)}"
            )

        with nav_col3:
            next_clicked = st.button(
                "Next →",
                disabled=current_page >= total_pages - 1,
                use_container_width=True,
            )

        if previous_clicked:
            st.session_state.page -= 1
            st.rerun()

        if next_clicked:
            st.session_state.page += 1
            st.rerun()

        for row_start in range(
            0,
            len(page_results),
            records_per_row,
        ):
            row_results = page_results[
                row_start:row_start + records_per_row
            ]

            # Every card in this row receives the same
            # height for each matching section.
            title_height = get_section_height(
                row_results=row_results,
                field_name="name",
                characters_per_line=18,
                line_height=38,
                padding=24,
            )

            cuisine_height = get_section_height(
                row_results=row_results,
                field_name="genre",
                characters_per_line=25,
                line_height=25,
                padding=20,
            )

            station_height = get_section_height(
                row_results=row_results,
                field_name="station",
                characters_per_line=25,
                line_height=25,
                padding=20,
            )

            address_height = get_section_height(
                row_results=row_results,
                field_name="address",
                characters_per_line=24,
                line_height=25,
                padding=20,
            )

            row_card_height = (
                title_height
                + cuisine_height
                + station_height
                + address_height
                + 260
            )

            columns = st.columns(records_per_row)

            for column, restaurant in zip(
                columns,
                row_results,
            ):
                with column:
                    with st.container(
                        border=True,
                        height=row_card_height,
                    ):
                        # All four title sections have
                        # the same height in this row.
                        with st.container(
                            height=title_height
                        ):
                            st.subheader(
                                restaurant.get(
                                    "name",
                                    "",
                                )
                            )

                        # All cuisine sections line up.
                        with st.container(
                            height=cuisine_height
                        ):
                            st.write(
                                f"🍱 **Cuisine:** "
                                f"{restaurant.get(
                                    'genre',
                                    '',
                                )}"
                            )

                        st.divider()

                        st.write(
                            f"⭐ **Rating:** "
                            f"{float(
                                restaurant.get(
                                    "rating",
                                    0,
                                )
                            ):.2f}"
                        )

                        st.write(
                            f"📝 **Reviews:** "
                            f"{int(
                                restaurant.get(
                                    "review_count",
                                    0,
                                )
                            )}"
                        )

                        # All station sections line up.
                        with st.container(
                            height=station_height
                        ):
                            st.write(
                                f"🚉 **Station:** "
                                f"{restaurant.get(
                                    'station',
                                    '',
                                )} "
                                f"({float(
                                    restaurant.get(
                                        'distance',
                                        0,
                                    )
                                ):.0f} m)"
                            )

                        st.write(
                            f"💴 **Dinner:** "
                            f"{restaurant.get(
                                'dinner_budget',
                                '',
                            )}"
                        )

                        # All address sections line up.
                        with st.container(
                            height=address_height
                        ):
                            st.write(
                                f"📍 **Address:** "
                                f"{restaurant.get(
                                    'address',
                                    '',
                                )}"
                            )

        # Only add the black line after a complete page.
        if len(page_results) == records_per_page:
            st.markdown(
                """
                <hr style="
                    border: none;
                    border-top: 7px solid black;
                    margin: 35px 0;
                ">
                """,
                unsafe_allow_html=True,
            )

>>>>>>> Stashed changes

except Exception as error:
    st.exception(error)
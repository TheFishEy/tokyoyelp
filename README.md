# TokyoYelp

## Description

TokyoYelp recommends food and restaurants using a Kaggle dataset based on Tabelog, a Japanese restaurant-review platform similar to Yelp.

The dataset helps match users with restaurants based on cuisine, location, budget, ratings, and search preferences.

Tabelog is a Japanese-style Yelp that Japanese residents commonly use for food and restaurant recommendations. Foreign visitors may have difficulty navigating the platform, so TokyoYelp provides a simple and intuitive experience for English-speaking users.

## Features

- Search for restaurants using keywords
- Filter restaurants by cuisine
- Select multiple cuisine categories
- Filter restaurants by neighborhood
- Filter restaurants by budget
- Filter restaurants by Tabelog rating
- View restaurant addresses
- View restaurant genres
- View restaurant ratings
- View review counts
- View dinner budgets
- Receive restaurant recommendations
- Browse restaurants using pagination
- Display 24 restaurants per page
- Use AI to select a restaurant based on personal preferences
- Display Japanese-inspired colors and styling

## Cuisine Categories

The application supports the following cuisine categories:

- Ramen
- Sushi
- Izakaya
- Yakiniku
- Tempura
- Yakitori
- Udon
- Soba
- Japanese
- Seafood
- Spanish
- Italian
- Fusion
- Chinese
- French

## Technologies Used

- Python
- Streamlit
- Pandas
- Requests
- Groq API
- Kaggle
- ChatGPT

## Dataset Credit

The restaurant dataset was obtained from Kaggle.

The dataset is based on restaurant information from Tabelog.

Dataset source:

[Kaggle: Tokyo Restaurant Reviews on Tabelog](https://www.kaggle.com/datasets/utm529fg/tokyo-restaurant-reviews-on-tabelog?resource=download)

Please follow the original dataset's license and attribution requirements.

## Project Structure

```text
tokyoyelp/
│
├── app.py
├── data.py
├── recommender.py
├── requirements.txt
│
├── data/
│   └── restaurants_english_final.csv
│
└── images/
    ├── logo_fixed.png
    └── pexels-cristiano-sinisterra-3279598-5197132.jpg
```

## Requirements

Before installing the project, make sure you have:

- Python 3.10 or newer
- Git
- Internet access

## Installation

### Step 1: Clone the repository

Open PowerShell, Terminal, or Command Prompt and run:

```bash
git clone https://github.com/TheFishEy/tokyoyelp.git
```

### Step 2: Enter the project folder

```bash
cd tokyoyelp
```

### Step 3: Create a virtual environment

For Windows PowerShell:

```powershell
py -m venv .venv
```

For macOS or Linux:

```bash
python3 -m venv .venv
```

### Step 4: Activate the virtual environment

For Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

For Windows Command Prompt:

```cmd
.venv\Scripts\activate
```

For macOS or Linux:

```bash
source .venv/bin/activate
```

After activation, your terminal should display something similar to:

```text
(.venv)
```

### Step 5: Install the required packages

If the project includes a `requirements.txt` file, run:

```bash
pip install -r requirements.txt
```

If the project does not include a `requirements.txt` file, install the packages manually:

```bash
pip install streamlit pandas requests
```

### Step 6: Download the dataset

Download the dataset from Kaggle:

[Kaggle: Tokyo Restaurant Reviews on Tabelog](https://www.kaggle.com/datasets/utm529fg/tokyo-restaurant-reviews-on-tabelog?resource=download)

After downloading the dataset:

1. Extract the downloaded file.
2. Find the restaurant CSV file.
3. Create a folder named `data` inside the project folder.
4. Place the CSV file inside the `data` folder.
5. Rename the CSV file to:

```text
restaurants_english_final.csv
```

The final location should be:

```text
data/restaurants_english_final.csv
```

### Step 7: Add the optional images

Create a folder named `images` inside the project folder.

Place the following files inside the `images` folder:

```text
logo_fixed.png
pexels-cristiano-sinisterra-3279598-5197132.jpg
```

The image files are optional. The application can still run without them, but the logo and hero image will not appear.

### Step 8: Run the application

Run the following command from the main project folder:

```bash
python -m streamlit run app.py
```

For Windows, you can also use:

```powershell
py -m streamlit run app.py
```

### Step 9: Open the application

After running the command, Streamlit will display a local URL similar to:

```text
Local URL: http://localhost:8501
```

Open this URL in your browser:

[http://localhost:8501](http://localhost:8501)

## Using the Application

### Search for a restaurant

Enter keywords into the search box.

Examples:

```text
sushi
```

```text
ramen near Shibuya
```

```text
Italian restaurant
```

### Select cuisine categories

Click one or more cuisine tags to filter restaurants by cuisine.

Multiple cuisine tags can be selected at the same time.

### Select a neighborhood

Choose a neighborhood from the dropdown menu.

Available neighborhoods include:

- Anywhere
- Chiyoda
- Shinjuku
- Shibuya
- Taito
- Minato
- Chuo

### Select a budget

Choose a budget level:

- ¥
- ¥¥
- ¥¥¥
- ¥¥¥¥
- ¥¥¥¥¥

### Select a rating

Choose a minimum Tabelog rating:

- Any rating
- Above 2.4
- Above 2.7
- Above 3.0
- Above 3.3
- Above 3.5

### Browse restaurant pages

The application displays 24 restaurants per page.

Use the following buttons to navigate:

- `Previous`
- `Next`

## Optional AI Feature

The main restaurant search and filtering features do not require an AI API key.

If an AI API key is configured, users can enter a preference such as:

```text
Best value for money
```

```text
Near tokyo station
```

```text
Something trendy and fast
```

The AI will select a restaurant from the filtered results and provide a short explanation.

## Stopping the Application

To stop the Streamlit application, return to the terminal and press:

```text
Ctrl + C
```

## Troubleshooting

### Streamlit is not recognized

If you see:

```text
streamlit is not recognized
```

Run:

```bash
python -m streamlit run app.py
```

On Windows, run:

```powershell
py -m streamlit run app.py
```

### Dataset not found

If you see:

```text
Dataset not found
```

Make sure the dataset is located at:

```text
data/restaurants_english_final.csv
```

Make sure the filename is spelled exactly:

```text
restaurants_english_final.csv
```

### ModuleNotFoundError

If you see an error such as:

```text
ModuleNotFoundError: No module named 'streamlit'
```

Install the required packages:

```bash
pip install streamlit pandas requests
```

### The logo or hero image does not appear

Make sure the image files are placed in:

```text
images/
```

The expected filenames are:

```text
logo_fixed.png
pexels-cristiano-sinisterra-3279598-5197132.jpg
```

## AI Usage

AI tools, including ChatGPT, were used to assist with generating and developing portions of the code.

The team reviewed, tested, corrected, and refined the AI-assisted code to ensure that it worked properly and met the project's requirements.

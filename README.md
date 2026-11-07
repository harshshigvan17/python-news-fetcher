# python-news-fetcher

Search and read the latest news from your terminal using Python and NewsAPI.

## Requirements

- Python 3
- `requests` library
- A free API key from [newsapi.org](https://newsapi.org)

## Setup

1. Install the library:

   pip install requests

2. Set your API key as an environment variable (Windows):

   setx NEWS_API_KEY "your_api_key"

   Then restart your terminal or VS Code.

## Usage

Run the program:

   python main.py

Type a topic (for example `sports` or `technology`) to see the latest news. Type `quit` to exit.

## Notes

- The free NewsAPI plan only returns articles from roughly the last month.
- Never share your API key or upload it to GitHub.

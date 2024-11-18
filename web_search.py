import requests
import os

SERPAPI_KEY = os.getenv("SERPAPI_KEY")

def search_query(query):
    try:
        url = f"https://serpapi.com/search.json?q={query}&api_key={SERPAPI_KEY}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json().get("organic_results", [])
    except requests.exceptions.RequestException as e:
        return f"Error: Unable to fetch search results for query '{query}'. Details: {e}"

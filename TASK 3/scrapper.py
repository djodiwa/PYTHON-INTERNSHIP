import requests
from bs4 import BeautifulSoup
import time  # For retry delays
import re   # For URL matching and filename sanitization

def sanitize_filename(name):
    # Replace invalid filename chars with underscores
    return re.sub(r'[\\/:*?"<>|]', '_', name)

def scrape_headlines(url):
    try:
        # Fetch with timeout to avoid hanging
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raises HTTPError for 4xx/5xx errors
        
        # Parse HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract site name from <title> tag
        site_name = soup.title.string.strip() if soup.title and soup.title.string else "default"
        site_name = sanitize_filename(site_name)
        filename = f"{site_name}-headlines.txt"
        
        # Auto-detect selector: Try common patterns, pick first with 5+ results
        selectors = [
            'h1', 'h2', 'h3',  # Basic headings
            'h2.title', 'h3.headline', 'span.title',  # Common classes
        ]
        headlines = []
        used_selector = None
        
        # HN-specific: Check URL and use precise table parser for story titles
        if 'ycombinator' in url.lower():
            used_selector = "HN Story Rows (<tr class='athing' ><a class='storylink'>)"
            rows = soup.find_all('tr', class_='athing')[:30]  # Top 30 stories only
            headlines = [row.find('a', class_='storylink').get_text(strip=True) 
                         for row in rows if row.find('a', class_='storylink')]
        else:
            for sel in selectors:
                potential = [h.get_text(strip=True) for h in soup.select(sel)]
                if len(potential) >= 5:  # Threshold to avoid empty/junk
                    headlines = potential
                    used_selector = f"CSS: {sel}"
                    break
        
        # Fallback: If still empty, try all <a> with length > 20 (rough headline filter)
        if not headlines:
            all_links = [a.get_text(strip=True) for a in soup.find_all('a') if len(a.get_text(strip=True)) > 20]
            headlines = all_links[:30]  # Limit to top 30
            used_selector = "Fallback: Long <a> texts"
            if not headlines:
                raise ValueError("No headlines found - site may use unusual structure")
        
        # Save to file
        with open(filename, 'w', encoding='utf-8') as f:
            for headline in headlines:
                f.write(headline + '\n')
        
        print(f"Success using selector '{used_selector}'! Scraped {len(headlines)} headlines and saved to {filename}")
        return True
        
    except requests.exceptions.RequestException as e:
        print(f"Request error during fetch: {e}")
        return False
    except ValueError as e:
        print(f"Parsing error: {e}")
        return False
    except Exception as e:
        print(f"Unexpected scraping error: {e}")
        return False

if __name__ == "__main__":
    # Ask user for URL (default to HN)
    default_url = "https://news.ycombinator.com/"
    user_url = input(f"Enter the news website URL (press Enter for default: {default_url}): ").strip()
    if not user_url:
        user_url = default_url
    print(f"Using URL: {user_url}")
    
    max_attempts = 5  # Configurable: Change this for more/fewer retries
    for attempt in range(1, max_attempts + 1):
        print(f"\n--- Attempt {attempt}/{max_attempts} ---")
        if scrape_headlines(user_url):
            print("Scraping completed successfully!")
            break  # Exit loop on success
        else:
            if attempt < max_attempts:
                print("Retrying in 3 seconds...")
                time.sleep(3)
            else:
                print("\nAll attempts failed. Check your connection, site availability, or try a different URL.")

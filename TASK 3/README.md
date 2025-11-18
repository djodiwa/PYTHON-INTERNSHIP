# WEB DEVELOPMENT INTERNSHIP - Task 3: Web Scraper for News Headlines

## Overview
This project fulfills Task 3 of the web development internship by implementing a Python-based web scraper to extract and automate the collection of top headlines from public news websites. Utilizing the `requests` library for HTTP requests and `BeautifulSoup` for HTML parsing, the script targets structured content such as `<h2>` or equivalent title elements. For demonstration, it is configured to scrape Hacker News (https://news.ycombinator.com/), a static site with clear headline markup, ensuring ethical and efficient data retrieval. The output is saved to a dynamically named text file, with built-in mechanisms for reliability and adaptability across sites.

## Demonstration of the Developed Web Scraper

![Demo GIF](assest/demo-clip.gif)
*The recording shows the complete execution flow — launching the script in the terminal, entering the default Hacker News URL, real-time retry/processing messages, confirmation of successful extraction using the Hacker News-specific selector, and the resulting "Hacker News-headlines.txt" file being automatically created and opened in the editor with the 30 cleanly scraped headlines visible.*

## Features
- **Interactive URL Configuration**: User is prompted to input a custom website URL, defaulting to Hacker News for immediate testing.
- **Dynamic Output Filename**: The text file is named based on the site's `<title>` tag (e.g., "Hacker News-headlines.txt"), with automatic sanitization to replace invalid characters.
- **Precise Headline Extraction**: Site-specific parsing for Hacker News using `<tr class="athing">` and `<a class="storylink">` selectors to retrieve only relevant story titles; general fallback logic tests common heading tags (e.g., `h2.title`, `h3.headline`) and long anchor texts for broader compatibility.
- **Retry and Resilience**: Supports up to five fetch attempts with 3-second intervals to mitigate transient network or parsing failures.
- **Comprehensive Error Management**: Handles HTTP errors, timeouts, empty results, and exceptions with descriptive console messages, ensuring graceful degradation without termination.
- **Optimized Data Handling**: Limits extraction to the top 30 headlines, applies text stripping for cleanliness, and uses UTF-8 encoding for robust file output.

## Tools and Setup
- **Development Environment**: Visual Studio Code (with Python extension for linting and execution).
- **Runtime**: Python 3.12.
- **Dependencies**: `requests` (for web requests) and `beautifulsoup4` (for parsing).

Prerequisites: Python 3.x installed on the system.

## How to Run the Web Scraper
1. **Create and Activate a Virtual Environment** (Recommended for dependency isolation):  
   **Linux / macOS**:  
   ```bash
   python3 -m venv scraper-env
   source scraper-env/bin/activate
   ```  
   **Windows**:  
   ```cmd
   python -m venv scraper-env
   scraper-env\Scripts\activate
   ```

2. **Install Required Libraries**:  
   ```bash
   pip install requests beautifulsoup4
   ```

3. **Download and Place the Script**:  
   - Save the provided code as `scraper.py`.  
   - Place `scraper.py` inside the `scraper-env` folder (alongside the virtual environment structure):  
     ```
     scraper-env/
     ├── scraper.py          ← Place the script here
     ├── bin/   (or Scripts/ on Windows)
     ├── lib/
     └── ...
     ```

4. **Execute the Script**:  
   ```bash
   python scraper.py
   ```

5. **Expected Behavior**:  
   - The script prompts for a URL (press Enter for the default Hacker News).  
   - It performs the scrape, displaying progress and any errors.  
   - On success: Outputs a confirmation message (e.g., "Scraped 30 headlines and saved to Hacker News-headlines.txt").  
   - The file is generated in the same directory.

To deactivate the virtual environment: Run `deactivate`.

## Development Process
The implementation followed the task's mini-guide iteratively within Visual Studio Code, with incremental testing via the integrated terminal.

1. **HTML Fetching with Requests**: Configured `requests.get()` with a 10-second timeout and status validation using `raise_for_status()`. Incorporated user input for the URL via `input()`.

2. **Parsing with BeautifulSoup**: Initialized the parser with `'html.parser'`. Implemented selector prioritization: Hacker News-specific extraction via `find_all('tr', class_='athing')` and inner `<a class="storylink">`; general trials across predefined CSS selectors; fallback to filtered long `<a>` elements.

3. **File Saving and Enhancements**: Derived the filename from `soup.title.string`, sanitized it using regex, and wrote headlines line-by-line to the file. Enclosed the core logic in a retry loop with `try-except` blocks for error categories (requests exceptions, ValueError for empty results, general exceptions). Added console logging for the used selector and item count.

The total development time was approximately 45 minutes, emphasizing modularity for future extensions.

## Key Learnings
- **Site Variability in Web Structures**: Recognized the need for tailored selectors (e.g., table-based for Hacker News versus heading-based for others), highlighting the value of browser inspection tools for accuracy.
- **Production-Ready Reliability**: Integrated timeouts, retries, and granular error handling to simulate real-world deployment challenges, improving script robustness.
- **Dynamic Content Management**: Learned filename sanitization techniques to handle metadata like page titles safely across operating systems.
- **Efficiency in Automation**: Balancing extraction limits (e.g., top 30 items) prevents overload while delivering actionable data; UTF-8 encoding ensures compatibility with diverse text.

This task advanced proficiency in Python for data automation, bridging web fetching with structured output for potential integrations like analysis pipelines.

## Files Included
- `scraper.py`: The core executable script.
- `[Site Name]-headlines.txt`: Auto-generated output file (e.g., "Hacker News-headlines.txt" upon execution).

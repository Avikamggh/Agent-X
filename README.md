created by avikam 
class=11


# Agent-X
The script agent-x.py is an intelligent web optimization and analysis tool that performs automated webpage evaluation using web scraping and Google Gemini AI. Its primary functions include content extraction, SEO optimization, broken link detection, and identification of common SEO issues. It is intended to assist developers, SEO specialists, and content managers in improving webpage performance and visibility.

2. Webpage Content Extraction
Function: extract_webpage_content(url)

Sends an HTTP request to the given URL.

Parses the response using BeautifulSoup.

Extracts:

Page title

Meta description

Main textual content from <p> tags

Returns a dictionary with the extracted data.

Ensures a timeout of 10 seconds and includes a User-Agent header to avoid request blocks.

3. Content Optimization
Function: optimize_content(content)

Uses the Gemini Pro model to enhance the extracted content.

Focuses on improving readability and SEO effectiveness while preserving the original meaning.

Returns the optimized content as a string.

4. Broken Link Checker
Function: check_broken_links(url)

Scans all anchor (<a>) tags in the page.

Converts relative URLs to absolute ones if needed.

Sends HEAD requests to validate each link.

Collects and returns a list of links that return error codes (status code ≥ 400) or cannot be reached.

5. SEO Issues Analyzer
Function: analyze_seo_issues(content)

Performs basic SEO diagnostics:

Checks if the meta description is missing.

Flags if the title exceeds 60 characters (standard SEO guideline).

Alerts if the word count is too low (less than 300 words).

Returns a list of detected SEO issues.

6. Main Processing Function
Function: process_webpage(url)

Orchestrates the entire process:

Extracts the webpage content.

Optimizes the text using Gemini.

Checks for broken links.

Analyzes for SEO deficiencies.

Outputs a structured JSON report with:

Original title

Optimized content

List of broken links

Detected SEO issues

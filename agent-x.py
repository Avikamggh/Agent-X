import requests
from bs4 import BeautifulSoup
import google.generativeai as genai
import json

# Configure Google Gemini API Key (Replace with your actual API key)
genai.configure(api_key="AIzaSyBcja87aOwTxj7SpZ-APghimUnBpys6fIc")

# Function to extract webpage content
def extract_webpage_content(url):
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=10)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        text = ' '.join([p.text for p in soup.find_all('p')])  # Extract paragraphs
        title = soup.title.string if soup.title else "No Title"
        meta_desc = ""
        meta = soup.find("meta", attrs={"name": "description"})
        if meta:
            meta_desc = meta.get("content", "")
        return {"title": title, "description": meta_desc, "content": text}
    return None

# Function to analyze and optimize content using Google Gemini AI
def optimize_content(content):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(f"Improve the following webpage content for better readability and SEO while keeping the meaning intact:\n{content}")
    return response.text.strip()

# Function to check for broken links
def check_broken_links(url):
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        links = [a.get("href") for a in soup.find_all("a", href=True)]
        broken_links = []
        for link in links:
            try:
                if not link.startswith("http"):
                    link = url + link  # Convert relative to absolute URL
                res = requests.head(link, allow_redirects=True, timeout=5)
                if res.status_code >= 400:
                    broken_links.append(link)
            except requests.exceptions.RequestException:
                broken_links.append(link)
        return broken_links
    return []

# Function to analyze SEO issues
def analyze_seo_issues(content):
    missing_meta = "Meta description is missing." if not content["description"] else ""
    long_title = "Title is too long." if len(content["title"]) > 60 else ""
    low_keyword_density = "Consider adding more relevant keywords for SEO." if len(content["content"].split()) < 300 else ""
    return [issue for issue in [missing_meta, long_title, low_keyword_density] if issue]

# Main function to process a webpage
def process_webpage(url):
    print(f"Processing {url}...")
    content = extract_webpage_content(url)
    if content:
        optimized_content = optimize_content(content["content"])
        broken_links = check_broken_links(url)
        seo_issues = analyze_seo_issues(content)
        
        results = {
            "title": content["title"],
            "optimized_content": optimized_content,
            "broken_links": broken_links,
            "seo_issues": seo_issues
        }
        print(json.dumps(results, indent=4))
        return results
    else:
        return {"error": "Failed to fetch webpage"}

# Example usage
if __name__ == "__main__":
    test_url = "https://physicsexplorer.netlify.app/v"
    process_webpage(test_url)

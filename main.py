import bs4 as bs
import requests as r
import streamlit as st
from scraper import scrape_url


### Global Variables
website_urls = []
filename = "scraped_content.txt" # File to save content to
content = [] # list contents of website

# Example URLs
# https://books.toscrape.com/, https://www.perplexity.ai/, https://www.google.com/
#


# streamlit UI and logic
st.title("Web Scraper")
url_input = st.text_input("Enter URLs to scrape (comma separated):")
if st.button("Scrape"):

    website_urls.extend([url.strip() for url in url_input.split(',') if url.strip()]) # Format URLs into a list
    
    for i in website_urls:
        st.write(f"Scraping the website... {i}")


        result = scrape_url(i)
        print(result)
        content.append(result)


        # Save content to the text file
        with open(filename, "w") as file:
            for i in content:
                file.write(i + "\n")

        st.write(f"Content saved to {filename}")


import requests as r
import streamlit as st
from scraper import scrape_url, split_dom, extract_content, clean_body
import parse


### Global Variables
website_urls = []
filename = "scraped_content.txt" # File to save content to
text_to_save = [] # list contents of website

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
        body_content = extract_content(result)
        cleaned_body = clean_body(body_content)
        print("Cleanup successful")

        st.session_state.dom_content = cleaned_body

        with st.expander("View DOM Content"):
            st.text_area("DOM Content", cleaned_body, height=300)

        print("DOM content extracted successfully")


if "dom_content" in st.session_state:
    parse_description = st.text_area("Describe the info you need")

    if st.button("Parse"):
        if parse_description:
            st.write("Parsing content...")
            print("Parsing content...")

            dom_chunks = split_dom(st.session_state.dom_content)

            parsed_results = parse.parse_withAI(dom_chunks, parse_description)
            print("Parsing completed")
            st.write(parsed_results)


            text_to_save.append(parsed_results)


            # Save content to the text file
            with open(filename, "w") as file:
                for i in text_to_save:
                    file.write(i + "\n")

            st.write(f"Content saved to {filename}")
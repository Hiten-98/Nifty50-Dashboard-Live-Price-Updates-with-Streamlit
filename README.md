# Nifty50-Dashboard-Live-Price-Updates-with-Streamlit

This is a simple dashboard which provides real-time Nifty50 price that updates live without the need for manual page refresh. The dashboard provides up-to-date information on the prices of the Nifty50 index constituents.

To achieve this, I utilized Streamlit's interactive features and integration with web scraping tools.

Here's an overview of the key components and functionalities of the dashboard:

Web Scraping: I utilized the BeautifulSoup library to scrape the required data from a trusted financial website. This allowed me to retrieve the latest prices of the Nifty50 index stocks.

Real-Time Updates: By leveraging Streamlit's continuous execution model, I implemented a program that constantly refreshes the scraped data at a specific interval. This ensures that the dashboard always displays the most recent prices without manual intervention.




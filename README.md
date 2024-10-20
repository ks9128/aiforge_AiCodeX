# aiforge_AiCodeX
# YouTube Comments Scraper and Sentiment Analysis Project

## Overview
This project scrapes YouTube comments from a video and performs sentiment analysis using the Aixplain API pipeline. It generates two CSV files:

- **comments.csv**: Contains the scraped comments.
- **comments_with_sentiment.csv**: Contains the comments along with their sentiment labels.

### This project utilizes the following technologies:
- **YouTube API** for scraping comments.
- **Aixplain.com** pipeline for sentiment analysis.

## Requirements
Make sure to install the necessary dependencies before running the project. Use the following command to install the required Python packages:

```bash
pip install -r requirements.txt
Instructions
Step 1: Scraping YouTube Comments
Navigate to the comments_scraper.py file.
Replace the placeholder api_key with your YouTube API key.
Run the script to scrape comments from a YouTube video, which will be saved as comments.csv.
python comments_scraper.py
Step 2: Sentiment_Analysis
Open the sentiment_analysis.py file.
Replace the placeholder api_url with your Aixplain API pipeline URL.
Replace the placeholder api_key with your Aixplain API key.
Run the script to analyze the comments' sentiment, which will be saved as comments_with_sentiment.csv.
python sentiment_analysis.py
Output Files
comments.csv: Contains the YouTube comments scraped using the YouTube API.
comments_with_sentiment.csv: Contains comments along with their respective sentiment labels processed through Aixplain.com.
Output Files
comments.csv: Contains the YouTube comments scraped using the YouTube API.
comments_with_sentiment.csv: Contains comments along with their respective sentiment labels processed through Aixplain.com.

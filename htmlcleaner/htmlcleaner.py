from bs4 import BeautifulSoup
import numpy as np 
import pandas as pd
import os

# Directory path where HTML files are stored
directory = r''  

# Empty list to store all data
data = []

# Iterating through HTML file in the directory
for filename in os.listdir(directory):
    if filename.endswith('.html'):
        filepath = os.path.join(directory, filename)

        # Loading each HTML file, read and utf-8
        with open(filepath, 'r', encoding='utf-8') as file:
            html_content = file.read()

        # Parsing HTML content with BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')

        # Finding all articles (abstract-col2 divs has all the data)
        articles = soup.find_all('div', class_='abstract-col2')

        # Iterate over each article with empty dictionary
        for article in articles:
            article_data = {}

            # Extract Journal Title (first <label> tag)
            journal_title_tag = article.find('label')
            if journal_title_tag:
                article_data['Journal Title'] = journal_title_tag.get_text(strip=True)

            # Extract Citation (<strong> tag with 'Citation' to next <p>)
            citation_tag = article.find('strong', string='Citation')
            if citation_tag:
                citation_text = citation_tag.find_next('p').get_text(strip=True)
                article_data['Citation'] = citation_text

            # Extract Copyright (<strong> tag with 'Copyright' to next <p>)
            copyright_tag = article.find('strong', string='Copyright')
            if copyright_tag:
                copyright_text = copyright_tag.find_next('p').get_text(strip=True)
                article_data['Copyright'] = copyright_text

            # Extract DOI (<strong> tag with 'DOI' to next <p>), also changes 'unavailable' data to np.nan
            doi_tag = article.find('strong', string='DOI')
            if doi_tag:
                doi_text = doi_tag.find_next('p').get_text(strip=True)
                if doi_text.lower() == "unavailable":
                    article_data['DOI'] = np.nan
                else:
                    article_data['DOI'] = doi_text

            # Extract PMID (<strong> tag with 'PMID' to next <p>), also changes 'unavailable' data to np.nan
            pmid_tag = article.find('strong', string='PMID')
            if pmid_tag:
                pmid_text = pmid_tag.find_next('p').get_text(strip=True)
                if pmid_text.lower() == "unavailable":
                    article_data['PMID'] = np.nan
                else:
                    # Keeps only the first line as sometimes it pulls ex. "32983905 PMCID"
                    article_data['PMID'] = pmid_text.splitlines()[0].strip()

            # Extract Abstract (<strong> tag with 'Abstract' to next <p>), also changes empty abstracts or '[Abstract unavailable]' to np.nan
                abstract_tag = article.find('strong', string='Abstract')
                if abstract_tag:
                    abstract_text = abstract_tag.find_next('p').get_text("\n", strip=True)
                    
                if not abstract_text or "[Abstract unavailable]" in abstract_text:
                    article_data['Abstract'] = np.nan
                else:
                    article_data['Abstract'] = abstract_text

            # Extract Keywords (<strong> tag with 'Keywords' to next <p>)
            keywords_tag = article.find('strong', string='Keywords')
            if keywords_tag:
                keywords_text = keywords_tag.find_next('p').get_text(strip=True)
                article_data['Keywords'] = keywords_text

            # Adding the article/articles to the list
            data.append(article_data)

# Convert the it pandas DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv('raw_data.csv', index=False)
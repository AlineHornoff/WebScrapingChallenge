# Import Dependencies 
import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager
import time
#import requests

# Define initial browser for scrape
def init_browser():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

# Define scrape
def scrape():
    browser = init_browser()


    # ***********************************
    # Mars News Scrape
    # ***********************************

    MarsNews_URL = "https://redplanetscience.com/"

    # Print Scarping Mars News
    print("Scraping Mars News...")

    # Visit Mars News URL
    browser.visit(MarsNews_URL)
    time.sleep(1)

    # Scrape into BeautifulSoup by creating HTML object and parser HTML
    html = browser.html
    soup = bs(html, "html.parser")

    # Find and save News Title under <div> tag with class='content_title'
    NewsTitle = soup.find('div', class_='content_title').text

    # Find and save Praragraph text under <div> tag with class='article_teaser_body'
    NewsParagraph = soup.find('div', class_='article_teaser_body').text

    # Print Mars News: Scraping complete!
    print("Mars New: Scraping complete!")


    # ****************************************
    # JPL Mars Space Images (Featured Images) Scrape
    # ****************************************

    # Visit JPL Featured Space Image URL
    JPLimages_URL = 'https://spaceimages-mars.com/'
    browser.visit(JPLimages_URL)
    time.sleep(1)   

    # Scrape into BeautifulSoup by creating HTML object and parser HTML
    html = browser.html
    soup = bs(html, "html.parser")  

    # Get image from URL
    img = [i.get("src") for i in soup.find_all("img", class_="headerimage fade-in")]

    # Save URL string for image
    featured_image_url = JPLimages_URL + img[0]

    # Stop browser
    browser.quit()


    # ****************************
    # Mars Facts Scrape
    # ****************************

    # Visit Mars Facts URL
    MarsFacts_URL = 'https://galaxyfacts-mars.com/'

    # Scrape table from URL using pandas
    FactsTable = pd.read_html(MarsFacts_URL)

    # Create table dataframe
    df=FactsTable[1]
    df.columns=['Discription', 'Value']

    # Save table to html
    FactsHTML = df.to_html()

   # Stop browser
    browser.quit()


   # **************************************
   # Mars Hemispheres
   # **************************************

   # Visit Mars Hemisphere URL
    hemi_url = "https://marshemispheres.com/"
    browser.visit(hemi_url)
    hemisphere_image_urls = []

    for i in range(4):
        html = browser.html
        soup = bs(html, "html.parser")
    
        title = soup.find_all("h3")[i].get_text()
        browser.find_by_tag('h3')[i].click()
    
        html = browser.html
        soup = bs(html, "html.parser")
    
        img_url = soup.find("img", class_="wide-image")["src"]
    
        hemisphere_image_urls.append({
            "title": title,
            "img_url": hemi_url + img_url
        })
        browser.back()
        
    title1 = hemisphere_image_urls[0]["title"]
    image1 = hemisphere_image_urls[0]["img_url"]
    
    title2 = hemisphere_image_urls[1]["title"]
    image2 = hemisphere_image_urls[1]["img_url"]

    title3 = hemisphere_image_urls[2]["title"]
    image3 = hemisphere_image_urls[2]["img_url"]

    title4 = hemisphere_image_urls[3]["title"]
    image4 = hemisphere_image_urls[3]["img_url"]


    # ***********************************
    # Final dictionary for Mongo
    # ***********************************
    
    final_mars_data = {
    "latest_title": NewsTitle,
    "latest_paragraph" : NewsParagraph,
    "featured_image": featured_image_url,
    "html_table": FactsHTML,
    "hemisphere_scrape": hemisphere_image_urls,
    "title1": title1,
    "title2": title2,
    "title3": title3,
    "title4": title4,
    "image1": image1,
    "image2": image2,
    "image3": image3,
    "image4": image4,

    }

    return final_mars_data  


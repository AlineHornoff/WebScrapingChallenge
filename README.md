# WebScrapingChallenge - Mission to Mars

Let's leave this planet and travel to Mars! In this challenge information is scraped from websites by utilising Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter in part one. In part two MongoDB and Flask templating are used to create a HTML page to display all information that was scraped from the URLs.

## Mission to Mars - Part One
Data is collected from the following URLs

### NASA Mars News
* Collected Data: latest News Title and Paragraph Text
* Collect From: https://redplanetscience.com/

### JPL Mars Space Images - Featured Image
* Collected Data: Image url for the current Featured Mars Image
* https://spaceimages-mars.com/

### Mars Facts
* Collected Data: Table containing facts about the planet including Diameter, Mass, etc.
* Collect From: https://galaxyfacts-mars.com/

### Mars Hemispheres
* Collected Data: High resolution images for each of Mar's hemispheres
* Collect From: https://marshemispheres.com/


## Mission to Mars - Part Two
Use MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.

* Start by converting your Jupyter notebook into a Python script called scrape_mars.py with a function called scrape that will execute all of your scraping code from above and return one Python dictionary containing all of the scraped data.
* Next, create a route called /scrape that will import your scrape_mars.py script and call your scrape function.
* Store the return value in Mongo as a Python dictionary.
* Create a root route / that will query your Mongo database and pass the mars data into an HTML template to display the data.
* Create a template HTML file called index.html that will take the mars data dictionary and display all of the data in the appropriate HTML elements. Use the following as a guide for what the final product should look like, but feel free to create your own design.

## Output for Web Scraping Challenge
![MissionToMars](Images/MissionToMars.png)
![MissionToMars1](Images/MissionToMars1.png)
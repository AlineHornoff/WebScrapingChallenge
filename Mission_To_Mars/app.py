# Import dependencies
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Create an instance for flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mission_to_mars")

# Route to render index.html template using data from Mongo
@app.route("/")
def echo():

    # Find one record of data from the mongo database
    final_mars_data = mongo.db.collection.find_one()

    # Return template and data
    return render_template("index.html", final_mars_data=final_mars_data)

# Route that will trigger the scrape function
@app.route("/scrape")
def scrapping_mars():

    # Run the scrape function
    final_mars_data = scrape_mars.scrape()

    # Update the Mongo database using update and upsert=True
    mongo.db.collection.update({}, final_mars_data, upsert=True)

     # Redirect back to home page
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
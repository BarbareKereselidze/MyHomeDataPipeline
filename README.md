# MyHomeDataPipeline
This Python program is designed to scrape information about real estate properties for sale in Tbilisi from the MyHome website. 
It extracts details such as the phone number of the seller, seller's name, post date, property price (in GEL and USD), and type of property (house, flat, land, etc). The data is then stored in a MySQL database.

Notes:
* This program uses threading to improve performance by allowing multiple pages to be scraped simultaneously.
  Each thread corresponds to a page.
* The program handles HTTP errors and retries the last successful page if an error occurs.
* The database schema is set up to store the scraped information.


File Structure:
1. Main.py
   * Main script coordinating the scraping process.
   * Utilizes threading for concurrent page scraping.
   * Defines thread_function for each thread's behavior.
3. Scraper.py
   * Handles HTTP requests and HTML parsing.
   * Contains Scraper class for scraping main and advertisement pages.
   * Provides methods to retrieve HTML content.
5. PropertyScraper.py
   * Contains PropertyScraper class for extracting property details.
   * Methods for finding ID, phone number, owner name, post date, price, and property type.
6. InsertIntoMySQL.py
   * Manages MySQL database interactions.
   * Defines InsertIntoMySQL class for connecting, creating tables, and uploading data.
   * Provides method to close the database connection.
   Note: You can set up MySQL database (locally or on the cloud) and modify the InsertIntoMySQL class to use your database credentials.


Scheduling with Linux Cron:

To keep the data up-to-date, the program is scheduled to run daily at 9 AM. While I considered writing new code to retrieve data, it's important to note that advertisements on the website may not always appear in chronological order, even when selected as such. As a result, comparing every advertisement date can be slow.
For efficiency, it's recommended to re-run the original code to fetch new data, in this case we can avoid extensive date comparisons.

To automate the program to run daily you can follow these steps:
1. Open your terminal.
2. Edit your crontab file by running: crontab -e
3. Add the following line at the end of the file: 0 9 * * * /usr/bin/python3 /path/to/Main.py
   path to main should be replaced by the actual path to your Main.py file.
4. Save and exit the editor. The program will now run at 9 AM every day.


Dependencies:
* threading
* mysql.connector
* BeautifulSoup
* datetime and timedelta

these libraries can be installed with command: pip install...

import threading

from PropertyScraper import PropertyScraper
from InsertIntoMySQL import InsertIntoMySQL
from Scraper import Scraper


# Using User-Agent string to mimic a common user agent of the Chrome web browser
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36'
}


# Creating a function for each thread to execute
def thread_function(start_ind):
    ind = start_ind
    # Keeping track of last successful ind in case of an error
    last_successful_ind = start_ind
    scraper = Scraper(headers)
    db_inserter = InsertIntoMySQL()

    # Scraping each advertisement
    while True:
        try:
            soup = scraper.scrape_page(ind)
            advertisements = soup.find_all('a', class_="card-container")
            for advertisement in advertisements:
                url = advertisement['href']

                soup2 = scraper.scrape_advertisement(url)
                property_scraper = PropertyScraper(soup2)

                # Getting information from each advertisement
                home_id = property_scraper.find_home_id()
                phone_number = property_scraper.find_phone_number()
                owner_name = property_scraper.find_name()
                post_date = property_scraper.find_post_date()
                price_gel = property_scraper.find_price_gel()
                price_usd = property_scraper.find_price_usd()
                property_type = property_scraper.find_property()

                # Inserting that information into a database
                db_inserter.upload_data(home_id, phone_number, owner_name, post_date, price_gel, price_usd, property_type)

            if advertisements:
                last_successful_ind = ind
                ind += 10
                print(ind)
            else:
                print("done :3")
                db_inserter.close_connection()
                break

        # # In case of an error continuing from last successful index
        except Exception as e:
            print(f"Thread {start_ind}: An error occurred: {e}")
            ind = last_successful_ind


def main():
    threads = []

    # Creating and running 10 threads at once
    for i in range(1, 11):
        thread = threading.Thread(target=thread_function, args=(i,))
        threads.append(thread)
        thread.start()

    # Waiting for all 10 threads to complete
    for thread in threads:
        thread.join()


if __name__ == "__main__":
    main()


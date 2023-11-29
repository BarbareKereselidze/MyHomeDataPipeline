from datetime import datetime, timedelta


# Creating a class for scraping each property's details
class PropertyScraper:
    def __init__(self, soup):
        self.soup = soup

    def find_home_id(self):
        home_id = self.soup.find('div', class_="d-flex align-items-center id-container").find('span').text.replace(': ',
                                                                                                                   '')
        return home_id

    def find_phone_number(self):
        phone_number = self.soup.find_all('div', class_="texts")[2].find('div', class_="title").text.replace('ტელ: ',
                                                                                                             '')
        return phone_number

    def find_name(self):
        name = self.soup.find('span', class_="badge badge-success mt-1").text
        return name

    def find_post_date(self):
        post_date_str = self.soup.find('div', class_="d-flex align-items-center date").find('span').text[:-6]

        # Getting current and yesterday's date and formatting it to d-m-y format
        current_datetime = datetime.now()
        today = current_datetime.strftime("%d-%m-%Y")
        yesterday_datetime = current_datetime - timedelta(days=1)
        yesterday = yesterday_datetime.strftime("%d-%m-%Y")

        date_replacements = {
            "დღეს": today,
            "გუშინ": yesterday,
            " ოქტ.": '-10-2023',
            " სექტ.": '-09-2023',
            " აგვ.": '-08-2023',
            " ივლ.": '-07-2023',
            " ივნ.": '-06-2023',
            " მაი.": '-05-2023',
            " აპრ.": '-04-2023',
            " მარ.": '-03-2023',
            " თებ.": '-02-2023',
            " იანვ.": '-01-2023',
            " ნოე.": '-11-',
            " დეკ.": '-12-'
        }

        # Replacing the keywords so the date format matches throughout the data
        for keyword, replacement in date_replacements.items():
            if keyword in post_date_str:
                post_date_str = post_date_str.replace(keyword, replacement)

        # Turning the formatted string into a datetime object
        post_date = datetime.strptime(post_date_str, '%d-%m-%Y')

        # Reformatting post_date into y-m-d format, so it can be inserted into the database as DATE
        return post_date.strftime('%Y-%m-%d')

    def find_price_gel(self):
        price = self.soup.find('span', class_="d-block convertable")
        # Removing the comma, so it can be inserted into the database as FLOAT
        price_gel = price['data-price-gel'].replace(',', '')
        return price_gel

    def find_price_usd(self):
        price = self.soup.find('span', class_="d-block convertable")
        price_usd = price['data-price-usd'].replace(',', '')
        return price_usd

    def find_property(self):
        type_of_property = self.soup.find('div',
                                          class_="product-link-tree d-inline-flex flex-nowrap align-items-center").find(
            'a').text.replace('იყიდება ', '')
        return type_of_property


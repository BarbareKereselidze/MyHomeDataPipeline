import mysql.connector


# Creating a class to create, modify and close MySQL database
class InsertIntoMySQL:
    def __init__(self):

        # Connecting to MySQL server
        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='bjbj',
            charset='utf8mb4'
        )

        self.cursor = self.conn.cursor()
        self.create_database_and_table()

    def create_database_and_table(self):
        # Creating and switching to 'MyHomeData' database
        # Using character set (utf8mb4) and collation (utf8mb4_unicode_ci) to support Georgian Alphabet
        self.cursor.execute("CREATE DATABASE IF NOT EXISTS MyHomeData CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")
        self.cursor.execute("USE MyHomeData")

        create_table_query = '''
        CREATE TABLE IF NOT EXISTS myhome (
            home_id INT PRIMARY KEY,
            phone_number VARCHAR(15),
            owner_name VARCHAR(50),
            post_date DATE,
            price_gel FLOAT,
            price_usd FLOAT,
            property_type VARCHAR(50)
        )CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci
        '''
        self.cursor.execute(create_table_query)

    def upload_data(self, home_id, phone_number, owner_name, post_date, price_gel, price_usd, property_type):

        insert_query = '''
        INSERT INTO myhome (home_id, phone_number, owner_name, post_date, price_gel, price_usd, property_type)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
            phone_number=VALUES(phone_number),
            owner_name=VALUES(owner_name),
            post_date=VALUES(post_date),
            price_gel=VALUES(price_gel),
            price_usd=VALUES(price_usd),
            property_type=VALUES(property_type)
        '''

        self.cursor.execute(insert_query, (home_id, phone_number, owner_name, post_date, price_gel, price_usd, property_type))
        self.conn.commit()

    def close_connection(self):
        self.cursor.close()
        self.conn.close()




import pymysql
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='Xihac0204',
                             db='projectc',
                             cursorclass=pymysql.cursors.DictCursor)

cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS ProjectC.Dim_Stock(
    stock varchar(255),
    PRIMARY KEY (stock)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS ProjectC.Dim_Exchange(
    exchange varchar(255),
    country varchar(255),
    PRIMARY KEY (exchange)
)
''')



cursor.execute('''
CREATE TABLE IF NOT EXISTS ProjectC.fact_stock(
    id int(11) AUTO_INCREMENT,
    date datetime,
    price numeric(10,5),
    open numeric(10,5),
    high numeric(10,5),
    low numeric(10,5),
    changed numeric(10,5),
    vol numeric(10,5),
    stock varchar(255),
    exchange varchar(255),
    PRIMARY KEY (id),
    FOREIGN KEY (stock) REFERENCES Dim_Stock(stock),
    FOREIGN KEY (exchange) REFERENCES Dim_Exchange(exchange)
)
''')
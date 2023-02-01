import sqlite3

create_table = """ CREATE TABLE IF NOT EXISTS clients (
				id integer PRIMARY KEY,
				name text NOT NULL,
				date_month integer NOT NULL,
				date_year integer NOT NULL,
				comments text
				); """
add_client = """ INSERT INTO clients (
				name,
				date_month,
				date_year,
				comments
				) VALUES(?,?,?,?) """

class clientBase:

	def __init__(self):
		connection = sqlite3.connect('dataFile.db')
		cursor = connection.cursor()
		cursor.execute(create_table)
		connection.commit()
		connection.close()

	def date(self, month, year):
		self.month = month
		self.year = year
		#search db table for entries whose month & year attributes match that of those given
		print(month + year)

	def name(self, name):
		self.name = name
		# search db table for entries whose name attribute matches that of the name given
		print(name)

	def addClient(self, name, month, year, comments):
		self.name, self.month, self.year, self.comments = name, month, year, comments
		values = (name, month, year, comments)
		connection = sqlite3.connect('dataFile.db')
		cursor = connection.cursor()
		cursor.execute(add_client, values)
		connection.commit()
		connection.close()

	def returnAll(self):
		connection = sqlite3.connect('dataFile.db')
		cursor = connection.cursor()
		cursor.execute("SELECT * FROM clients")
		clients = cursor.fetchall()
		for client in clients:
			print(client)
		connection.close()

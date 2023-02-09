import sqlite3

create_table = """ CREATE TABLE IF NOT EXISTS clients (
				id integer PRIMARY KEY,
				first_name text NOT NULL,
				last_name text NOT NULL,
				date_month integer NOT NULL,
				date_year integer NOT NULL,
				comments text
				); """
add_client = """ INSERT INTO clients (
				first_name,
				last_name,
				date_month,
				date_year,
				comments
				) VALUES(?,?,?,?,?) """

class clientBase:

	def __init__(self):
		self.connection = sqlite3.connect('dataFile.db')
		self.cursor = self.connection.cursor()
		self.cursor.execute(create_table)
		self.connection.commit()
		self.connection.close()

	def date(self, month, year):
		self.month = month
		self.year = year
		#search db table for entries whose month & year attributes match that of those given
		print(month + year)

	def firstName(self, firstName):
		self.firstName = firstName
		# search db table for entries whose name attribute matches that of the name given
		print(self.firstName)

	def lastName(self, lastName):
		self.lastName = lastName
		# search db table for entries whose name attribute matches that of the name given
		print(self.lastName)

	def addDB(self, values):
		self.values = values
		self.connection = sqlite3.connect('dataFile.db')
		self.cursor = self.connection.cursor()
		self.cursor.execute(add_client, self.values)
		self.connection.commit()
		self.connection.close()

	def returnAll(self):
		self.connection = sqlite3.connect('dataFile.db')
		self.cursor = self.connection.cursor()
		self.cursor.execute("SELECT * FROM clients")
		self.clients = self.cursor.fetchall()
		# self.clientList = []
		# for i in self.clients:
		# 	self.clientList.append(i)
		self.connection.close()
		return self.clients
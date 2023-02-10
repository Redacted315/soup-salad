import sqlite3

create_clients_table = """ CREATE TABLE IF NOT EXISTS clients (
				client_id integer PRIMARY KEY,
				first_name text NOT NULL,
				last_name text NOT NULL,
				date_month integer NOT NULL,
				date_year integer NOT NULL
				); """

create_communications_table = """ CREATE TABLE IF NOT EXISTS communications (
				client_id integer,
				comments text NOT NULL,
				FOREIGN KEY(client_id) REFERENCES clients(client_id)
				); """

add_client = """ INSERT INTO clients (
				first_name,
				last_name,
				date_month,
				date_year
 				) VALUES(?,?,?,?); """

enable_keys = "PRAGMA foreign_keys=1;"

class clientBase:

	def __init__(self):
		self.connection = sqlite3.connect('main.db')
		self.cursor = self.connection.cursor()
		self.cursor.execute(enable_keys)
		self.cursor.execute(create_clients_table)
		self.cursor.execute(create_communications_table)
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

	def newClient(self, values):
		self.values = values
		self.connection = sqlite3.connect('main.db')
		self.cursor = self.connection.cursor()
		self.cursor.execute(add_client, self.values)
		self.connection.commit()
		self.connection.close()

	def newComment(self, comment):
		self.comment = comment
		self.connection = sqlite3.connect('main.db')
		self.cursor = self.connection.cursor()
		self.cursor.execute(add_client, self.comment)
		self.connection.commit()
		self.connection.close()

	def returnAll(self):
		self.connection = sqlite3.connect('main.db')
		self.cursor = self.connection.cursor()
		self.cursor.execute("SELECT * FROM clients")
		self.clientList = self.cursor.fetchall()
		self.connection.close()
		return self.clientList

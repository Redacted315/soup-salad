# example dataset
from dbinteraction import clientBase
import random

first = [
"Messiah",
"Kimora",
"Genevieve",
"Alfred",
"Bella",
"Evie",
"Roberto",
"Maximo",
"Sariah",
"Bennett",
"Lailah",
"Michael",
]
last = [
"Rowe",
"Rush",
"Crane",
"Wise",
"Finley",
"Mathews",
"Lutz",
"Luna",
"Horne",
"Hendrix",
"Salinas",
"Maddox",
]
month = random.randint(1,12)
year = 2023

db = clientBase()

for i in first:
	values = (i, last[first.index(i)], month, year, "example comments")
	db.addDB(values)
# test dbinteraction
from dbinteraction import clientBase

a = clientBase()
a.addClient("John Knobber", 7, 2022, "sussy baka")
a.addClient("John Knobber", 8, 2022, "goblin mode")
a.addClient("John Knobber", 9, 2022, "juicer")
a.addClient("John Knobber", 10, 2022, "loves rad.-lib. agi.-prop.")

a.returnAll()
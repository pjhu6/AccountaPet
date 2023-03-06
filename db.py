from os.path import isfile
from sqlite3 import connect
from consumable import Consumable

DB_PATH = "db/database.db"
BUILD_PATH = "db/build.sql"

cxn = connect(DB_PATH, check_same_thread=False)
cur = cxn.cursor()


def with_commit(func):
	def inner(*args, **kwargs):
		func(*args, **kwargs)
		commit()

	return inner


@with_commit
def build():
	if isfile(BUILD_PATH):
		scriptexec(BUILD_PATH)

# Save database
def commit():
	cxn.commit()

def close():
	cxn.close()


def field(command, *values):
	cur.execute(command, tuple(values))

	if (fetch := cur.fetchone()) is not None:
		return fetch[0]

def record(command, *values):
	cur.execute(command, tuple(values))

	return cur.fetchone()

def records(command, *values):
	cur.execute(command, tuple(values))

	return cur.fetchall()

def execute(command, *values):
	cur.execute(command, tuple(values))


def column(command, *values):
	cur.execute(command, tuple(values))

	return [item[0] for item in cur.fetchall()]

def scriptexec(path):
	with open(path, "r", encoding="utf-8") as script:
		cur.executescript(script.read())

def getpath():
	return DB_PATH

# Table specific methods
def build_consumable(c_id):
	c_data = record("SELECT c_id, c_name, cost, hunger_value, happiness_value FROM all_consumables WHERE c_id = ?", c_id)
	return Consumable(c_data[0], c_data[1], c_data[2], c_data[3], c_data[4])

def append_consumable(user_id, consumable):
	execute("INSERT INTO user_consumables (c_id, user_id) VALUES (?, ?)", consumable.id, user_id)

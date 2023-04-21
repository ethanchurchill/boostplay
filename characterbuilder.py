import sys
import os
import dndformatting
from connect import connect, disconnect
import json
import subprocess
import base64

# def createCharacter(self, val):


# def selectClass(self, val):
def isIter(value):
	try:
		_ = (e for e in value)
	except TypeError:
		return False
	return True

def formatJsonData(data):
	data = data[10:-1]
	return data


if __name__ == '__main__':
	in_val = sys.argv[1]
	userid = sys.argv[2]
	conn = connect()
	cur = conn.cursor()
	if in_val == 'new-char':
		f = open('assets/new-char-template.json')
		data = json.load(f)
		print(data)
		print(type(data))
		data_json = json.dumps(data, indent=4)
		print(type(data_json))
		cur.execute("INSERT INTO dndcharacterdata (userid, charjson) VALUES (%s, %s);",(userid, data_json,))
	elif in_val == 'retrieve':
		cur.execute("SELECT charid, charjson FROM dndcharacterdata WHERE userid = %s;",(userid,))
		data = cur.fetchall()
		print(json.dumps(data))
	elif isIter(in_val) and in_val[0:5] == "char-":
		val = in_val[5:]
		cur.execute("SELECT charjson FROM dndcharacterdata WHERE userid = %s AND charid = %s;",(userid,val,))
		data = cur.fetchone()
		print(json.dumps(data))
	else:
		char_json = json.loads(formatJsonData(in_val))
		print(char_json)
		print(char_json['name'])
		char_id = (char_json['charid'])[5:]
		cur.execute("SELECT charjson FROM dndcharacterdata WHERE userid = %s AND charid = %s;",(userid,char_id,))
		data = cur.fetchone()
		print(data[0])
		example = open('assets/new-char-template.json')
		print(json.dumps(example, indent=4))

	disconnect(conn, cur)
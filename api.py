import flask
from flask import request
from flask import jsonify
import sqlite3

app = flask.Flask(__name__)
app.config["DEBUG"] = True
con = sqlite3.connect('database.db', check_same_thread=False)

# API to book a ticket using a user’s name, phone number, and timings.
@app.route('/api/bookticket', methods=['GET'])
def insert_row():
	query_parameters = request.args
	username = query_parameters.get("username")
	phonenumber = query_parameters.get("phonenumber")
	timing = query_parameters.get("timing")

	if not (username or phonenumber or timing):
		return "<h1>Error!!</h1><p>Some parameter's missing. Please pass the username, phonenumber and timing.</p>"

	l = []
	l.append(username)
	l.append(phonenumber)
	l.append(timing)

	cursorObj = con.cursor()
	query = "INSERT INTO tickets VALUES(null,?,?,?);".format(username,phonenumber,timing)
	try:
		cursorObj.execute(query,l)
		con.commit()
		print("Inserted!")
		rowid = cursorObj.lastrowid
		print("Last row id:",rowid)
		return "<h1>Your ticket id is {}</h1><p>Thank you for the booking.</p>".format(rowid)
	except:
		print("Insert fail.")

#API to update the ticket timing
@app.route('/api/changetime', methods=['GET'])
def updateTicket():
	query_parameters = request.args
	time = query_parameters.get("timing")
	id_ = query_parameters.get("id")
	if not (id_ or timing):
		return "<h1>Error!!</h1><p>Some parameter's missing. Please pass the ticket id and new timing.</p>"
	cursorObj = con.cursor()
	try:
		cursorObj.execute("UPDATE tickets set timings=? where id=?",(time,id_))
		con.commit()
		print("update successfully done")
		return "<h1>Your ticket timing is updated to {}</h1><p>Thank you !</p>".format(time)
	except:
		print("update failed")
		return "<h1>Some error occured!</h1>"

#API to  view tickets of a particular time
@app.route('/api/showtickets', methods=['GET'])
def show_rows():
	query_parameters = request.args
	timing = query_parameters.get("timing")
	if timing :
		time = timing
		cursorObj = con.cursor()
		cursorObj.execute("SELECT * from tickets where timings=?",[time])
		rows = cursorObj.fetchall()
		results = []
		for row in rows:
			#print(,' ','username',row[1],' ','phonenumber',row[2],' ','timing',row[3])
			dic = {}
			dic["ticketid"] = row[0]
			dic["User's name"] = row[1]
			dic["Phone Number"] = row[2]
			dic["Timing"] = row[3]
			results.append(dic)
		return jsonify(results)
	else:
		return "<h1>Error!!</h1><p>Time parameter is not provided.</p>"

# API to delete a particular ticket
@app.route('/api/deleteticket', methods=['GET'])
def deleteTicket():
	query_parameters = request.args
	id_ = query_parameters.get("id")
	if not (id_ or timing):
		return "<h1>Error!!</h1><p>Some parameter's missing. Please pass the ticket id.</p>"
	cursorObj = con.cursor()
	try:
		cursorObj.execute("DELETE FROM tickets where id = ?",(id_,))
		con.commit()
		print("delete successfully done")
		return "<h1>Ticket with id {} id deleted</h1><p>Thank you !</p>".format(id_)
	except:
		print("delete failed")
		return "<h1>Some error occured!</h1>"
if __name__ == '__main__':
	app.run()
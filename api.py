import flask
from flask import request
from flask import jsonify
import sqlite3

app = flask.Flask(__name__)
app.config["DEBUG"] = True
con = sqlite3.connect('database.db', check_same_thread=False)

# API to book a ticket using a user’s name, phone number, and timings.
@app.route('/api/bookticket', methods=['GET'])
def bookTicket():
	markExpired()
	query_parameters = request.args
	username = query_parameters.get("username")
	phonenumber = query_parameters.get("phonenumber")
	timing = query_parameters.get("timing")

	if(username==None or phonenumber==None or timing==None):
		return "<h1>Error!!</h1><p>Some parameter's missing. Please pass the username, phonenumber and timing.</p>"

	current_ticket_count = getCount(timing)
	if(current_ticket_count>=20):
		return "<h1>Sorry!</h1><p>This show is full. Please book for other timing.</p>"

	l = []
	l.append(username)
	l.append(phonenumber)
	l.append(timing)

	cursorObj = con.cursor()
	query = "INSERT INTO tickets VALUES(null,?,?,?,'active');".format(username,phonenumber,timing)
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
def updateTicketTime():
	markExpired()
	query_parameters = request.args
	time = query_parameters.get("timing")
	id_ = query_parameters.get("id")
	if(id_==None or time==None):
		return "<h1>Error!!</h1><p>Some parameter's missing. Please pass the ticket id and new timing.</p>"

	current_ticket_count = getCount(time)
	if(current_ticket_count>=20):
		return "<h1>Sorry!</h1><p>This show is full. Please book for other timing.</p>"
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
def showTickets():
	markExpired()
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
			dic['Staus'] = row[4]
			results.append(dic)
		return jsonify(results)
	else:
		return "<h1>Error!!</h1><p>Time parameter is not provided.</p>"

# API to delete a particular ticket
@app.route('/api/deleteticket', methods=['GET'])
def deleteTicket():
	query_parameters = request.args
	id_ = query_parameters.get("id")
	if(id_== None):
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

 # API to view the users details based on a ticket id
@app.route('/api/showparticularticket', methods=['GET'])
def viewUser():
	markExpired()
	query_parameters = request.args
	id_ = query_parameters.get("id")
	if(id_== None):
		return "<h1>Error!!</h1><p>Some parameter's missing. Please pass the ticket id.</p>"
	cursorObj = con.cursor()
	cursorObj.execute("SELECT * from tickets where id=?",[id_])
	rows = cursorObj.fetchall()
	result = []
	if(len(rows)==0):
		return "<h1>No ticket found with id {}</h1>".format(id_)
	for row in rows:
		dic = {}
		dic["ticketid"] = row[0]
		dic["User's name"] = row[1]
		dic["Phone Number"] = row[2]
		#dic["Timing"] = row[3]
		#dic['Status'] = row[4]
		result.append(dic)
	return jsonify(result)

# Function to Mark a ticket as expired if there is a 
# diff of 8 hours between the ticket timing and current time.
def markExpired():
	cursorObj = con.cursor()
	query = "UPDATE tickets set status = 'expired' WHERE timings <= time('now','localtime','-8 hours');"
	cursorObj.execute(query)
	con.commit()

# Function to delete expired
def deleteExpired():
	cursorObj = con.cursor()
	query = "DELETE FROM tickets where status='expired';"
	cursorObj.execute(query)
	con.commit()


#Query to get the count of tickets at a particular time
def getCount(time):
	cursorObj = con.cursor()
	cursorObj.execute("SELECT count(*) from tickets where timings=?",[time])
	return cursorObj.fetchall()[0][0]

if __name__ == '__main__':
	app.run()
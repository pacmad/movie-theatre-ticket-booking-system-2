import sqlite3

from sqlite3 import Error

def sql_connection():

    try:

        con = sqlite3.connect('database.db')
        print("connection successfully connected")
        return con

    except Error:

        print(Error)


# Query to insert values to the talble
def insert_row(con):
	cursorObj = con.cursor()
	query = "INSERT INTO tickets VALUES(null,'xyz', 9897456872, '15:45')";
	try:
		cursorObj.execute(query)
		con.commit()
		print("Inserted!")
		rowid = cursorObj.lastrowid
		print("Last row id:",rowid)
		return rowid
	except:
		print("Insert fail.")

#query to  view tickets of a particular time
def show_rows(con,time):
	cursorObj = con.cursor()
	cursorObj.execute("SELECT * from tickets where timings=?",[time])
	rows = cursorObj.fetchall()
	l = []
	for row in rows:
		#print(,' ','username',row[1],' ','phonenumber',row[2],' ','timing',row[3])
		dic = {}
		dic["ticketid"] = row[0]
		dic["User's name"] = row[1]
		dic["Phone Number"] = row[2]
		dic["Timing"] = row[3]
		l.append(dic)
	return l

# Query to show all the rows of the tickets table
def showALLRows(con):
	cursorObj = con.cursor()
	cursorObj.execute("SELECT * from tickets")
	rows = cursorObj.fetchall()
	for row in rows:
		print(row)

#Query to get the count of tickets at a particular time
def getCount(con,time):
	cursorObj = con.cursor()
	cursorObj.execute("SELECT count(*) from tickets where timings=?",[time])
	return cursorObj.fetchall()[0][0]

#query to update the ticket timing
def updateTicket(con,id_,time):
	cursorObj = con.cursor()
	try:
		cursorObj.execute("UPDATE tickets set timings=? where id=?",(time,id_))
		con.commit()
		print("update successfully done")
		return True
	except:
		print("update failed")
		return False

# Query to delete a particular ticket
def deleteTicket(con,id_):
	cursorObj = con.cursor()
	try:
		cursorObj.execute("DELETE FROM tickets where id = ?",(id_,))
		con.commit()
		print("delete successfully done")
		return True
	except:
		print("delete failed")
		return False

 # query to view the users details based on a ticket id
def viewUser(con,id_):
	cursorObj = con.cursor()
	cursorObj.execute("SELECT * from tickets where id=?",[id_])
	rows = cursorObj.fetchall()
	l = []
	for row in rows:
		#print(,' ','username',row[1],' ','phonenumber',row[2],' ','timing',row[3])
		dic = {}
		dic["ticketid"] = row[0]
		dic["User's name"] = row[1]
		dic["Phone Number"] = row[2]
		dic["Timing"] = row[3]
		l.append(dic)
	return l

if __name__ == '__main__':
	con = sql_connection()
	#insert_row(con)
	#print(show_rows(con,"15:45"))
	#print(getCount(con,"15:45"))
	#updateTicket(con,5,"15:50")
	#deleteTicket(con,5)
	#showALLRows(con)
	print(viewUser(con,4))
	#print(lastRowId(con))





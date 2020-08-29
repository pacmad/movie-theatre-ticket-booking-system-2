import flask
from flask import request
from flask import jsonify
import sqlite3

app = flask.Flask(__name__)
app.config["DEBUG"] = True
con = sqlite3.connect('database.db', check_same_thread=False)

#API to  view tickets of a particular time
@app.route('/api/bookticket', methods=['GET'])
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


if __name__ == '__main__':
	app.run()
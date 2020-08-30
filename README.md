# movie-theatre-ticket-booking-system

Its a REST interface for a movie theatre ticket booking system.
```
Language - Python
Web Framework - Flask
Database - SQLLite
```

## It supports the following business cases:
- An endpoint to book a ticket using a user’s name, phone number, and timings.
- An endpoint to update a ticket timing.
- An endpoint to view all the tickets for a particular time.
- An endpoint to delete a particular ticket.
- An endpoint to view the user’s details based on the ticket id.
- Mark a ticket as expired if there is a diff of 8 hours between the ticket timing and current time.
- For a particular timing, a maximum of 20 tickets can be booked.

## Prerequisites

```
Python3
Flask
Sqllite
```

## Endpoints

1. **An endpoint to book a ticket using a user’s name, phone number, and timings.**

**Endpoint**-> http://127.0.0.1:5000/api/bookticket

*Parameters*
```
username - User's name
phonenumber - User's phonenumber
timing - time in HH:MM format

example: 
http://127.0.0.1:5000/api/bookticket?username=John&phonenumber=1234567890&timing=15:30
```

- returns the ticket ID of the booked ticket.
- cannot book if 20 tickets are already booked for that show timing.
- return error if any parameter is not passed during api call.

2. **An endpoint to update a ticket timing.**

**Endpoint**-> http://127.0.0.1:5000/api/changetime

*Parameters*
```
id - Ticket ID
timing - new time in HH:MM format

example: 
http://127.0.0.1:5000/api/changetime?id=15&timing=16:30
```

- updates the ticket timing if ticket id matches and show is not full for that timing.
- cannot update if 20 tickets are already booked for that show timing.
- return error if any parameter is not passed during api call.

3. **An endpoint to view all the tickets for a particular time.**


**Endpoint**-> http://127.0.0.1:5000/api/showtickets

*Parameters*
```
timing - time in HH:MM format

example: 
http://127.0.0.1:5000/api/showtickets?timing=16:30
```
- returns all the tickets for that particular time in JSON format.
- Each json object contains -> ticketid, User's Name, Phone Number, Timing, Status.
- return error if timing parameter is not passed during api call.

4. **An endpoint to delete a particular ticket.**


**Endpoint**-> http://127.0.0.1:5000/api/deleteticket

*Parameters*
```
id = Ticket ID

example: 
http://127.0.0.1:5000/api/deleteticket?id=10
```
- delete the ticket with given ticket ID if exists.
- return error if id parameter is not passed during api call.
- returns a delete successfull message.

5. **An endpoint to view the user’s details based on the ticket id.**


**Endpoint**-> http://127.0.0.1:5000/api/showparticularticket

*Parameters*
```
id = Ticket ID

example: 
http://127.0.0.1:5000/api/showparticularticket?id=10
```
- returns a JSON object containing the users details.
- returns error if there is no ticket with that id.
- JSON object contains -> ticket id, User's name, Phone Number.

## Database structure

SQLLITE is used as the relational database to store the data.

Table name is **tickets**.

Table structure:
- *id* integer primary key
- *username* varchar
- *phonenumber* integer
- *timings* varchar
- *status* varchar

id is auto incremented

username stores the user's name

phonenumber stores the user's phonenumber

timings stores the show time of the ticket in HH:MM format

status keeps the record if the ticket is **active** or **expired**

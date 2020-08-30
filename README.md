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

1. An endpoint to book a ticket using a user’s name, phone number, and timings.

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



## CS 3200 Final Project

### Group Members:
* Christina Long: 1:35 Group 18
* Adrian Monaghan: 3:25 Group 22
* Venkat Pamulapati: 3:25 Group 22

### Instructions for setup
1. Create a mysql schema called `python_test`
2. Import the schema from the `flaskProject3200/databse`
3. Clone the repository
4. Type `python3 -m pip install -r requirements.txt` into console
5. Copy the `configExample.py` file into a new file called `config.py` in the `flaskr/` directory
6. Fill out the appropriate fields to connect to your database
7. Run the project!

### Technical Details
* Flask for routing and server
* MySQL for database
* SQLAlchemy for interacting with database via ORM 
* Jinja and Bootstrap for front end

### Functionality
* Support all CRUD operatoins for the 4 tables
* Meets all spec requirements in P1, P2, and P3

### Write Up
In the world of flying, often, pilots use paper tables to keep track of their flights that they make. They also tend to fill in the same information in every log they make, wasting time and energy. A digital logbook, that allows storage and retrieval of all the pilot’s logs in one place would allow for a paper logbook to no longer be needed. Another issue with paper logbooks is that they can be lost or destroyed. A pilot’s logbook can be tens of thousands, if not hundreds of thousands of dollars to them, as it is their only legal record of their flights. Losing their logbook would be detrimental and a large hassle to both  them, and their career.

We built an electronic logbook, that allows for the storage and retrieval, of all a pilot’s logs throughout time. It allows for logs to be stored long term, in a relational database. We also have places for pilots to input the aircraft they fly as well as what pilot ratings they have. Allowing for the input of aircraft that they fly removes the risk of inputting a wrong value in each log entry. This allows for a pilot to easily keep track of how many hours they have flown for. This number is required for job applications as well as new licenses that a pilot may want to get. Having a logbook be digital also removes the worry of it being lost or damage. If this were to be implemented using redundant systems and backups, there would be no fear of losing your logs.

The typical user of this application is any pilot, big time, or weekend warrior, that wants to keep their logs safe, and have a backup. Professional pilots fly a lot, and therefore, spend a lot of time inputting flights into their logbook. An application that would allow you to fill out a log from your phone while on the go would be very beneficial. Pilots that fly for fun would no longer need to carry their logbook with them to and from the airport, and therefore, would have less of a chance of losing it. They could keep it in a safe place at home, where they know it would not get damaged or lost. Our users, therefore, are any pilots, professional or recreational.

Two domain objects that we implemented was the log domain object, and the aircraft domain object. The log domain object references both the users table as well as the aircrafts domain object. The aircraft domain object only references the log domain object. The aircraft table stores data about each individual aircraft. This removes any potential redundancy or inaccurate information that could come from mis inputting information about aircraft if it were stored in the logs. The aircraft table stores information such as aircraft identification, category and class of the aircraft, and the type of aircraft. The logs domain object stores all the information in the log. It stores which aircraft you flew, how many landings you made, who was flying, what conditions the flight was in, the day the flight was taken, where you flew to, as well as any notes about the flight.

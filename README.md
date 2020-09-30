# Spottr
Full stack project with Flask and PostgreSQL. 

Spottr is a web app to allow a gym's staff to track memberships, activities and trainers. The interface is designed to work cleanly on all sizes of screens.

# Running Instructions
In order to run the app, you will need to create and seed an SQL database called "spottr". From the project's root folder, in the terminal:

    psql createdb spottr
    psql -d spottr -f db/spottr.sql

You now have an empty database with the appropriate tables, but they are still empty. You can either run the app and populate it manually, or add some data using the console:

    python3 console.py

To run the app (assuming that Flask is installed on your computer):

    flask run
    
 # Brief
 
 The brief and MVP for this project:
 
 A local gym has asked you to build a piece of software to help them to manage memberships, and register members for classes.

MVP:
* The app should allow the gym to create and edit Members
* The app should allow the gym to create and edit Classes
* The app should allow the gym to book members on specific classes
* The app should show a list of all upcoming classes
* The app should show all members that are booked in for a particular class


In addition, the following extensions were implemented:
* The app allows the gym to create and edit Trainers
* The app allows entirely deleting trainers, activities, members and bookings.
* The app allows members to add a note to bookings.
* The app allows deactivation of trainers and members. Deactivated members and trainers can not be added to activities.
* The app allows activities to have a maximum capacity. Once the capacity has been reached, additional members cannot be booked into the class.

# Technologies Used

This app is an example of a full-stack project, using:
* python 3
* Flask
* HTML
* CSS
* PostgreSQL


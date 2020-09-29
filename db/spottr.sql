
DROP TABLE IF EXISTS bookings;
DROP TABLE IF EXISTS activities;
DROP TABLE IF EXISTS members;
DROP TABLE IF EXISTS trainers;



CREATE TABLE trainers(
    id SERIAL PRIMARY KEY,
    name VARCHAR (255),
    active BOOLEAN
);

CREATE TABLE members(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    active BOOLEAN
);

CREATE TABLE activities(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    date VARCHAR(255),
    time VARCHAR(255),
    trainer_id INT REFERENCES trainers(id),
    capacity INT
);

CREATE TABLE bookings(
    id SERIAL PRIMARY KEY,
    member_id INT REFERENCES members(id) ON DELETE CASCADE,
    activity_id INT REFERENCES activities(id) ON DELETE CASCADE,
    note TEXT
);


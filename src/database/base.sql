
create table ClientData(
	id integer PRIMARY KEY autoincrement,
    name varchar(50),
    surname varchar(50),
    address varchar(50),
    phone_number varchar(50)
);

create table Post(
	id integer PRIMARY KEY autoincrement,
    name varchar(50),
    power_level integer
);

create table Personal(
	id integer PRIMARY KEY autoincrement,
    name varchar(50),
    surname varchar(50),
    post_id integer,
    foreign key (post_id) references Post(id)
);

create table Users(
	id integer PRIMARY KEY autoincrement,
    login varchar(16) not null unique,
    password varchar(16) not null,
    personal_id integer,
    foreign key (personal_id) references Personal(id)
);

create table TaskStatus(
	id integer PRIMARY KEY autoincrement,
    name varchar(50)
);

create table TaskType(
	id integer PRIMARY KEY autoincrement,
    name varchar(50)
);

create table Task(
    id integer PRIMARY KEY autoincrement,
    date_start DATE,
    clientdata_id integer,
    personal_id integer,
    taskstatus_id integer,
    tasktype_id integer,
    foreign key (clientdata_id) references ClientData(id),
    foreign key (personal_id) references Personal(id),
    foreign key (taskstatus_id) references TaskStatus(id),
    foreign key (tasktype_id) references TaskType(id)
);
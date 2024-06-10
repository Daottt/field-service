insert into Post (name, power_level)
	values ("admin", "0");

insert into Personal (name, surname, post_id)
	values ("admin","", "1");

insert into Users (login, password, personal_id)
	values ("1", "1", "1");

insert into TaskStatus (name)
    values("Ожидает", "В процессе", "Выполнена")

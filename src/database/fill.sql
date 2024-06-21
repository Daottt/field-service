insert into Post (name, power_level)
	values ("admin", "0"), ("Менеджер", 1), ("Мастер", 2);

insert into Personal (fio, post_id)
	values ("admin", "1"), ("Трубин Никита Юрьевич", "3"), ("Степанов Андрей Викторович", "3");

insert into Users (login, password, personal_id)
	values ("1", "1", "1");

insert into TaskStatus (name)
    values("Ожидает"), ("В процессе"), ("Выполнена");

insert into TaskType (name)
    values("Осмотр"), ("Ремонт"), ("Замена");

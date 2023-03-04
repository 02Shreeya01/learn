create database practice;

use practice;
create table student(Student_id int, Student_name char,student_class int);
alter table student
Modify Student_name Text;
insert into student(Student_id, Student_name, Student_class) values (1, "Ravi", 3); 
insert into student(Student_id, Student_name, Student_class) values (2, "Sailu", 2); 
insert into student(Student_id, Student_name, Student_class) values (1, "praneeth", 1); 
insert into student(Student_id, Student_name, Student_class) values (3, "Sai", 3); 
insert into student(Student_id, Student_name, Student_class) values (1, "Rahul", 2); 
insert into student(Student_id, Student_name, Student_class) values (4, "Pavan", 1); 
insert into student(Student_id, Student_name, Student_class) values (1, "Nani", 3); 
insert into student(Student_id, Student_name, Student_class) values (5, "Priyanka", 2); 
insert into student(Student_id, Student_name, Student_class) values (1, "Mounika", 1); 
insert into student(Student_id, Student_name, Student_class) values (6, "Nikila", 3); 

select * from student where Student_id = 1;

select Student_id from student where Student_name like "%R"; 

update student
set Student_name = "Sridevi" where Student_id = 1 and Student_class = 1;

select Min(Student_id) from student 
where Student_Class = 3;


-- Hello Everyone


/*

Hello
Everyone

*/

create database NSTIWIndore;
show databases;

use NSTIWIndore;
show tables;

create table Students (
RollNo int primary key not null auto_increment,
sname varchar(100),
class int,
city VARCHAR(25) default "Indore",
contact int unique not null,
email varchar(100) unique not null
);



desc students;

alter table students modify contact bigint;

insert into 
students(RollNo, sname, class, city,contact,email) 
values (1001,"Yash", 10,"Ujjain",4838305848, "yash@email.com");

alter table students add aadhar varchar(12);

insert into students 
(sname,class, contact,email, aadhar) 
values ("Mohan",7,1234567890,"Mohan@email.com",123456789012);
insert into students values(1003,"Sohan",8,"Dewas",1234561212,"sohan@email.com",123456789034);

select * from students;


insert into students 
(sname,class, contact,email, aadhar) 
values ("Rohan",11,1234567891,"rohan@email.com",323456789012);

alter table students drop column aadhar;



use northwind;
select * from employee; 


select phone as "Phone Number",
firstname as "First Name" ,
lastname as  "Last Name",
title as "Job Title",
city as City from employee;

select * from employee where city = "London";
select * from product where unitprice < 10;

select * from product where unitprice between 5 and 10;

select * from employee where title like "Sales%";

select * from employee where title like "%Manager";
select * from employee where lastname like "__u%";

select * from employee order by city desc;

select * from employee;

update employee
set lastname = "Malik"
where employeeId = 9;

use northwind;
select avg(unitprice) as "Average Price" from product;
select sum(unitprice) as "Sum of Price" from product;
select productname, max(unitprice) from product;
select productname, min(unitprice) from product;
select count(productid) from product;
select supplierid,count(productname) from product group by supplierid;
select * from product;

use sakila;
select * from film;
select rental_duration, count(film_id) from film 
group by rental_duration 
having rental_duration >= 5 
order by rental_duration;

select round(4.39827492837492387492374) as "Calculation";
select ceil(4.39827492837492387492374) as "Calculation";
select floor(4.39827492837492387492374) as "Calculation";

select abs(-55.555);

use northwind;
select upper(concat(firstname,' ',lastname)) as FullName from employee;



use	RevStudDb 
begin transaction;

insert into dbo.student values(101,'AAA','QWERTY','BLR',6524871);
insert into dbo.student values(102 ,'BBB','SWETHA','HYD',798871);

select * from student 

save transaction level1;

insert into dbo.student(rollno , sname , pin)
values(103,'CCC',600021);
insert into dbo.student(sname, pin, rollno)
values('DDD',3456789, 104);

save transaction level2;

update student set addr='SWEXYHK' where rollno =103;

rollback transaction level2;

COMMIT TRANSACTION 

update student set city='HYD' where rollno=102;
update student set city ='BLR'where rollno =103;

delete from student where rollno =104;
truncate table student;


create database RevCompanyDb

use RevCompanyDb

create table dept(deptno smallint, dname varchar(3) not null, 
constraint pk_deptno primary key(deptno));

create table emp(empno smallint, ename varchar(30) not null, 
mgr smallint ,
sal numeric(10,2),
comm numeric(7,2),
deptno smallint,
constraint pk_empno primary key(empno),
constraint fk_deptno foreign key(deptno) references dept(deptno));

insert into dept values(10,'IT')
insert into dept values(20,'HR')
insert into dept values(30,'SAL')
insert into dept values(40,'MKT')
insert into dept values(50,'OPS')

select * from dept

INSERT INTO emp (empno, ename, mgr, sal, comm, deptno) VALUES
(1001, 'Alice', NULL, 60000.00, NULL, 10),  
(1002, 'Bob', 1001, 75000.00, NULL, 20),   
(1003, 'Charlie', 1002, 50000.00, 500.00, 30), 
(1004, 'Diana', 1003, 52000.00, 300.00, 30),   
(1005, 'Ethan', 1002, 58000.00, NULL, 40), 
(1006, 'Fiona', 1005, 62000.00, NULL, 50);  

select * from emp

select empno as 'Emp Num', ename as 'Name'
from emp;

select empno as 'Emp Num', ename as 'Name'
from emp
where empno!= 1004


select empno as "Emp Num", ename as "Name"
from emp
where empno not in (1002,1003,1005);

select empno as 'Emp Num', ename as 'Name'
from emp
where sal between 40000 and 55000;

select empno as 'Emp Num', ename as 'Name'
from emp
where ename = 'bob' 

select empno as 'Emp Num', ename as 'Name'
from emp
where ename like '__a%';

select empno as 'Emp Num', ename as 'Name'
from emp
where ename not in('alice','fiona');

select empno as 'Emp Num', ename as 'Name'
from emp
where empno= 1004 or ename like '%a%';

select empno as 'Emp Num', ename as 'Name'
from emp
where empno!= 1003;

select empno as 'Emp Num', ename as 'Name', sal as 'Salary', comm as 'Commision'
from emp
where sal > 50000
order by comm,sal desc;

select count(empno) as 'No of Emp', sum(sal) as 'Total', avg(comm) as 'Avg Comm',
min(sal) as 'Least sal', max(sal) as 'Top earner'
from emp
where sal > 50000 ;


select * from emp 

select empno as 'Emp Num', ename as 'Name', sal as 'Salary'
from emp
order by deptno , empno, ename, sal

select deptno as 'Department', sum(sal) as 'Total Salary'
from emp
group by deptno
having sum(sal)>100000;

select deptno as 'Department', sum(sal) as 'Total Salary'
from emp
where deptno in(10,30,50)
group by deptno
having sum(sal)>=62000
order by sum(sal);

insert into dept values(60,'QC')
insert into dept values(70,'CC')

INSERT INTO emp (empno, ename, mgr, sal, comm, deptno) VALUES
(1007,'AAA',1002,60000,NUll,Null),
(1008,'BB',1001, 75000.00, NULL,Null),
(1009,'C',1002, 50000.00, 500.00,Null)

select e.ename, d.dname
from emp e inner join dept d
on d.deptno= e.deptno;

select e.ename, d.dname
from emp e LEFT OUTER join dept d
on d.deptno= e.deptno;

select e.ename, d.dname
from emp e RIGHT OUTER join dept d
on d.deptno= e.deptno;

select e.ename, d.dname
from emp e FULL OUTER join dept d
on d.deptno= e.deptno;








select deptno as 'Department', sum(sal) as 'Total Salary'
from emp
where deptno in (10,30,50)
group by deptno;




















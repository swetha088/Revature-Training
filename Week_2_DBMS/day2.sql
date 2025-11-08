
use RevCompanyDb

select * from emp;

select e.ename as 'Employee' , m.ename as 'Manager'
from emp e join emp m
on e.mgr=m.empno

select*
from emp e cross join dept d

select * from dept

select ename
from emp
where deptno= (select deptno
from dept
where dname ='qc')

select ename from emp where sal> (select avg(sal) from emp)

SELECT ename, Deptno,Sal FROM Emp E
WHERE Sal > (SELECT AVG(Sal) FROM Emp WHERE Deptno =E.Deptno);



select deptno,avgsal from
(select deptno,avg(sal) as avgsal
from emp 
group by deptno) 
as Details;


SELECT Deptno,AvgSalary
FROM(
     SELECT deptno, AVG(Sal) AS AvgSalary
     FROM Emp
     GROUP BY Deptno AS DeptStats);

select * from emp;

create view vemp as select empno,ename from emp where deptno in (10,20,30);

select * from vemp

insert into emp (empno, ename, deptno) values (1110,'XX',20)
insert into vemp values (1111,'YY')

UPDATE vemp set empno = 10000 where empno =1111

UPDATE vemp set ename = 'Lucky'  where empno =1111

delete from vemp where empno=1111
drop view vemp

create nonclustered index ideptno on emp(deptno)
drop index emp.ideptno 

create or alter procedure sp_empdata
    @empno int , @ename varchar(20) , @sal numeric(10,2),@deptno int
as
begin
    begin transaction
      insert into emp (empno,ename,sal,deptno)
      values(@empno,@ename,@sal,@deptno)
      commit 
      select * from emp
    end
  exec sp_empdata 1012,'lakshman',20000,20

create or alter procedure sp_empdata
    @empno int , @ename varchar(20) , @sal numeric(10,2),@deptno int
as
begin
    begin transaction
      insert into emp (empno,ename,sal,deptno)
      values(@empno,@ename,@sal,@deptno)
      update emp set comm = sal * 0.1 where empno = @empno
      commit 
      select * from emp
      return 1
end

declare @status int
exec @status = sp_empdata 1015,'Sree',1000, 20
print @status


create or alter function dbo.EmpInsertion(@empno int , @ename varchar)
returns varchar(20)
as
begin
    return CAST(@empno AS VARCHAR) + '-' + @ename


select dbo.EmpInsertion(2000, 'vri') response 


create or alter function AvgSal()
returns table
as
return 
     select deptno, avg(sal) as avgsal from emp group by deptno

select  * from AvgSal()

CREATE TRIGGER trg_AfterInsertEmp
ON emp
AFTER INSERT
AS
BEGIN
    PRINT 'New employee record inserted into emp table.'
END

insert into emp (empno,ename) values (1121,'minos')












--add depto
CREATE OR REPLACE PROCEDURE Add_Depto(
    p_department_number IN NUMBER,
    p_department_name IN VARCHAR2,
    p_location IN VARCHAR2
) AS
BEGIN
    INSERT INTO dept (deptno, dname, loc)
    VALUES (p_department_number, p_department_name, p_location);
    COMMIT;
END Add_Depto;
/

--update depto
CREATE OR REPLACE PROCEDURE Update_Depto(
    p_department_id IN NUMBER,
    p_name IN VARCHAR2,
    p_location IN VARCHAR2
) AS
BEGIN
    UPDATE dept
    SET dname = p_name, loc = p_location
    WHERE deptno = p_department_id;
    COMMIT;
END Update_Depto;
/

-- delete_depto
CREATE OR REPLACE PROCEDURE Delete_Depto(
    p_department_id IN NUMBER
) AS
BEGIN
    DELETE FROM dept WHERE deptno = p_department_id;
    COMMIT;
END Delete_Depto;
/


-- add employee
CREATE OR REPLACE PROCEDURE Add_Emp(
    emp_id NUMBER,
    emp_name VARCHAR2,
    emp_job VARCHAR2,
    emp_manager NUMBER,
    emp_hiredate DATE,
    emp_salary NUMBER,
    emp_commision NUMBER,
    emp_deptno NUMBER
) AS
BEGIN
    INSERT INTO emp (empno,ename,emp.job,mgr,hiredate,sal,comm,deptno)
    VALUES (emp_id,emp_name,emp_job,emp_manager,emp_hiredate,emp_salary,emp_commision,emp_deptno);
    COMMIT;
END Add_Emp;
/

-- delete employee
CREATE OR REPLACE PROCEDURE Delete_Emp(
    p_employee_id IN NUMBER
) AS
BEGIN
    DELETE FROM emp WHERE empno = p_employee_id;
    --COMMIT;
END Delete_Emp;
/

--update emp
CREATE OR REPLACE PROCEDURE Update_Emp(
        emp_id NUMBER,
        emp_name VARCHAR2,
        emp_job VARCHAR2,
        emp_manager NUMBER,
        emp_hiredate DATE,
        emp_salary NUMBER,
        emp_commision NUMBER,
        emp_deptno NUMBER
) AS
BEGIN
    UPDATE emp
    SET ename = emp_name, emp.job = emp_job, mgr = emp_manager, hiredate = emp_hiredate, sal = emp_salary, comm = emp_commision, deptno = emp_deptno
    WHERE empno = emp_id;
    COMMIT;
END Update_Emp;
/

--noEmp_depto
CREATE OR REPLACE FUNCTION NoEmp_Depto(
    p_department_id IN NUMBER
) RETURN NUMBER 
AS
    v_count NUMBER;
BEGIN
    SELECT COUNT(*) INTO v_count FROM emp WHERE deptno = p_department_id;
    RETURN v_count;
END NoEmp_Depto;
/





declare
begin
    --Add_Emp(7777,'Gru','villian',7839,sysdate,1000,null,20);
    --Delete_Emp(7777);
    --Update_Emp(7777,'Gru','villian',7839,null,1000,null,20); 
    dbms_output.put_line(NoEmp_Depto(10));
end;
/

set serveroutput on;
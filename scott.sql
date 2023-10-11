--add depto
CREATE OR REPLACE PROCEDURE Add_Depto(
    p_department_number IN NUMBER,
    p_department_name IN VARCHAR2,
    p_location IN VARCHAR2
) IS
    pk_exception EXCEPTION;
    null_exception EXCEPTION;
    aux NUMBER;

BEGIN
    IF p_department_number IS NULL OR p_department_name IS NULL OR p_location IS NULL THEN
        raise null_exception; 
    END IF;

    select count(*) into aux from dept where deptno = p_department_number;
    IF aux > 0 then
        raise pk_exception;
    end if; 


    INSERT INTO dept (deptno, dname, loc)
    VALUES (p_department_number, p_department_name, p_location);
    COMMIT;

EXCEPTION
    WHEN pk_exception then
        raise_application_error(-20200,'Error: Id repetido.');
    WHEN null_exception THEN -- Manejo de valores nulos
        raise_application_error(-20201, 'Error: Valores nulos no permitidos.');
    WHEN OTHERS then
        raise_application_error(-20026,'Error: Error desconocido');
END Add_Depto;
/

--update depto
CREATE OR REPLACE PROCEDURE Update_Depto(
    p_department_id IN NUMBER,
    p_name IN VARCHAR2,
    p_location IN VARCHAR2
) AS
    null_exception EXCEPTION;
    error_depto EXCEPTION;
    aux NUMBER;
BEGIN

    select count(*) into aux from dept where deptno = p_department_id;
    IF aux = 0 then
        raise error_depto;
    end if; 

    IF p_name IS NULL OR p_location IS NULL THEN
        raise null_exception; 
    END IF;

    UPDATE dept
    SET dname = p_name, loc = p_location
    WHERE deptno = p_department_id;
    COMMIT;

EXCEPTION
    WHEN error_depto THEN 
        raise_application_error(-20300,'Error: Departamento Inexistente');
    WHEN null_exception THEN -- Manejo de valores nulos
        raise_application_error(-20201, 'Error: Valores nulos no permitidos.');
    WHEN OTHERS then
        raise_application_error(-20026,'Error: Error desconocido');

END Update_Depto;
/



-- delete_depto
CREATE OR REPLACE PROCEDURE Delete_Depto(
    p_department_id IN NUMBER
) AS
    error_depto EXCEPTION;
    aux NUMBER;
BEGIN

    select count(*) into aux from dept where deptno = p_department_id;
    IF aux = 0 then
        raise error_depto;
    end if; 

    DELETE FROM dept WHERE deptno = p_department_id;
    COMMIT;
EXCEPTION
    WHEN error_depto THEN 
        raise_application_error(-20300,'Error: Departamento Inexistente');
    WHEN OTHERS then
        raise_application_error(-20026,'Error: Error desconocido');

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

    pk_exception EXCEPTION;
    null_exception EXCEPTION;
    aux NUMBER;

BEGIN

    select count(*) into aux from emp where empno = emp_id;
    IF aux > 0 then
        raise pk_exception;
    end if;

    IF emp_name IS NULL OR emp_job IS NULL OR emp_hiredate IS NULL OR emp_salary IS NULL OR emp_deptno IS NULL THEN
        raise null_exception; 
    END IF;
 
    INSERT INTO emp (empno,ename,emp.job,mgr,hiredate,sal,comm,deptno)
    VALUES (emp_id,emp_name,emp_job,emp_manager,emp_hiredate,emp_salary,emp_commision,emp_deptno);
    COMMIT;

    EXCEPTION
    WHEN pk_exception THEN 
        raise_application_error(-20200,'Error: Id Repetido');
    WHEN null_exception THEN -- Manejo de valores nulos
        raise_application_error(-20201, 'Error: Valores nulos no permitidos.');
    WHEN OTHERS then
        raise_application_error(-20026,'Error: Error desconocido');

END Add_Emp;
/

-- delete employee
CREATE OR REPLACE PROCEDURE Delete_Emp(
    p_employee_id IN NUMBER
) AS
    error_depto EXCEPTION;
    aux NUMBER;
BEGIN

    select count(*) into aux from emp where empno = p_employee_id;
    IF aux = 0 then
        raise error_depto;
    end if; 

    DELETE FROM emp WHERE empno = p_employee_id;
    --COMMIT;

EXCEPTION
    WHEN error_depto THEN 
        raise_application_error(-20300,'Error: Departamento Inexistente');
    WHEN OTHERS then
        raise_application_error(-20026,'Error: Error desconocido');



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
    null_exception EXCEPTION;
    error_depto EXCEPTION;
    aux NUMBER;
BEGIN

    select count(*) into aux from emp where empno = emp_id;
    IF aux = 0 then
        raise error_depto;
    end if; 

    IF emp_name IS NULL OR emp_job IS NULL OR emp_hiredate IS NULL OR emp_salary IS NULL OR emp_deptno IS NULL THEN
        raise null_exception; 
    END IF;

    UPDATE emp
    SET ename = emp_name, emp.job = emp_job, mgr = emp_manager, hiredate = emp_hiredate, sal = emp_salary, comm = emp_commision, deptno = emp_deptno
    WHERE empno = emp_id;
    COMMIT;

EXCEPTION
    WHEN error_depto THEN 
        raise_application_error(-20300,'Error: Departamento Inexistente');
    WHEN null_exception THEN -- Manejo de valores nulos
        raise_application_error(-20201, 'Error: Valores nulos no permitidos.');
    WHEN OTHERS then
        raise_application_error(-20026,'Error: Error desconocido');

END Update_Emp;
/

--noEmp_depto
CREATE OR REPLACE FUNCTION NoEmp_Depto(
    p_department_id IN NUMBER
) RETURN NUMBER 
AS
    error_depto EXCEPTION;
    v_count NUMBER;
BEGIN
    SELECT COUNT(*) INTO v_count FROM emp WHERE deptno = p_department_id;

    IF v_count = 0 then
        raise error_depto;
    end if;
    RETURN v_count;

EXCEPTION
    WHEN error_depto THEN 
        raise_application_error(-20300,'Error: Departamento Inexistente');
    WHEN OTHERS then
        raise_application_error(-20026,'Error: Error desconocido');


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
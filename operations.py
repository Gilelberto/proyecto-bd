def add_depto(cursor):
    depto_no = input('Ingrese el número de departamento: ')
    depto_name = input('Ingrese el nombre del departamento: ')
    location = input('Ingrese la ubicación del departamento; ')
    params = (depto_no,depto_name,location)
    cursor.callproc("Add_depto",params)

def update_depto(cursor):
    depto_no = input('Ingrese el número de departamento: ')
    depto_name = input('Ingrese el nombre del departamento: ')
    location = input('Ingrese la ubicación del departamento: ')
    params = (depto_no,depto_name,location)
    cursor.callproc("Update_Depto",params)

def delete_depto(cursor):
    depto_no = input('Ingrese el número de departamento: ')
    params = (depto_no)
    cursor.callproc("Delete_Depto",params)
    pass

def add_emp(cursor):
    emp_id = input('Ingrese el id del empleado a agregar: '), #puede ser autoincremental
    emp_name = input('Ingrese el nombre del empleado: ')
    emp_job = input('Ingrese el puesto del empleado: ')
    emp_manager = input('Ingrese el id del manager: ') 
    emp_hiredate = input('Ingrese la fecha de contratación: ') #mejor manejarlo en una función
    emp_salary = input('Ingrese el salario del empleado: ')
    emp_commision = input('Ingrese la comisión del empleado (pulse enter si no tiene): ')
    emp_deptno = input('Ingrese el departamento al cual pertenece el empleado: ')
    params = (emp_id,emp_name,emp_job,emp_manager,emp_hiredate,emp_salary,emp_commision,emp_deptno)
    cursor.callproc("Add_Emp",params)

def delete_emp(cursor):
    empno = input('Ingrese el id del empleado: ')
    params = (empno)
    cursor.callproc("Delete_Emp",params)

def update_emp(cursor):
    emp_id = input('Ingrese el id del empleado a agregar: '), #puede ser autoincremental
    emp_name = input('Ingrese el nombre del empleado: ')
    emp_job = input('Ingrese el puesto del empleado: ')
    emp_manager = input('Ingrese el id del manager: ') 
    emp_hiredate = input('Ingrese la fecha de contratación: ') #mejor manejarlo en una función
    emp_salary = input('Ingrese el salario del empleado: ')
    emp_commision = input('Ingrese la comisión del empleado (pulse enter si no tiene): ')
    emp_deptno = input('Ingrese el departamento al cual pertenece el empleado: ')
    params = (emp_id,emp_name,emp_job,emp_manager,emp_hiredate,emp_salary,emp_commision,emp_deptno)
    cursor.callproc("Update_Emp",params)

def noEmp_depto(cursor): #checar esta parte porque es una función no un proceso
    depto_no = input('Ingrese el número del departamento')
    params = (depto_no)
    cursor.callproc("NoEmp_Depto",params)
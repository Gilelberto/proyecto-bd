import oracledb

def add_depto(cursor):
    try: 
        depto_no = input('Ingrese el número de departamento: ')
        depto_name = input('Ingrese el nombre del departamento: ')
        location = input('Ingrese la ubicación del departamento; ')
        params = (depto_no,depto_name,location)
        cursor.callproc("Add_depto",params)
    except oracledb.DatabaseError as e:
        error, = e.args
        if error.code == 20200:
            print("Error: Id repetido.")
        elif error.code == 20201:
            print("Error: Valores nulos no permitidos.")
        elif error.code == 20026:
            print("Error: Error desconocido.")
        else:
            print("Error de base de datos:", e)
    

def update_depto(cursor):
    try:
        depto_no = input('Ingrese el número de departamento: ')
        depto_name = input('Ingrese el nombre del departamento: ')
        location = input('Ingrese la ubicación del departamento: ')
        params = (depto_no,depto_name,location)
        cursor.callproc("Update_Depto",params)
    except oracledb.DatabaseError as e:
        error, = e.args
        if error.code == 20300:
            print("Error: Departamento inexistente")
        elif error.code == 20201:
            print("Error: Valores nulos no permitidos.")
        elif error.code == 20026:
            print("Error: Error desconocido.")
        else:
            print("Error de base de datos:", e)
    

def delete_depto(cursor):
    try:
        depto_no = input('Ingrese el número de departamento: ')
        params = (depto_no,)
        cursor.callproc("Delete_Depto",params)
    except oracledb.DatabaseError as e:
        error, = e.args
        if error.code == 20300:
            print("Error: Departamento inexistente")
        elif error.code == 20026:
            print("Error: Error desconocido.")
        else:
            print("Error de base de datos:", e)


def add_emp(cursor):
    try:
        emp_id = input('Ingrese el id del empleado a agregar: ')#puede ser autoincremental
        emp_name = input('Ingrese el nombre del empleado: ')
        emp_job = input('Ingrese el puesto del empleado: ')
        emp_manager = input('Ingrese el id del manager: ') 
        emp_hiredate = input('Ingrese la fecha de contratación: ') #mejor manejarlo en una función
        emp_salary = input('Ingrese el salario del empleado: ')
        emp_commision = input('Ingrese la comisión del empleado (pulse enter si no tiene): ')
        emp_deptno = input('Ingrese el departamento al cual pertenece el empleado: ')
        params = (emp_id,emp_name,emp_job,emp_manager,emp_hiredate,emp_salary,emp_commision,emp_deptno)
        cursor.callproc("Add_Emp",params)
    except oracledb.DatabaseError as e:
        error, = e.args
        if error.code == 20200:
            print("Error: Id repetido.")
        elif error.code == 20201:
            print("Error: Valores nulos no permitidos.")
        elif error.code == 20026:
            print("Error: Error desconocido.")
        else:
            print("Error de base de datos:", e)

def delete_emp(cursor):
    try:
        empno = input('Ingrese el id del empleado: ')
        params = (empno,)
        cursor.callproc("Delete_Emp",params)
    except oracledb.DatabaseError as e:
        error, = e.args
        if error.code == 20300:
            print("Error: Empleado inexistente")
        elif error.code == 20026:
            print("Error: Error desconocido.")
        else:
            print("Error de base de datos:", e)
    

def update_emp(cursor):
    try:
        emp_id = input('Ingrese el id del empleado a agregar: ') #puede ser autoincremental
        emp_name = input('Ingrese el nombre del empleado: ')
        emp_job = input('Ingrese el puesto del empleado: ')
        emp_manager = input('Ingrese el id del manager: ') 
        emp_hiredate = input('Ingrese la fecha de contratación: ') #mejor manejarlo en una función
        emp_salary = input('Ingrese el salario del empleado: ')
        emp_commision = input('Ingrese la comisión del empleado (pulse enter si no tiene): ')
        emp_deptno = input('Ingrese el departamento al cual pertenece el empleado: ')
        params = (emp_id,emp_name,emp_job,emp_manager,emp_hiredate,emp_salary,emp_commision,emp_deptno)
        cursor.callproc("Update_Emp",params)
    except oracledb.DatabaseError as e:
        error, = e.args
        if error.code == 20300:
            print("Error: Empleado inexistente")
        elif error.code == 20201:
            print("Error: Valores nulos no permitidos.")
        elif error.code == 20026:
            print("Error: Error desconocido.")
        else:
            print("Error de base de datos:", e)
    
    

def noEmp_depto(cursor): 
    try:
        depto_no = input('Ingrese el número del departamento:')
        params = [depto_no]
        result = cursor.callfunc("NoEmp_Depto",int,params)
        if result > 0:
            print('*****El departamento si tiene empleados asignados ' + ' Cantidad:'+ str(result) + '******')
        else:
            print('****El departamento no tiene empleados asignados****')
    except oracledb.DatabaseError as e:
        error, = e.args
        if error.code == 20300:
            print("Error: Departamento inexistente")
        elif error.code == 20026:
            print("Error: Error desconocido.")
    
    

    
    
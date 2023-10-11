import oracledb

# def add_depto(cursor, depto_no, depto_name, location):
#     try: 
#         params = (depto_no, depto_name, location)
#         cursor.callproc("Add_Depto", params)
#     except oracledb.DatabaseError as e:
#         error, = e.args
#         if error.code == 20200:
#             print("Error: Id repetido.")
#         elif error.code == 20201:
#             print("Error: Valores nulos no permitidos.")
#         elif error.code == 20026:
#             print("Error: Error desconocido.")
#         else:
#             print("Error de base de datos:", e)


def add_depto(cursor, depto_no, depto_name, location):
    try:
        params = (depto_no, depto_name, location)
        cursor.callproc("Add_Depto", params)
    except oracledb.DatabaseError as e:
        error, = e.args
        if error.code == 20200:
            raise ValueError("Error: Id repetido.")
        elif error.code == 20201:
            raise ValueError("Error: Valores nulos no permitidos.")
        elif error.code == 20026:
            raise ValueError("Error: Error desconocido.")



def update_depto(cursor,depto_no,depto_name,location):
    try:
        params = (depto_no,depto_name,location)

        cursor.callproc("Update_Depto",params)
    except oracledb.DatabaseError as e:
        error, = e.args
        if error.code == 20300:
            raise ValueError("Error: Departamento inexistente")
        elif error.code == 20201:
            raise ValueError("Error: Valores nulos no permitidos.")
        elif error.code == 20026:
            raise ValueError("Error: Error desconocido.")
        else:
            raise ValueError("Error de base de datos:", e)
    

def delete_depto(cursor,depto_no):
    try:
        params = (depto_no,)
        cursor.callproc("Delete_Depto",params)
    except oracledb.DatabaseError as e:
        error, = e.args
        if error.code == 20300:
            raise ValueError("Error: Departamento inexistente")
        elif error.code == 20026:
            raise ValueError("Error: Error desconocido.")
        else:
            raise ValueError("Error de base de datos:", e)


def add_emp(cursor,emp_id,emp_name,emp_job,emp_manager,emp_hiredate,emp_salary,emp_commision,emp_deptno):
    try:
        params = (emp_id,emp_name,emp_job,emp_manager,emp_hiredate,emp_salary,emp_commision,emp_deptno)
        cursor.callproc("Add_Emp",params)
    except oracledb.DatabaseError as e:
        error, = e.args
        if error.code == 20200:
            raise ValueError("Error: Id repetido.")
        elif error.code == 20201:
            raise ValueError("Error: Valores nulos no permitidos.")
        elif error.code == 20026:
            raise ValueError("Error: Error desconocido.")
        else:
            raise ValueError("Error de base de datos:", e)

def delete_emp(cursor,empno):
    try:
        params = (empno,)
        cursor.callproc("Delete_Emp",params)
    except oracledb.DatabaseError as e:
        error, = e.args
        if error.code == 20300:
            raise ValueError("Error: Empleado inexistente")
        elif error.code == 20026:
            raise ValueError("Error: Error desconocido.")
        else:
            raise ValueError("Error de base de datos:", e)
    

def update_emp(cursor,emp_id,emp_name,emp_job,emp_manager,emp_hiredate,emp_salary,emp_commision,emp_deptno):
    try:
        params = (emp_id,emp_name,emp_job,emp_manager,emp_hiredate,emp_salary,emp_commision,emp_deptno)
        cursor.callproc("Update_Emp",params)
    except oracledb.DatabaseError as e:
        error, = e.args
        if error.code == 20300:
            raise ValueError("Error: Empleado inexistente")
        elif error.code == 20201:
            raise ValueError("Error: Valores nulos no permitidos.")
        elif error.code == 20026:
            raise ValueError("Error: Error desconocido.")
        else:
            raise ValueError("Error de base de datos:", e)
    
    

def noEmp_depto(cursor,depto_no): 
    try:
        params = [depto_no]
        result = cursor.callfunc("NoEmp_Depto",int,params)
        if result > 0:
            return '*****El departamento si tiene empleados asignados ' + ' Cantidad:'+ str(result) + '******'
        else:
            return '****El departamento no tiene empleados asignados****'
    except oracledb.DatabaseError as e:
        error, = e.args
        if error.code == 20300:
            raise ValueError("Error: Departamento inexistente")
        elif error.code == 20400:
            raise ValueError("Error: El departamento no tiene ningun empleado asociado")
        elif error.code == 20026:
            raise ValueError("Error: Error desconocido.")
        else:
            raise ValueError("Error de base de datos:", e)
    

    
    
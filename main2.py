import tkinter as tk
from tkinter import ttk
import oracledb
import operations as op

# Conectar a la base de datos Oracle
def connect_to_oracle():
    username = 'SCOTT'
    password = 'scott'
    dsn = 'localhost:1521/xepdb1'

    try:
        connection = oracledb.connect(user=username, password=password, dsn=dsn)
        return connection
    except oracledb.DatabaseError as e:
        print("Error de Oracle:", e)

# Función para agregar un departamento
def add_department():
    # Ventana emergente para agregar departamento
    add_department_window = tk.Toplevel(root)
    add_department_window.title("Agregar Departamento")

    department_number_label = tk.Label(add_department_window, text="Número de Departamento:")
    department_number_entry = tk.Entry(add_department_window)
    department_name_label = tk.Label(add_department_window, text="Nombre del Departamento:")
    department_name_entry = tk.Entry(add_department_window)
    department_location_label = tk.Label(add_department_window, text="Ubicación del Departamento:")
    department_location_entry = tk.Entry(add_department_window)

    result_label = tk.Label(add_department_window, text="", fg="red")  # Etiqueta para mostrar errores

    def submit():
        result_label.config(text="")  # Limpia el mensaje de error antes de intentar agregar un departamento

        # Obtener los datos del usuario desde la ventana emergente
        number = department_number_entry.get()
        name = department_name_entry.get()
        location = department_location_entry.get()

        # Llama a la función de operations.py para agregar un departamento
        
        # if connection:
        #     cursor = connection.cursor()
        #     try:
        #         op.add_depto(cursor, number, name, location)
        #         connection.commit()
        #         result_label.config(text="Departamento agregado exitosamente")
        #     except oracledb.DatabaseError as e:
        #         result_label.config(text="Error: " + str(e))
        #     cursor.close()
        #     connection.close()
        connection = connect_to_oracle()
        if connection:
            cursor = connection.cursor()
            try:
                op.add_depto(cursor, number, name, location)
                connection.commit()
                result_label.config(text="Departamento agregado exitosamente",fg="green")
            except ValueError as e:
                result_label.config(text=str(e),fg="red")
            except oracledb.DatabaseError as e:
                result_label.config(text="Error inesperado: " + str(e),fg="red")
            finally:
                cursor.close()
                connection.close()



    submit_button = tk.Button(add_department_window, text="Agregar", command=submit)
    department_number_label.pack()
    department_number_entry.pack()
    department_name_label.pack()
    department_name_entry.pack()
    department_location_label.pack()
    department_location_entry.pack()
    result_label.pack()  # Agrega el widget de etiqueta para mostrar errores
    submit_button.pack()
############################################################################################################################

# Función para actualizar un departamento
def update_department():
    # Ventana emergente para agregar departamento
    update_department_window = tk.Toplevel(root)
    update_department_window.title("Actualizar Departamento")

    department_number_label = tk.Label(update_department_window, text="Número de Departamento:")
    department_number_entry = tk.Entry(update_department_window)
    department_name_label = tk.Label(update_department_window, text="Nombre del Departamento:")
    department_name_entry = tk.Entry(update_department_window)
    department_location_label = tk.Label(update_department_window, text="Ubicación del Departamento:")
    department_location_entry = tk.Entry(update_department_window)

    result_label = tk.Label(update_department_window, text="", fg="red")  # Etiqueta para mostrar errores

    def submit():
        result_label.config(text="")  # Limpia el mensaje de error antes de intentar agregar un departamento

        # Obtener los datos del usuario desde la ventana emergente
        number = department_number_entry.get()
        name = department_name_entry.get()
        location = department_location_entry.get()

        connection = connect_to_oracle()
        if connection:
            cursor = connection.cursor()
            try:
                op.update_depto(cursor, number, name, location)
                connection.commit()
                result_label.config(text="Departamento actualizado exitosamente",fg="green")
            except ValueError as e:
                result_label.config(text=str(e),fg="red")
            except oracledb.DatabaseError as e:
                result_label.config(text="Error inesperado: " + str(e),fg="red")
            finally:
                cursor.close()
                connection.close()



    submit_button = tk.Button(update_department_window, text="Actualizar", command=submit)
    department_number_label.pack()
    department_number_entry.pack()
    department_name_label.pack()
    department_name_entry.pack()
    department_location_label.pack()
    department_location_entry.pack()
    result_label.pack()  # Agrega el widget de etiqueta para mostrar errores
    submit_button.pack()


#############################################################################################################
# Función para eliminar un departamento
def delete_department():
    # Ventana emergente para agregar departamento
    delete_department_window = tk.Toplevel(root)
    delete_department_window.title("Eliminar Departamento")

    department_number_label = tk.Label(delete_department_window, text="Número de Departamento:")
    department_number_entry = tk.Entry(delete_department_window)


    result_label = tk.Label(delete_department_window, text="", fg="red")  # Etiqueta para mostrar errores

    def submit():
        result_label.config(text="")  # Limpia el mensaje de error antes de intentar agregar un departamento

        # Obtener los datos del usuario desde la ventana emergente
        number = department_number_entry.get()

        connection = connect_to_oracle()
        if connection:
            cursor = connection.cursor()
            try:
                op.delete_depto(cursor, number)
                connection.commit()
                result_label.config(text="Departamento Eliminado exitosamente",fg="green")
            except ValueError as e:
                result_label.config(text=str(e),fg="red")
            except oracledb.DatabaseError as e:
                result_label.config(text="Error inesperado: " + str(e),fg="red")
            finally:
                cursor.close()
                connection.close()



    submit_button = tk.Button(delete_department_window, text="Eliminar", command=submit)
    department_number_label.pack()
    department_number_entry.pack()
    result_label.pack()  # Agrega el widget de etiqueta para mostrar errores
    submit_button.pack()


######################################################################################################3

# Función para agregar un empleado 
def add_employee():
    # Ventana emergente para agregar departamento
    add_employee_window = tk.Toplevel(root)
    add_employee_window.title("Agregar Empleado")

    employee_emp_id_label = tk.Label(add_employee_window, text="id del empleado a agregar:")
    employee_emp_id_entry = tk.Entry(add_employee_window)
    employee_name_label = tk.Label(add_employee_window, text="Nombre del empleado:")
    employee_name_entry = tk.Entry(add_employee_window)
    employee_job_label = tk.Label(add_employee_window, text="Puesto del empleado:")
    employee_job_entry = tk.Entry(add_employee_window)
    employee_manager_label = tk.Label(add_employee_window, text="id del manager:")
    employee_manager_entry = tk.Entry(add_employee_window)
    employee_hiredate_label = tk.Label(add_employee_window, text="fecha de contratación: dd/mm/aaaa")
    employee_hiredate_entry = tk.Entry(add_employee_window)
    employee_salary_label = tk.Label(add_employee_window, text="salario del empleado:")
    employee_salary_entry = tk.Entry(add_employee_window)
    employee_commision_label = tk.Label(add_employee_window, text="comisión del empleado (vacio si no tiene):")
    employee_commision_entry = tk.Entry(add_employee_window)
    employee_deptno_label = tk.Label(add_employee_window, text="departamento al cual pertenece el empleado: ")
    employee_deptno_entry = tk.Entry(add_employee_window)


    result_label = tk.Label(add_employee_window, text="", fg="red")  # Etiqueta para mostrar errores

    def submit():
        result_label.config(text="")  # Limpia el mensaje de error antes de intentar agregar un departamento

        # Obtener los datos del usuario desde la ventana emergente
        emp_id = employee_emp_id_entry.get()
        emp_name = employee_name_entry.get()
        emp_job = employee_job_entry.get()
        emp_manager = employee_manager_entry.get()
        emp_hiredate = employee_hiredate_entry.get()
        emp_salary = employee_salary_entry.get()
        emp_commision = employee_commision_entry.get()
        emp_deptno = employee_deptno_entry.get()


        connection = connect_to_oracle()
        if connection:
            cursor = connection.cursor()
            try:
                op.add_emp(cursor,emp_id,emp_name,emp_job,emp_manager,emp_hiredate,emp_salary,emp_commision,emp_deptno)
                connection.commit()
                result_label.config(text="Empleado agregado existosamente",fg="green")
            except ValueError as e:
                result_label.config(text=str(e),fg="red")
            except oracledb.DatabaseError as e:
                result_label.config(text="Error inesperado: " + str(e),fg="red")
            finally:
                cursor.close()
                connection.close()



    submit_button = tk.Button(add_employee_window, text="Agregar", command=submit)
    employee_emp_id_label.pack()
    employee_emp_id_entry.pack()
    employee_name_label.pack()
    employee_name_entry.pack()
    employee_job_label.pack()
    employee_job_entry.pack()
    employee_manager_label.pack()
    employee_manager_entry.pack()
    employee_hiredate_label.pack()
    employee_hiredate_entry.pack()
    employee_salary_label.pack()
    employee_salary_entry.pack()
    employee_commision_label.pack()
    employee_commision_entry.pack()
    employee_deptno_label.pack()
    employee_deptno_entry.pack()
    result_label.pack()  # Agrega el widget de etiqueta para mostrar errores
    submit_button.pack()

########################################################################################################
# Función para eliminar un empleado 

def delete_employee():
    # Ventana emergente para agregar departamento
    delete_employee_window = tk.Toplevel(root)
    delete_employee_window.title("Eliminar Empleado")

    employee_empno_label = tk.Label(delete_employee_window, text="Id de Empleado:")
    employee_empno_entry = tk.Entry(delete_employee_window)


    result_label = tk.Label(delete_employee_window, text="", fg="red")  # Etiqueta para mostrar errores

    def submit():
        result_label.config(text="")  # Limpia el mensaje de error antes de intentar agregar un departamento

        # Obtener los datos del usuario desde la ventana emergente
        empno = employee_empno_entry.get()

        connection = connect_to_oracle()
        if connection:
            cursor = connection.cursor()
            try:
                op.delete_emp(cursor,empno)
                connection.commit()
                result_label.config(text="Empleado Eliminado exitosamente",fg="green")
            except ValueError as e:
                result_label.config(text=str(e),fg="red")
            except oracledb.DatabaseError as e:
                result_label.config(text="Error inesperado: " + str(e),fg="red")
            finally:
                cursor.close()
                connection.close()



    submit_button = tk.Button(delete_employee_window, text="Eliminar", command=submit)
    employee_empno_label.pack()
    employee_empno_entry.pack()
    result_label.pack()  # Agrega el widget de etiqueta para mostrar errores
    submit_button.pack()





#######################################################################################################


# Función para actualizar un empleado
def update_employee():
    # Ventana emergente para agregar departamento
    update_employee_window = tk.Toplevel(root)
    update_employee_window.title("Actualizar Empleado")

    update_employee_emp_id_label = tk.Label(update_employee_window, text="id del empleado a actualizar:")
    update_employee_emp_id_entry = tk.Entry(update_employee_window)
    update_employee_name_label = tk.Label(update_employee_window, text="Nombre del empleado:")
    update_employee_name_entry = tk.Entry(update_employee_window)
    update_employee_job_label = tk.Label(update_employee_window, text="Puesto del empleado:")
    update_employee_job_entry = tk.Entry(update_employee_window)
    update_employee_manager_label = tk.Label(update_employee_window, text="id del manager:")
    update_employee_manager_entry = tk.Entry(update_employee_window)
    update_employee_hiredate_label = tk.Label(update_employee_window, text="fecha de contratación: dd/mm/aaaa")
    update_employee_hiredate_entry = tk.Entry(update_employee_window)
    update_employee_salary_label = tk.Label(update_employee_window, text="salario del empleado:")
    update_employee_salary_entry = tk.Entry(update_employee_window)
    update_employee_commision_label = tk.Label(update_employee_window, text="comisión del empleado (vacio si no tiene):")
    update_employee_commision_entry = tk.Entry(update_employee_window)
    update_employee_deptno_label = tk.Label(update_employee_window, text="departamento nuevo al que pertenecerá el empleado: ")
    update_employee_deptno_entry = tk.Entry(update_employee_window)

    result_label = tk.Label(update_employee_window, text="", fg="red")  # Etiqueta para mostrar errores

    def submit():
        result_label.config(text="")  # Limpia el mensaje de error antes de intentar agregar un departamento

        # Obtener los datos del usuario desde la ventana emergente
        emp_id = update_employee_emp_id_entry.get()
        emp_name = update_employee_name_entry.get()
        emp_job = update_employee_job_entry.get()
        emp_manager = update_employee_manager_entry.get()
        emp_hiredate = update_employee_hiredate_entry.get()
        emp_salary = update_employee_salary_entry.get()
        emp_commision = update_employee_commision_entry.get()
        emp_deptno = update_employee_deptno_entry.get()

        connection = connect_to_oracle()
        if connection:
            cursor = connection.cursor()
            try:
                op.update_emp(cursor,emp_id,emp_name,emp_job,emp_manager,emp_hiredate,emp_salary,emp_commision,emp_deptno)
                connection.commit()
                result_label.config(text="Empleado actualizado exitosamente",fg="green")
            except ValueError as e:
                result_label.config(text=str(e),fg="red")
            except oracledb.DatabaseError as e:
                result_label.config(text="Error inesperado: " + str(e),fg="red")
            finally:
                cursor.close()
                connection.close()



    submit_button = tk.Button(update_employee_window, text="Actualizar", command=submit)
    update_employee_emp_id_label.pack()
    update_employee_emp_id_entry.pack()
    update_employee_name_label.pack()
    update_employee_name_entry.pack()
    update_employee_job_label.pack()
    update_employee_job_entry.pack()
    update_employee_manager_label.pack()
    update_employee_manager_entry.pack()
    update_employee_hiredate_label.pack()
    update_employee_hiredate_entry.pack()
    update_employee_salary_label.pack()
    update_employee_salary_entry.pack()
    update_employee_commision_label.pack()
    update_employee_commision_entry.pack()
    update_employee_deptno_label.pack()
    update_employee_deptno_entry.pack()
    result_label.pack()  # Agrega el widget de etiqueta para mostrar errores
    submit_button.pack()


#########################################################################################################

# Función para Verificar si un departamento no tiene empleados

def noEmp_department():
    # Ventana emergente para agregar departamento
    noEmp_department_window = tk.Toplevel(root)
    noEmp_department_window.title(" Verificar si un departamento no tiene empleados")

    noEmp_department_number_label = tk.Label(noEmp_department_window, text="Id de Departamento:")
    noEmp_department_number_entry = tk.Entry(noEmp_department_window)


    result_label = tk.Label(noEmp_department_window, text="", fg="red")  # Etiqueta para mostrar errores

    def submit():
        result_label.config(text="")  # Limpia el mensaje de error antes de intentar agregar un departamento

        # Obtener los datos del usuario desde la ventana emergente
        depto_no = noEmp_department_number_entry.get()

        connection = connect_to_oracle()
        if connection:
            cursor = connection.cursor()
            try:
                aux = op.noEmp_depto(cursor, depto_no)
                connection.commit()
                result_label.config(text=aux,fg="green")
            except ValueError as e:
                result_label.config(text=str(e),fg="red")
            except oracledb.DatabaseError as e:
                result_label.config(text="Error inesperado: " + str(e),fg="red")
            finally:
                cursor.close()
                connection.close()



    submit_button = tk.Button(noEmp_department_window, text="Verificar", command=submit)
    noEmp_department_number_label.pack()
    noEmp_department_number_entry.pack()
    result_label.pack()  # Agrega el widget de etiqueta para mostrar errores
    submit_button.pack()


#######################################################################################################
#funcion para mostrar la tabla de empleados
def mostrar_tabla_emp():
    connection = connect_to_oracle()
    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM emp") 
        column_names = [desc[0] for desc in cursor.description]

        # Crear una ventana emergente para mostrar la tabla
        tabla_window = tk.Toplevel(root)
        tabla_window.title("Tabla de Datos")


        tree = ttk.Treeview(tabla_window, columns=column_names, show="headings")

        for col in column_names:
            tree.heading(col, text=col)
            tree.column(col, width=100)

        for row in cursor:
            tree.insert("", "end", values=row)

        tree.pack()

########################################################################################################

#funcion para mostrar la tabla de departamentos
def mostrar_tabla_dept():
    connection = connect_to_oracle()
    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM dept")  
        column_names = [desc[0] for desc in cursor.description]

        # Crear una ventana emergente para mostrar la tabla
        tabla_window = tk.Toplevel(root)
        tabla_window.title("Tabla de Datos")


        tree = ttk.Treeview(tabla_window, columns=column_names, show="headings")

        for col in column_names:
            tree.heading(col, text=col)
            tree.column(col, width=100)

        for row in cursor:
            tree.insert("", "end", values=row)

        tree.pack()


##########################################################################################################
# Función para salir de la aplicación
def salir():
    root.destroy()


#######################################################################################################
# Crear la ventana principal
root = tk.Tk()
root.title("Interfaz para Base de Datos Oracle")

######DEPARTAMENTOS###
# Botón para agregar departamento
add_department_button = tk.Button(root, text="Agregar Departamento", command=add_department)
# Botón para updatear departamento
update_department_button = tk.Button(root, text="Actualizar Departamento", command=update_department)
# Botón para eliminar departamento
delete_department_button = tk.Button(root, text="Eliminar Departamento", command=delete_department)
###########EMPLEADOOOOOOS############
# Botón para agregar empleadooo
add_employee_button = tk.Button(root, text="Agregar Empleado", command=add_employee)
# Botón para eliminar empleadooo
delete_employee_button = tk.Button(root, text="Eliminar Empleado", command=delete_employee)
# Botón para actualizar empleadooo
update_employee_button = tk.Button(root, text="Actualizar Empleado", command=update_employee)
# Botón para Verificar si un departamento no tiene empleados
noEmp_department_button = tk.Button(root, text="Verificar si un departamento no tiene empleados", command=noEmp_department)
#Boton mostrar tabla Empleados 
mostrar_tabla_emp_button = tk.Button(root, text="Consultar Tabla Empleados", command=mostrar_tabla_emp)
#Boton mostrar tabla Departamentos 
mostrar_tabla_dept_button = tk.Button(root, text="Consultar Tabla Departamentos", command=mostrar_tabla_dept)
# Botón para salir
salir_button = tk.Button(root, text="Salir", command=salir)




# Diseño de la interfaz
add_department_button.pack()
update_department_button.pack()
delete_department_button.pack()
add_employee_button.pack()
delete_employee_button.pack()
update_employee_button.pack()
noEmp_department_button.pack()
mostrar_tabla_emp_button.pack()
mostrar_tabla_dept_button.pack()
salir_button.pack()








root.mainloop()

import tkinter as tk
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

# Crear la ventana principal
root = tk.Tk()
root.title("Interfaz para Base de Datos Oracle")

# Botón para agregar departamento
add_department_button = tk.Button(root, text="Agregar Departamento", command=add_department)

# Diseño de la interfaz
add_department_button.pack()

root.mainloop()

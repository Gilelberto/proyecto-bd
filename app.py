import oracledb
import operations as op
# Configurar los detalles de la conexión
username = 'SCOTT'
password = 'scott'
dsn = 'localhost:1521/xepdb1'  # Por ejemplo, 'localhost/XE' para una base de datos local

# Crear una conexión
connection = oracledb.connect(user=username, password = password,dsn= dsn)

cursor = connection.cursor()

try:

    # Llamar al procedimiento almacenado con parámetros de entrada
    #params = (parametro1, parametro2, parametro3)  # Reemplaza con los valores adecuados
    #cursor.callproc("Add_depto")#, params)
    while True:
        print("Menú:")
        print("1. Agregar departamento")
        print("2. Actualizar departamento")
        print("3. Eliminar departamento")
        print("4. Agregar empleado")
        print("5. Eliminar empleado")
        print("6. Actualizar empleado")
        print("7. Verificar si un departamento no tiene empleados")
        print("8. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            op.add_depto(cursor)
        elif opcion == "2":
            op.update_depto()
        elif opcion == "3":
            op.delete_depto()
        elif opcion == "4":
            op.add_emp()
        elif opcion == "5":
            op.delete_emp()
        elif opcion == "6":
            op.update_emp()
        elif opcion == "7":
            op.noEmp_depto(cursor)
        elif opcion == "8":
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

except oracledb.DatabaseError as e:
    error, = e.args
    print("Error de Oracle:", error.message)

finally:
    # Cierra el cursor y la conexión
    cursor.close()
    connection.close()
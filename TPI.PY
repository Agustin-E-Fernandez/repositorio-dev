print("===========================================================================")
print("TP integrador – Repetitivas- Condicionales y Secuenciales")
print("El trabajo consta de 5 Ejercicios")
print("===========================================================================")

ejerciciosvistos = [False] * 6  

while True:
    
    
    print("Progreso de los Ejercicios")
    print("\n")
    for i in range(1, 6):
        estado = "X Visto" if ejerciciosvistos[i] else "O Pendiente"
        print(f"Ejercicio {i}: {estado}")
    print("===========================================================================")
    
    while True:
        opcion = input("Qué ejercicio desea evaluar? (1-5): ").strip()
        
        if opcion.isdigit():
            opcion = int(opcion)
            if 1 <= opcion <= 5:
                break  
            else:
                print("Error: Ingrese un número entre 1 y 5.")
        else:
            print("Error: Ingrese solo números.")
     

    ## Ejercicio 1 ##############################################################################
    if opcion == 1:
        ejerciciosvistos[1] = True   # Marcar como visto
        
        print("===========================================================================")
        print("\nEjercicio 1: Simular una Compra con Validaciones y Cálculo Total")
        # Nombre del Cliente 
        nombre = input("\nIngresar el Nombre del Cliente: ")

        while nombre.isalpha() == False:
            print("Error: Ingresar el Nombre del Cliente.")
            nombre = input("Ingresar el Nombre del Cliente: ")
        cantidadproductos = input("Ingresar la Cantidad de Productos: ")

        # Ingresar la Cantidad de Productos 
        while cantidadproductos.isdigit() == False or cantidadproductos == "0":
            print("Error: Ingrese un número entero mayor a 0.")

            cantidadproductos = input("Ingresar la Cantidad de Productos: ")

        cantidad = int(cantidadproductos)
        sindescuento = 0
        condescuento = 0

        for x in range(1, cantidad + 1):
            print(f"Producto {x}")
            
            precio = input("Precio: ")
            while precio.isdigit() == False:
                print("Error: Ingrese un Precio Válido")
                precio = input("Precio: ")
            
            precio = int(precio)
            
            # Descuento 
            opcion = input("Tiene descuento? (S/N): ").lower()
            while opcion != "s" and opcion != "n":
                print("Error: Por favor ingresar 's' o 'n'.")
                opcion = input("Tiene descuento? (S/N): ").lower()
            
            if opcion == "s":
                descuento = precio * 0.10
                preciofinal = precio - descuento
            else:
                preciofinal = precio
                
            sindescuento = sindescuento + precio
            condescuento = condescuento + preciofinal

        ahorro = sindescuento - condescuento
        promedio = condescuento / cantidad
        # Resultado
        print(f"\nCliente: {nombre}")
        print(f"Cantidad de productos: {cantidad}")
        print(f"Total sin descuentos: ${sindescuento}")
        print(f"Total con descuentos: ${condescuento:.2f}")
        print(f"Ahorro: ${ahorro:.2f}")
        print(f"Promedio por producto: ${promedio:.2f}")

    
    ## Ejercicio 2 ##############################################################################
    elif opcion == 2:
        ejerciciosvistos[2] = True   
        
        print("===========================================================================")
        print("\nEjercicio 2 — Acceso al Campus y Menú Seguro")

        usuariocorrecto = "alumno"
        clavecorrecta = "python123"
        intentos = 0
        acceso = False

        while intentos < 3:
            intentos = intentos + 1
            print("Intento", intentos, "/ 3")
            
            usuario = input("\nUsuario: ")
            clave = input("Clave: ")
            
            if usuario == usuariocorrecto and clave == clavecorrecta:
                acceso = True
                intentos = 3  
            else:
                print("Error: credenciales inválidas.")

        if acceso == False:
            print("\nCuenta bloqueada")
        else:
            print("\nAcceso concedido.")
            
            opcion = 0
            while opcion != 4:
                print("\n1) Estado 2) Cambiar clave 3) Mensaje 4) Salir")
                entrada = input("Opción: ")
                
                if entrada.isdigit() == True:
                    opcion = int(entrada)
                    
                    if opcion == 1:
                        print("\nEstado: Inscripto")
                        
                    elif opcion == 2:
                        nuevaclave = input("Nueva clave (Minimo 6 caracteres): ")
                        
                        while len(nuevaclave) < 6:
                            print("Error: la clave es muy corta.")
                            nuevaclave = input("Nueva clave: ")
                        
                        confirmacion = input("Confirme la clave: ")
                        if nuevaclave == confirmacion:
                            clavecorrecta = nuevaclave
                            print("\nLa clave se ha modificado con éxito")
                        else:
                            print("\nError: las claves no coinciden")
                    
                    elif opcion == 3:
                        print("\n!Un gran poder conlleva una gran responsabilidad!")
                        
                    elif opcion == 4:
                        print("\nSaliendo del Sistema")
                    
                    else:
                        print("\nError, Intente Nuevamente")
                else:
                    print("\nError: Ingrese un Número Válido.")

    ## Ejercicio 3 ##############################################################################
    elif opcion == 3:
        ejerciciosvistos[3] = True   # Marcar como visto
        
        print("===========================================================================")
        print("\nEjercicio 3 (Alta) — Agenda de Turnos con Nombres")

        # Operador
        nombredeloperador = input("Nombre del Operador: ")
        while nombredeloperador.isalpha() == False:
            print("Error: solo Letras")
            nombredeloperador = input("Nombre del Operador: ")

        # Turnos 
        lunes1 = ""
        lunes2 = ""
        lunes3 = ""
        lunes4 = ""

        martes1 = ""
        martes2 = ""
        martes3 = ""

        # Menú Principal 
        opcion = 0
        while opcion != 5:
            print("===============================================")
            print("-----------------------------------------------")
            print("\nMENÚ DE TURNOS")
            print("\n1. Reservar Turno")
            print("2. Cancelar Turno")
            print("3. Ver Agenda del Día")
            print("4. Ver Resumen General")
            print("5. Cerrar Sistema")
            print("\n-----------------------------------------------")
            
            print("===============================================")
            opciones = input("\nElija una Opción: ")
            
            if opciones.isdigit() == True:
                opcion = int(opciones)
                
                # Opción 1: Reservar
                if opcion == 1:
                    dia = input("\nElegir Día (1=Lunes, 2=Martes): ")
                    
                    if dia == "1" or dia == "2":
                        paciente = input("\nNombre del Paciente: ")
                        
                        if paciente.isalpha() == True:
                            # Verificar si ya existe el nombre
                            repetido = False
                            if dia == "1":
                                if paciente == lunes1 or paciente == lunes2 or paciente == lunes3 or paciente == lunes4:
                                    repetido = True
                            else:
                                if paciente == martes1 or paciente == martes2 or paciente == martes3:
                                    repetido = True
                            
                            if repetido == True:
                                print("Error: El paciente ya tiene un turno este día.")
                                print("===============================================")
                            else:
                                # Buscar primer lugar libre
                                asignado = False
                                if dia == "1":
                                    if lunes1 == "":
                                        lunes1 = paciente
                                        asignado = True
                                    elif lunes2 == "":
                                        lunes2 = paciente
                                        asignado = True
                                    elif lunes3 == "":
                                        lunes3 = paciente
                                        asignado = True
                                    elif lunes4 == "":
                                        lunes4 = paciente
                                        asignado = True
                                else:
                                    if martes1 == "":
                                        martes1 = paciente
                                        asignado = True
                                    elif martes2 == "":
                                        martes2 = paciente
                                        asignado = True
                                    elif martes3 == "":
                                        martes3 = paciente
                                        asignado = True
                                
                                if asignado == True:
                                    print("\n¡Turno reservado con éxito!")
                                    print("===============================================")
                                else:
                                    print("\nLo sentimos, no hay más cupos para este día.")
                                    print("===============================================")
                        else:
                            print("\nError: El nombre debe contener solo letras.")
                            print("===============================================")
                    else:
                        print("\nError: Día inválido.")
                        print("===============================================")

                # Opcion 2: Cancelar
                elif opcion == 2:
                    dia = input("\nElegir día (1=Lunes, 2=Martes): ")
                    paciente = input("\nNombre del paciente a cancelar: ")
                    cancelado = False
                    
                    if dia == "1":
                        if paciente == lunes1: lunes1 = ""; cancelado = True
                        elif paciente == lunes2: lunes2 = ""; cancelado = True
                        elif paciente == lunes3: lunes3 = ""; cancelado = True
                        elif paciente == lunes4: lunes4 = ""; cancelado = True
                    elif dia == "2":
                        if paciente == martes1: martes1 = ""; cancelado = True
                        elif paciente == martes2: martes2 = ""; cancelado = True
                        elif paciente == martes3: martes3 = ""; cancelado = True
                    
                    if cancelado == True:
                        print("\nTurno cancelado correctamente.")
                        print("===============================================")
                    else:
                        print("No se encontró al paciente.")
                        print("===============================================")

                # Opción 3: Ver la agenda
                elif opcion == 3:
                    dia = input("\nVer agenda (1=Lunes, 2=Martes): ")
                    print("===============================================")
                    if dia == "1":
                        print("Agenda Lunes:")
                        print("===============================================")
                        print("\n")
                        if lunes1 == "": print("1. (libre)") 
                        else: print("1.", lunes1)
                        if lunes2 == "": print("2. (libre)") 
                        else: print("2.", lunes2)
                        if lunes3 == "": print("3. (libre)") 
                        else: print("3.", lunes3)
                        if lunes4 == "": print("4. (libre)") 
                        else: print("4.", lunes4)
                    elif dia == "2":
                
                        print("Agenda Martes:")
                        print("===============================================")
                        print("\n")
                        if martes1 == "": print("\n1. (libre)") 
                        else: print("1.", martes1)
                        if martes2 == "": print("2. (libre)") 
                        else: print("2.", martes2)
                        if martes3 == "": print("3. (libre)") 
                        else: print("3.", martes3)

                # Opción 4: Resumen General
                elif opcion == 4:
                    # Lunes
                    ocupadoloslunes = 0
                    if lunes1 != "": ocupadoloslunes = ocupadoloslunes + 1
                    if lunes2 != "": ocupadoloslunes = ocupadoloslunes + 1
                    if lunes3 != "": ocupadoloslunes = ocupadoloslunes + 1
                    if lunes4 != "": ocupadoloslunes = ocupadoloslunes + 1
                    
                    # Martes
                    ocupadolosmartes = 0
                    if martes1 != "": ocupadolosmartes = ocupadolosmartes + 1
                    if martes2 != "": ocupadolosmartes = ocupadolosmartes + 1
                    if martes3 != "": ocupadolosmartes = ocupadolosmartes + 1
                    
                    print("\nLunes:", ocupadoloslunes, "ocupados,", (4 - ocupadoloslunes), "libres.")
                    print("===============================================")
                    print("\nMartes:", ocupadolosmartes, "ocupados,", (3 - ocupadolosmartes), "libres.")
                    print("===============================================")
                    
                    if ocupadoloslunes > ocupadolosmartes:
                        print("\nDía con más turnos: Lunes")
                        print("===============================================")
                    elif ocupadolosmartes > ocupadoloslunes:
                        print("\nDía con más turnos: Martes")
                        print("===============================================")
                    else:
                        print("\nAmbos días tienen la misma cantidad de turnos.")
                        print("===============================================")

                elif opcion == 5:
                    print("Cerrando el sistema de", nombredeloperador, ". ¡Hasta luego!")
                    print("===============================================")
                    
                else:
                    print("Error: Elija una opción entre 1 y 5.")
                    print("===============================================")
            else:
                print("Error: Debe ingresar un número.")
                print("===============================================")

    ## Ejercicio 4 ##############################################################################
    elif opcion == 4:
        ejerciciosvistos[4] = True   # Marcar como visto
        
        energia = 100
        tiempo = 12
        cerraduras_abiertas = 0
        alarma = False
        codigo_parcial = ""
        forzar_seguidas = 0

        nombre = input("Ingrese su nombre: ")

        while nombre.isalpha() == False:
            print("Error. Solo letras.")
            nombre = input("Ingrese su nombre: ")

        print("===========================================================================")
        print("\nBienvenido", nombre, "a la Bóveda") 


        while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3:

            if alarma == True and tiempo <= 3:
                print("La Bóveda se Bloqueó. PERDISTE")
                break

            # Variables iniciales
            print("." + "." *50)
            print("\nESTADO")
            print("Energía:", energia)
            print("Tiempo:", tiempo)
            print("Cerraduras abiertas:", cerraduras_abiertas)
            print("Alarma:", alarma)
            print("Código:", codigo_parcial)

            # Opciones a elegir
            print("." + "." *50)
            print("\n1. Forzar cerradura")
            print("2. Hackear panel")
            print("3. Descansar")

            opcion = input("Elija una Opción: ")

            # Validar opciones
            while opcion.isdigit() == False or int(opcion) < 1 or int(opcion) > 3:
                print("Error")
                opcion = input("Elija una Opción: ")

            opcion = int(opcion)

            # Opción 1: Forzar Cerradura
            if opcion == 1:
                energia -= 20
                tiempo -= 2
                forzar_seguidas += 1

                # Regla Anti-Spam
                if forzar_seguidas == 3:
                    print("Forzaste demasiado la cerradura")
                    print("La cerradura se trabó y se activó la alarma")
                    alarma = True
                    forzar_seguidas = 0
                    break

                else:
                    # Energía baja
                    if energia < 40:
                        numero = input("Riesgo! Elegí un número del 1 al 3: ")

                        while numero.isdigit() == False or int(numero) < 1 or int(numero) > 3:
                            print("Error")
                            numero = input("Elegí un número del 1 al 3: ")

                        if int(numero) == 3:
                            print("Se Activó la Alarma")
                            alarma = True

                    # si no hay alarma abre la cerradura 
                    if alarma == False:
                        cerraduras_abiertas += 1
                        print("Abriste una Cerradura")
                    else:
                        print("No pudiste abrir la cerradura")

            # Opción 2: Hackear Panel 
            elif opcion == 2:
                energia -= 10
                tiempo -= 3
                forzar_seguidas = 0  

                print("Hackeando")

                for i in range(4):
                    print("Paso", i + 1)
                    codigo_parcial += "A"

                if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
                    cerraduras_abiertas += 1
                    print("Se abrió una cerradura automáticamente")

            # Opción 3: Descansar
            elif opcion == 3:
                energia += 15
                tiempo -= 1
                forzar_seguidas = 0  

                if energia > 100:
                    energia = 100

                if alarma == True:
                    energia -= 10
                    print("La alarma te quitó energía")

                print("Descansaste")

        # Resultado
        if cerraduras_abiertas == 3:
            print("\nGANASTE! Abriste la bóveda")

        elif energia <= 0 or tiempo <= 0:
            print("\nPERDISTE. Te quedaste sin recursos")    

    ## Ejercicio 5 ##############################################################################
    elif opcion == 5:
        ejerciciosvistos[5] = True   # Marcar como visto
        
        print("===========================================================================")
        print("\nEjercicio 5 — Escape Room: La Arena del Gladiador")
        print("BIENVENIDO A LA ARENA")

        # Paso 1: Nombre del gladiador
        Nombre = input("Nombre del Gladiador: ")

        while Nombre.isalpha() == False or Nombre == "":
            print("Error: Solo se permiten letras.")
            Nombre = input("Nombre del Gladiador: ")

        # Paso 2: Estadísticas iniciales
        HPGladiador = 100
        HPEnemigo = 100
        Posiones = 3
        DanoBase = 15
        DanoEnemigo = 12
        TurnodelGladiador = True
        Jugando = True

        print("INICIO DEL COMBATE")

        # Paso 3: Ciclo de combate
        while Jugando == True:

            print("\n----------------------------------------------")
            print(f"{Nombre} (HP: {HPGladiador}) vs Enemigo (HP: {HPEnemigo}) | Pociones: {Posiones}")
            print("----------------------------------------------")
            print("Elige acción:")
            print("1. Ataque Pesado")
            print("2. Ráfaga Veloz")
            print("3. Curar")

            Opcion = input("Opción: ")

            # Validación del menú
            while Opcion.isdigit() == False or (Opcion != "1" and Opcion != "2" and Opcion != "3"):
                if Opcion.isdigit() == False:
                    print("Error: Ingrese un número válido.")
                else:
                    print("Error: la opción debe ser 1, 2 o 3.")
                Opcion = input("Opción: ")

            # Turno del jugador
            if TurnodelGladiador == True:

                # Opción 1: Ataque Pesado
                if Opcion == "1":
                    if HPEnemigo < 20:
                        Dano = DanoBase * 1.5
                        print(">> ¡Golpe Crítico!")
                    else:
                        Dano = DanoBase

                    HPEnemigo = HPEnemigo - Dano
                    print(f"\n¡Atacaste al enemigo por {Dano} puntos de daño!")

                # Opción 2: Ráfaga Veloz
                elif Opcion == "2":
                    print(">> ¡Inicias una ráfaga de golpes!")
                    for i in range(3):
                        HPEnemigo = HPEnemigo - 5
                        print("> Golpe conectado por 5 de daño")

                # Opción 3: Curar
                elif Opcion == "3":
                    if Posiones > 0:
                        HPGladiador = HPGladiador + 30
                        Posiones = Posiones - 1
                        print("¡Te curaste +30 HP!")
                    else:
                        print("¡No quedan pociones!")

            # Si el enemigo ya murió, termina el juego
            if HPEnemigo <= 0:
                HPEnemigo = 0
                Jugando = False

            # Turno del enemigo (solo si sigue vivo)
            if Jugando == True:
                HPGladiador = HPGladiador - DanoEnemigo
                print(f"¡El enemigo te atacó por {DanoEnemigo} puntos de daño!")

            # Si el jugador muere, termina el juego
            if HPGladiador <= 0:
                HPGladiador = 0
                Jugando = False

        # Paso 4: Fin del juego
        print("\n=== FIN DEL COMBATE ===")
        print(f"{Nombre} (HP: {HPGladiador}) vs Enemigo (HP: {HPEnemigo})")

        if HPGladiador > 0:
            print(f"¡VICTORIA! {Nombre} ha ganado la batalla.")
        else:
            print("DERROTA. Has caído en combate.")

    else:   
        print("Opción inválida")
    
    print("===========================================================================")  
    
    while True:                                  
        seguir = input("\nDesea seguir evaluando? (si/no): ").lower().strip()
        
        if seguir in ["si", "s", "no", "n"]:
            if seguir in ["si", "s"]:
                seguir = "si"
            else:
                seguir = "no"
            break
        else:
            print("Error: Por favor ingrese 'si', 's', 'no' o 'n'.")
    
    print("\n")
    
    if seguir == "no":
        print("Programa finalizado.")
        break  
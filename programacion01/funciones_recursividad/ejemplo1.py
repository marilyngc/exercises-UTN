def cuenta_regresiva (iteraciones):
    if iteraciones != -1:
        print(f"valor de la iteracion {iteraciones}")
        cuenta_regresiva(iteraciones - 1);


cuenta_regresiva(10);
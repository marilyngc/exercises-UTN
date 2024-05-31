# Crea la clase de instancia Linterna.

# La misma debe tener:
# A. Los atributos marca, nivelBateria, color.
# B. Sobrecarga de constructores:


# Un constructor que inicialice solo marca y color, estableciendo un valor por defecto de 100 para nivelBateria.

# D. El método LinternaToString(), este método debe retornar un string con toda su información.
# E. El método Encender(int minutos) que retornará un booleano para informar si pudo estar encendida la cantidad de minutos recibidos por parámetro. Tener en cuenta que para poder encenderse se debe tener batería y por cada minuto encendida se consume 1% de batería.
# F. Sobrecarga del método Encender() para que también pueda recibir el tiempo en horas.
# G. En un proyecto de consola, crear un objeto del tipo Linterna, mostrar todos sus valores y dentro de un bucle repetitivo usar el método Encender(). Este deberá repetirse hasta que la linterna agote su batería y se deberá informar cuántas repeticiones logra realizar.
# Cloud_Computing_Proyecto_Parcial_2023-1

Tablas para la base de datos:

Client(pkey:id, firstname, lastname)
Car(pkey:id, brand, model, type, year, cost)
Location(pkey:id, address, district)
Reservation(pkey:id, client.id, car.id, location.id, date, start_of_rental, end_of_rental, total_cost)

DONE:
- Esqueleto de los archivos:
    - app.py (El main file, se setea la database con SQLAlchemy y se encuentra el run)
    - models.py (Donde estan guardardos los modelos)
    - {model}.py (Los endpoints para las APIs de cada modelo)

TO DO:
1. Backend
    Supongo si logra funcionar de manera local, podrá funcionar con contenedores
    - Levantar la base de datos:
        - Primero la probamos en una base de datos local
        - De preferencia postgres (ya que es la que sé mas)
    - Probar la API
        - Usamos Testfully a ver si agarra bien los endpoints y la base de datos
        - Dependiendo como funcione, modificamos los archivos
        - Una vez funcione como debería, procedemos a la siguiente fase
    
2. Frontend
    Lo mismo que en backend, probamos local y de ahi a contenedores
    - Crear una web que use las APIs
        - No tengo ni idea de çómo hacerla con un framework de javascript (como Vue).
        - Si alguien sabe, que lo intente. Caso contrario probamos con puro HTML
    - Probar la web
        - Levantamos la aplicacion en Local y probamos a ver si funciona como debe.
        - Dependiendo de como resulte, modificamos los archivos
        - Una vez funcione como deberia, procedemos a la siguiente fase

3. Containers
    Si llegamos hasta acá es porque la aplicación en bloque funciona localmente
    - Separamos por contenedores
        - Supongo que tendremos un total de 5 contenedores : 4 para las APIs, 1 para la aplicacion (app.py, models.py y el frontend estatico)
        - Si usamos un framework para el frontend, creo que se usa un contenedor aparte
    - Probamos los contenedores
        - Creo que podemos probar cada contenedor de las APIs por su lado en Testfully.
        - Para probar la aplicacion levantariamos todo en un solo docker-compose

4. El resto
    Mas que ser lo ultimo, creo que deberia realizarse en paralelo con la aplicacion
    - Lo del diagrama de solucion
    - La documentacion de la aplicacion (el readme)
    - Un ppt para la presentacion
    - Un informe que incluya todo lo hecho en el proyecto (entregable para el profe)
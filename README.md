# Cloud_Computing_Proyecto_Parcial_2023-1

Tablas para la base de datos:

Client(pkey:id, firstname, lastname)
Car(pkey:id, brand, model, type, year, cost)
Location(pkey:id, address, district)
Reservation(pkey:id, client.id, car.id, location.id, date, start_of_rental, end_of_rental, total_cost)

DONE:
- Script de las APIS
- Levantada la base de datos RDS

TO DO:

1. Backend:    
    - Montar contenedores
    - Probar APIS Testfully
    
2. Frontend:
    Lo mismo que en backend, probamos local y de ahi a contenedores
    - Crear una web que use las APIs
        - No tengo ni idea de çómo hacerla con un framework de javascript (como Vue).
        - Si alguien sabe, que lo intente. Caso contrario probamos con puro HTML
    - Probar la web en container/S3:
    
4. El resto:
    Mas que ser lo ultimo, creo que deberia realizarse en paralelo con la aplicacion
    - Lo del diagrama de solucion (CASI LISTO) falta consultar 
    - La documentacion de la aplicacion (el readme) (opcional
    - Un ppt para la presentacion 

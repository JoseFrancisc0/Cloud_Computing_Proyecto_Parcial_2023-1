# Cloud_Computing_Proyecto_Parcial_2023-1

Tablas para la base de datos:

Client(pkey:id, firstname, lastname)
Car(pkey:id, brand, model, type, year, cost)
Location(pkey:id, address, district)
Reservation(pkey:id, client.id, car.id, location.id, date, start_of_rental, end_of_rental, total_cost)

DONE:
- Base de datos RDS
- Backend (4 APIs en contenedores)
- MVs de Produccion
- Load Balancer

TO DO:
 
1. Backend:
   - Implementar CORS

2. Frontend:
    - A puro ChatGPT sacamos los HTMLs, CSSs y JSs
    - Y almacenamos (docker/S3)
    
3. El resto:
    Mas que ser lo ultimo, creo que deberia realizarse en paralelo con la aplicacion
    - Lo del diagrama de solucion (CASI LISTO) falta consultar 
    - La documentacion de la aplicacion (el readme) (opcional
    - Un ppt para la presentacion 

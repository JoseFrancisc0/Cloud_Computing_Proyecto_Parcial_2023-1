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
- Basic functional Frontend

TO DO:
 
1. Frontend:
    - Mas css
    - Meterlo en Bucket S3
    
2. El resto:
    - Lo del diagrama de solucion (CASI LISTO)
    - La documentacion de la aplicacion (el readme) Casi lo mismo del ppt
    - Un ppt para la presentacion 

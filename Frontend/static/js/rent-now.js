// USER
var clientID, clientFirstName, clientLastName;
const createUserForm = document.getElementById('create-user-form');
const createUserButton = document.getElementById('create-user-button');
const carSelectionForm = document.getElementById('car-selection-form');
// Submit Create User form
createUserForm.addEventListener('submit', async (event) => {
  event.preventDefault();
  clientID = createUserForm.elements['id'].value;
  clientFirstName = createUserForm.elements['firstname'].value;
  clientLastName = createUserForm.elements['lastname'].value;
  
  /// POST USER
  const clientPayload = {
    id: clientID,
    firstname: clientFirstName,
    lastname: clientLastName
  };
  try {
    const response = await fetch('http://lb-proyecto-prod-638305711.us-east-1.elb.amazonaws.com:8011/clients', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(clientPayload)
    });

    const data = await response.json();
    console.log(data);
    alert('User created successfully!');

  } catch (error) {
    console.error(error);
    alert('Error creating user.');
  }
}); /// END POST USER

// Enable/disable Create User button based on form validation
createUserForm.addEventListener('input', () => {
  const idField = createUserForm.elements['id'];
  createUserButton.disabled = !createUserForm.checkValidity() || idField.value.length !== 8;
});
/// END USER

// CAR LIST
var carId, carCostPerDay;
let cars; // define the cars array as a global variable

		fetch('http://lb-proyecto-prod-638305711.us-east-1.elb.amazonaws.com:8012/cars')
			.then(response => response.json())
			.then(data => {
				cars = data; // assign the fetched data to the cars array
				const carsTableBody = document.getElementById('cars-table-body');
				cars.forEach(car => {
					const row = document.createElement('tr');
					row.innerHTML = `
						<td><input type="radio" name="car" value="${car.id}"></td>
						<td>${car.id}</td>
						<td>${car.brand}</td>
						<td>${car.model}</td>
						<td>${car.type_of_car}</td>
						<td>${car.year_car}</td>
						<td>${car.cost_per_day}</td>
					`;
					carsTableBody.appendChild(row);
					});
				})
			.catch(error => console.error(error));

		const carsForm = document.getElementById('cars-form');
		carsForm.addEventListener('submit', event => {
			event.preventDefault();
			carId = carsForm.elements.car.value;
			console.log(`Selected car ID: ${carId}`);
			const selectedCar = cars.find(car => car.id == carId);
            carCostPerDay = selectedCar.cost_per_day;
            console.log(`Selected car price: ${carCostPerDay}`);
			// Do something with the selected car ID and price, such as submitting them to a server
		});
/// END CARS

// LOCATION LIST
var locationId;
fetch('http://lb-proyecto-prod-638305711.us-east-1.elb.amazonaws.com:8013/locations')
.then(response => response.json())
.then(locations => {
  const locationsTableBody = document.getElementById('locations-table-body');
  locations.forEach(location => {
    const row = document.createElement('tr');
    row.innerHTML = `
      <td><input type="radio" name="location" value="${location.id}"></td>
      <td>${location.id}</td>
      <td>${location.address}</td>
      <td>${location.district}</td>
    `;
    locationsTableBody.appendChild(row);
  });
})
.catch(error => console.error(error));
const locationsForm = document.getElementById('locations-form');
locationsForm.addEventListener('submit', event => {
event.preventDefault();
locationId = locationsForm.elements.location.value;
console.log(`Selected location ID: ${locationId}`);
// Do something with the selected location ID, such as submitting it to a server
});
/// END LOCATIONS


/// DATE SELECTOR
var startDate, endDate, nDays, currentDate, totalCost;
function saveDates(){
  // Get the values of the start and end dates
  startDate = new Date(document.getElementById("start-date").value);
  endDate = new Date(document.getElementById("end-date").value);
  // Add one day to the start and end dates
  var oneDayMs = 24 * 60 * 60 * 1000; // One day in milliseconds
  startDate.setTime(startDate.getTime() + oneDayMs);
  endDate.setTime(endDate.getTime() + oneDayMs);
  // Calculate the difference in milliseconds
  var differenceInMs = endDate.getTime() - startDate.getTime();
  // Convert the difference to days
  nDays = differenceInMs / (1000 * 60 * 60 * 24);
  // Save the current date
  currentDate = new Date().toISOString().slice(0, 10);
  startDate = startDate.toISOString().slice(0, 10);
  endDate = endDate.toISOString().slice(0, 10);
  console.log(`Selected start date: ${startDate}`);
  console.log(`Selected end date: ${endDate}`);
  console.log(`Difference: ${nDays}`);
  console.log(`Current date: ${currentDate}`);

  totalCost = nDays * carCostPerDay;
  console.log(`Total cost: ${totalCost}`);
}



const confirmRentButton = document.getElementById('confirmRent');

confirmRentButton.addEventListener('click', async (event) => {
    /// PAYLOAD
    const rentalPayload = {
        client_id: clientID,
        car_id: carId,
        location_id: locationId,
        date: currentDate,
        start_of_rental: startDate,
        end_of_rental: endDate,
        total_cost: totalCost
    };

    try {
        const response = await fetch('http://lb-proyecto-prod-638305711.us-east-1.elb.amazonaws.com:8014/reservations', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(rentalPayload)
        });

        const data = await response.json();
        console.log(data);
        alert('Reservation created successfully!');

    } catch (error) {
        console.error(error);
        alert('Error creating Reservation.');
    }
})
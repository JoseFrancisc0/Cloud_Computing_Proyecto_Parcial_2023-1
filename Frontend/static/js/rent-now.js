const createUserForm = document.getElementById('create-user-form');
const createUserButton = document.getElementById('create-user-button');
const carSelectionForm = document.getElementById('car-selection-form');
const selectCarForm = document.getElementById('select-car-form');
const selectCarButton = document.getElementById('select-car-button');

// Submit Create User form
createUserForm.addEventListener('submit', async (event) => {
  event.preventDefault();

  const id = createUserForm.elements['id'].value;
  const firstname = createUserForm.elements['firstname'].value;
  const lastname = createUserForm.elements['lastname'].value;

  const payload = {
    id: id,
    firstname: firstname,
    lastname: lastname
  };

  try {
    const response = await fetch('http://127.0.0.1:8011/clients', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(payload)
    });

    const data = await response.json();
    console.log(data);
    alert('User created successfully!');

    // Show Car Selection form
    createUserForm.style.display = 'none';
    carSelectionForm.style.display = 'block';
  } catch (error) {
    console.error(error);
    alert('Error creating user.');
  }
});

// Enable/disable Create User button based on form validation
createUserForm.addEventListener('input', () => {
  const idField = createUserForm.elements['id'];
  createUserButton.disabled = !createUserForm.checkValidity() || idField.value.length !== 8;
});

// CAR LIST
fetch('http://127.0.0.1:8012/cars')
.then(response => response.json())
.then(cars => {
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
const selectedCarId = carsForm.elements.car.value;
console.log(`Selected car ID: ${selectedCarId}`);
// Do something with the selected car ID, such as submitting it to a server
});

// LOCATION LIST
fetch('http://127.0.0.1:8013/locations')
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
const selectedLocationId = locationsForm.elements.location.value;
console.log(`Selected location ID: ${selectedLocationId}`);
// Do something with the selected location ID, such as submitting it to a server
});

/// DATE SELECTOR

function saveDates(){
  // Get the values of the start and end dates
  var startDate = new Date(document.getElementById("start-date").value);
  var endDate = new Date(document.getElementById("end-date").value);

  // Add one day to the start and end dates
  var oneDayMs = 24 * 60 * 60 * 1000; // One day in milliseconds
  startDate.setTime(startDate.getTime() + oneDayMs);
  endDate.setTime(endDate.getTime() + oneDayMs);

  // Calculate the difference in milliseconds
  var differenceInMs = endDate.getTime() - startDate.getTime();

  // Convert the difference to days
  var differenceInDays = differenceInMs / (1000 * 60 * 60 * 24);

  // Save the current date
  const currentDate = new Date().toISOString().slice(0,10);

  console.log(`Selected start date: ${startDate}`);
  console.log(`Selected end date: ${endDate}`);
  console.log(`Difference: ${differenceInDays}`);
  console.log(`Current date: ${currentDate}`);
}
// Get elements from the DOM
const searchForm = document.getElementById('search-form');
const carContainer = document.getElementById('car-container');

// Function to render the car list
function renderCarList(cars) {
  carContainer.innerHTML = '';
  for (const car of cars) {
    const carCard = document.createElement('div');
    carCard.className = 'car-card';

    const carImage = document.createElement('img');
    carImage.className = 'car-image';
    carImage.src = car.image;
    carImage.alt = `${car.brand} ${car.model}`;

    const carHeading = document.createElement('h2');
    carHeading.className = 'car-heading';
    carHeading.textContent = `${car.brand} ${car.model}`;

    const carDetails1 = document.createElement('p');
    carDetails1.className = 'car-details';
    carDetails1.textContent = `Type: ${car.type_of_car}`;

    const carDetails2 = document.createElement('p');
    carDetails2.className = 'car-details';
    carDetails2.textContent = `Year: ${car.year_car}`;

    const carDetails3 = document.createElement('p');
    carDetails3.className = 'car-details';
    carDetails3.textContent = `Cost per day: $${car.cost_per_day}`;

    carCard.appendChild(carImage);
    carCard.appendChild(carHeading);
    carCard.appendChild(carDetails1);
    carCard.appendChild(carDetails2);
    carCard.appendChild(carDetails3);

    carContainer.appendChild(carCard);
  }
}

// Function to filter the car list based on search criteria
function filterCars(cars, brand, year) {
  return cars.filter(car => {
    const brandMatch = brand === '' || car.brand.toLowerCase().includes(brand.toLowerCase());
    const yearMatch = year === '' || car.year_car == year;
    return brandMatch && yearMatch;
  });
}

// Function to handle form submission and filter the car list
function handleSearch(event) {
  event.preventDefault();
  const brand = event.target.elements.brand.value.trim();
  const year = event.target.elements.year.value.trim();
  const filteredCars = filterCars(cars, brand, year);
  renderCarList(filteredCars);
}

// Fetch the car list from the API
let cars;
fetch('http://127.0.0.1:8012/cars')
  .then(response => response.json())
  .then(data => {
    cars = data;
    renderCarList(cars);
  });

// Add event listener for form submission
searchForm.addEventListener('submit', handleSearch);

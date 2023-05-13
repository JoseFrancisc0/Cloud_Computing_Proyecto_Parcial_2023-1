const locationContainer = document.getElementById('location-container');
const searchForm = document.getElementById('search-form');

let locations = [];

async function getLocations() {
  const response = await fetch('http://127.0.0.1:8013/locations');
  const data = await response.json();
  locations = data;
  showLocations(locations);
}

function showLocations(locationsToShow) {
  locationContainer.innerHTML = '';
  locationsToShow.forEach(location => {
    const locationCard = document.createElement('div');
    locationCard.classList.add('location-card');
    const locationHeading = document.createElement('h2');
    locationHeading.classList.add('location-heading');
    locationHeading.textContent = location.address;
    const locationDetails = document.createElement('p');
    locationDetails.classList.add('location-details');
    locationDetails.textContent = location.district;
    locationCard.appendChild(locationHeading);
    locationCard.appendChild(locationDetails);
    locationContainer.appendChild(locationCard);
  });
}

function filterLocations() {
  const addressInput = document.getElementById('address-input');
  const districtInput = document.getElementById('district-input');
  let filteredLocations = locations;
  if (addressInput.value !== '') {
    filteredLocations = filteredLocations.filter(location => location.address.toLowerCase().includes(addressInput.value.toLowerCase()));
  }
  if (districtInput.value !== '') {
    filteredLocations = filteredLocations.filter(location => location.district.toLowerCase().includes(districtInput.value.toLowerCase()));
  }
  showLocations(filteredLocations);
}

searchForm.addEventListener('submit', event => {
  event.preventDefault();
  filterLocations();
});

getLocations();

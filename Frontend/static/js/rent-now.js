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

// Submit Select Car form
selectCarForm.addEventListener('submit', (event) => {
  event.preventDefault();

  const car = selectCarForm.elements['car'].value;
  alert(`Car selected: ${car}`);
});
const form = document.getElementById('reservation-form');

form.addEventListener('reserve', (event) => {
    event.preventDefault();

    const formData = new FormData(form);
    const data = Object.fromEntries(formData.entries());

    console.log(data);
    
});

function clearForm() {
    document.getElementById('reservation-form').reset();
}
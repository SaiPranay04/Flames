document.getElementById('flamesForm').addEventListener('submit', function(event) {
    event.preventDefault();

    let name1 = document.getElementById('name1').value;
    let name2 = document.getElementById('name2').value;

    fetch('/flames', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ name1: name1, name2: name2 }),
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').innerHTML = `The relationship is: ${data.relation}`;
    })
    .catch(error => console.error('Error:', error));
});

document.getElementById('fetchDataBtn').addEventListener('click', function() {
    fetch('https://jsonplaceholder.typicode.com/posts/1')
        .then(response => response.json())
        .then(data => {
            const displayArea = document.getElementById('dataDisplay');
            displayArea.innerHTML = `<p>Title: ${data.title}</p><p>Body: ${data.body}</p>`;
        })
        .catch(error => console.error('Error fetching data:', error));
});

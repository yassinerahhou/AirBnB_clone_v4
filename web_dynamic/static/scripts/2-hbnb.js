document.addEventListener('DOMContentLoaded', function () {
  const apiUrl = 'http://0.0.0.0:5001/api/v1/status/';
  const apiStatusDiv = document.getElementById('api_status');

  // Make an HTTP GET request to the API status URL
  fetch(apiUrl)
    .then(response => response.json())
    .then(data => {
      if (data.status === 'OK') {
        apiStatusDiv.classList.add('available');
      } else {
        apiStatusDiv.classList.remove('available');
      }
    })
    .catch(error => {
      console.error('Error fetching API status:', error);
      apiStatusDiv.classList.remove('available');
    });
});

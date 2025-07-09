function fetchUptime() {
    fetch('/api/uptime')
        .then(response => response.json())
        .then(data => {
            document.getElementById('uptime').textContent = data.uptime;
        });
}

// Fetch uptime every 5 seconds
fetchUptime();
setInterval(fetchUptime, 5000);
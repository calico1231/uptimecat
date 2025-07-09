# uptimecat

## A Docker image to monitor and display the uptime of your Docker host server.

`uptimecat` is a simple Docker image built with Python, designed to help you easily view the uptime of the host system running your Docker containers. This project is currently in **beta** and under active development.

### Installation with Docker Compose

To quickly set up and run `uptimecat`, use the following `docker-compose.yml` configuration:

```yaml
version: '1.4' # Docker Compose file format version
services:
  uptimecat:
    image: ghcr.io/calico1231/uptimecat:main
    container_name: uptimecat
    ports:
      # Maps host port 8080 to container port 8080.
      # Ensure your uptimecat application inside the Docker image listens on port 8080.
      - "8080:8080" 
    # If uptimecat needs to store any persistent data (e.g., configuration, logs),
    # uncomment and adjust the volumes section below.
    # For a stateless application, this section can be omitted.
    # volumes:
    #   - ./data:/app/data # Example: Maps a 'data' folder in your current directory to '/app/data' inside the container
    restart: unless-stopped
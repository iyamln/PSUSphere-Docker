# PSUSphere Docker

PSUSphere is a Django-based student organization management system. It manages colleges, academic programs, students, organizations, and organization memberships.

## Features

- Manage colleges
- Manage academic programs
- Manage student organizations
- Manage student information
- Manage organization memberships
- Django Admin interface
- Search and filter records in the Admin interface

## Docker

This project includes a `Dockerfile`, `docker-compose.yml`, `.dockerignore`, and `requirements.txt` for building and running the Django application with Docker.

## Authors

- Aliah Molina
- Christian Dave Denzon

## Requirements

- Docker Desktop
- Git

## Project Structure

```text
PSUSphere/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .dockerignore
├── README.md
└── for_client/
    └── docker-compose.yml
```

## Running the Application from Source

1. Clone this repository.
2. Open a terminal in the project directory.
3. Build the Docker image and start the application:

```bash
docker compose up --build -d
```

4. Open the application in your browser:

```text
http://localhost:8000/
```

To check the container status:

```bash
docker compose ps
```

To view application logs:

```bash
docker compose logs -f
```

To stop the application:

```bash
docker compose down
```

## Running the Published Docker Image

The Docker image is published on Docker Hub as:

`iyamln/psusphere-django:latest`

1. Navigate to the `for_client` directory.
2. Create a local `.env` file containing the required environment variables. Use your own valid OAuth credentials if Google or GitHub login is needed. Never commit this file.
3. Pull the image and start the application:

```bash
docker compose pull
docker compose up -d
```

4. Open:

```text
http://localhost:8001/
```

To stop the client deployment:

```bash
docker compose down
```

## Environment Variables

The client deployment uses a local `.env` file for environment-specific settings, including OAuth credentials.

Keep `.env` files and real API keys, client secrets, and other credentials private. Do not upload them to GitHub or include them in public documentation.

OAuth providers may require their authorized redirect URIs to match the address and port used to access the application.

## Docker Files

- **Dockerfile:** Defines the environment and instructions for building the Django image.
- **docker-compose.yml:** Builds and runs the application from the project source.
- **requirements.txt:** Lists the Python dependencies.
- **.dockerignore:** Excludes unnecessary files from the Docker build context.
- **for_client/docker-compose.yml:** Runs the published Docker Hub image without building it from source.

## Notes

This project is intended for learning and demonstration. Before deploying it publicly, configure production settings, use a secure Django secret key, disable debug mode, and configure a production-ready web server and database.

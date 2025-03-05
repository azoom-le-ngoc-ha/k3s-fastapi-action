# FastAPI K3s Deployment

This project demonstrates how to deploy a FastAPI application to a K3s cluster using GitHub Actions and Docker.

## Project Structure

```
.github/
    workflows/
        deploy.yaml
.gitignore
Dockerfile
main.py
requirements.txt
```

## Requirements

- Docker
- Kubernetes (K3s)
- GitHub Actions

## Setup

1. Clone the repository:

```sh
git clone https://github.com/yourusername/yourrepository.git
cd yourrepository
```

2. Create a virtual environment and activate it:

```sh
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install the dependencies:

```sh
pip install -r requirements.txt
```

## Running the Application Locally

To run the FastAPI application locally, use the following command:

```sh
uvicorn main:app --host 0.0.0.0 --port 8000
```

The application will be available at `http://localhost:8000`.

## Docker

To build and run the Docker container locally:

1. Build the Docker image:

```sh
docker build -t fastapi-app .
```

2. Run the Docker container:

```sh
docker run -p 8000:8000 fastapi-app
```

## Deployment

This project uses GitHub Actions to deploy the FastAPI application to a K3s cluster.

### GitHub Actions Workflow

The GitHub Actions workflow is defined in `.github/workflows/deploy.yaml`. It performs the following steps:

1. Checkout the code.
2. Login to Docker Hub.
3. Build and push the Docker image.
4. SSH into the VPS and deploy the application using `kubectl`.

### Secrets

The following secrets need to be configured in your GitHub repository:

- `DOCKER_USERNAME`: Your Docker Hub username.
- `DOCKER_PASSWORD`: Your Docker Hub password.
- `VPS_HOST`: The hostname or IP address of your VPS.
- `VPS_USER`: The username to SSH into your VPS.
- `VPS_SSH_KEY`: The private SSH key to access your VPS.

## Endpoints

- `GET /`: Returns a welcome message.
- `GET /ping`: Returns a health check message.

## License

This project is licensed under the MIT License.

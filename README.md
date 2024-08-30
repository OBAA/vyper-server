# Vyper Server

A Dockerized Vyper compiler server that exposes a REST API for compiling Vyper smart contracts.

## Overview

The Vyper Server is a service that allows you to compile Vyper smart contracts through a REST API. It is built using Docker and provides an easy way to integrate Vyper compilation into your development workflow or other services.

## Features

- **Compile Vyper Contracts**: Expose a REST API endpoint to compile Vyper smart contracts.
- **Dockerized**: Easily deployable using Docker.
- **Customizable**: Configure the server with your preferred settings.

## Getting Started

### Prerequisites

- Docker: Make sure Docker is installed on your machine. [Install Docker](https://docs.docker.com/get-docker/).

### Building the Docker Image

1. Clone the repository:

    ```bash
    git clone https://gitea.svc.obaa.cloud/obaa/vyper-server.git
    cd vyper-server
    ```

2. Build the Docker image:

    ```bash
    docker build -t vyper-server .
    ```

### Running the Server

Run the Docker container:

```bash
docker run -d -p 8000:8000 vyper-server
```
The server will be available at http://localhost:8000/compile.

## API Usage

### Compile Vyper Smart Contract

**Endpoint:** `POST /compile`

**Request Body:**

```json
{
    "manifest": "ethpm/3",
    "name": "Vyper Smart Contract",
    "version": "1.0.0",
    "sources": {
        "contract.vy": {
            "content": "<contract-code-here>"
        }
    }
}
```
**Response:**

***On successful compilation:***

```json
{
    "output": "compiled contract output here"
}
```
***On error:***

```json
{
    "error": "error message here"
}
```

## Configuration

You can customize the server settings using environment variables:

`PORT:` The port on which the server listens (default: `8000`).

## Testing

To test the server locally, use the following commands:

1. Open the terminal in your project directory.

2. Run the tests:

```bash
npm test
```

## Contributing

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Push to the branch.
5. Create a new Pull Request.


# License

This project is licensed under the MIT License.

## Contact
For issues or feature requests, please open an issue on the GitHub repository.
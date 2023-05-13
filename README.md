# fastapi_test

## Description
Brief description of your project.

## Requirements
Make sure you have the following components installed:
- Docker
- Docker Compose

## Usage Instructions

1. Clone this repository to your local machine.
2. Navigate to the root directory of the project.
3. Start the services using Docker Compose or Make.

### Make commands list
- Display available commands and their descriptions
    ```sh make help```
- Start the database service 
    ```sh make start-db```
- Start the API development server 
    ```sh make start-api-dev```
- Start the database service 
    ```sh make start-all```
### Docker Compose commands list
- Start the database service 
    ```sh docker-compose up -d db```
- Start the API development server 
    ```sh cd app && uvicorn main:app --reload --port 5000```
- Start the database service 
    ```sh docker-compose up --build```
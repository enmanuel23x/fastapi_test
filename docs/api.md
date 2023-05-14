## API Routes

### API Documentation
- **URL:** `/docs`
- **Method:** GET
- **Description:** Access the documentation for the Task API.
- **Response:*** Interactive API documentation with details of all available routes and request/response schemas.

### Retrieve All Tasks
- **URL:** `/tasks`
- **Method:** GET
- **Description:** Retrieves all tasks.
- **Response:** List of tasks.

### Retrieve a Task
- **URL:** `/tasks/{task_id}`
- **Method:** GET
- **Description:** Retrieves a specific task.
- **Response:** Task details.

### Create a Task
- **URL:** `/tasks`
- **Method:** POST
- **Description:** Creates a new task.
- **Request Body:** Task data.
- **Response:**  Success message.

### Update a Task
- **URL:** `/tasks/{task_id}`
- **Method:** PUT
- **Description:** Updates an existing task.
- **Request Body:** Updated task data.
- **Response:** Success message.

### Delete a Task
- **URL:** `/tasks/{task_id}`
- **Method:** DELETE
- **Description:** Deletes a specific task.
- **Response:** Success message.
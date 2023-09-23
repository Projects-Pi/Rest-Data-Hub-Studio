Certainly! Here's a usage documentation for the routes in your Flask application for managing tasks, followed by `curl` examples for each route:

### Get All Tasks (`GET /tasks`)

- **Description:** This route allows you to retrieve a list of all tasks.

- **Response Codes:**
  - 200 (OK): If the list of tasks is successfully retrieved.
  - 500 (Internal Server Error): If an error occurs during retrieval.

### Get Task by ID (`GET /tasks/<int:task_id>`)

- **Description:** This route allows you to retrieve a specific task by its ID.

- **Parameters:**
  - `task_id` (integer): The ID of the task to be retrieved (specified in the URL).

- **Response Codes:**
  - 200 (OK): If the task is found and successfully retrieved.
  - 404 (Not Found): If the task specified by `task_id` is not found.
  - 500 (Internal Server Error): If an error occurs during retrieval.

### Create Task (`POST /tasks`)

- **Description:** This route allows you to create a new task.

- **Parameters:**
  - `title` (string): The title of the new task.
  - `completed` (boolean, optional): Whether the task is completed (default is `False`).

- **Request Example:**
  ```json
  {
    "title": "New Task",
    "completed": false
  }
  ```

- **Response Codes:**
  - 201 (Created): If the task is successfully created.
  - 500 (Internal Server Error): If an error occurs during task creation.

### Update Task by ID (`PUT /tasks/<int:task_id>`)

- **Description:** This route allows you to update an existing task by its ID.

- **Parameters:**
  - `task_id` (integer): The ID of the task to be updated (specified in the URL).
  - `title` (string): The new title for the task.
  - `completed` (boolean): Whether the task is completed.

- **Request Example:**
  ```json
  {
    "title": "Updated Task",
    "completed": true
  }
  ```

- **Response Codes:**
  - 200 (OK): If the task is found and successfully updated.
  - 404 (Not Found): If the task specified by `task_id` is not found.
  - 500 (Internal Server Error): If an error occurs during task update.

### Delete Task by ID (`DELETE /tasks/<int:task_id>`)

- **Description:** This route allows you to delete a task by its ID.

- **Parameters:**
  - `task_id` (integer): The ID of the task to be deleted (specified in the URL).

- **Response Codes:**
  - 200 (OK): If the task is found and successfully deleted.
  - 404 (Not Found): If the task specified by `task_id` is not found.
  - 500 (Internal Server Error): If an error occurs during task deletion.

### Curl Examples:

Here are `curl` examples for each of the task routes:

#### Get All Tasks (`GET /tasks`)

```bash
# Get a list of all tasks
curl -X GET http://your-api-url/tasks
```

#### Get Task by ID (`GET /tasks/<int:task_id>`)

```bash
# Get a specific task by ID
curl -X GET http://your-api-url/tasks/1
```

#### Create Task (`POST /tasks`)

```bash
# Create a new task
curl -X POST http://your-api-url/tasks -H "Content-Type: application/json" -d '{
  "title": "New Task",
  "completed": false
}'
```

#### Update Task by ID (`PUT /tasks/<int:task_id>`)

```bash
# Update an existing task by ID
curl -X PUT http://your-api-url/tasks/1 -H "Content-Type: application/json" -d '{
  "title": "Updated Task",
  "completed": true
}'
```

#### Delete Task by ID (`DELETE /tasks/<int:task_id>`)

```bash
# Delete a task by ID
curl -X DELETE http://your-api-url/tasks/1
```

Replace `http://your-api-url` with the actual URL of your Flask API, and provide the correct data in the requests according to your specific use case.

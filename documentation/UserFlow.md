Here's a usage documentation for the routes in the Flask application, followed by `curl` examples for each route:

### User Registration (`POST /register`)

- **Description:** This route allows the registration of a new user.

- **Parameters:**
  - `username` (string): The username for the new user.
  - `email` (string): The email address for the new user.
  - `password` (string): The password for the new user.

- **Request Example:**
  ```json
  {
    "username": "new_user",
    "email": "user@example.com",
    "password": "new_user_password"
  }
  ```

- **Response Codes:**
  - 201 (Created): If the user is successfully registered.
  - 400 (Bad Request): If any of the required parameters (username, email, password) are missing.
  - 409 (Conflict): If a user with the same email address already exists.
  - 500 (Internal Server Error): If an error occurs during registration.

### User Login (`POST /login`)

- **Description:** This route allows a user to log in.

- **Parameters:**
  - `email` (string): The email address of the user.
  - `password` (string): The password of the user.

- **Request Example:**
  ```json
  {
    "email": "user@example.com",
    "password": "user_password"
  }
  ```

- **Response Codes:**
  - 200 (OK): If the user is successfully logged in.
  - 400 (Bad Request): If any of the required parameters (email, password) are missing.
  - 401 (Unauthorized): If the provided email or password is incorrect.
  - 403 (Forbidden): If the user is not approved (user_status is not 'active').
  - 500 (Internal Server Error): If an error occurs during login.

### Get All Users (`GET /`)

- **Description:** This route allows an admin to retrieve a list of all user entities.

- **Parameters:**
  - `admin_id` (integer): The ID of the admin making the request.
  - `admin_password` (string): The password of the admin making the request.

- **Response Codes:**
  - 200 (OK): If the list of user entities is successfully retrieved.
  - 401 (Unauthorized): If the provided `admin_password` is incorrect.
  - 404 (Not Found): If the admin specified by `admin_id` is not found.
  - 500 (Internal Server Error): If an error occurs during retrieval.

### Get User by ID (`GET /<int:id>`)

- **Description:** This route allows an admin to retrieve a user entity by ID.

- **Parameters:**
  - `admin_id` (integer): The ID of the admin making the request.
  - `admin_password` (string): The password of the admin making the request.
  - `id` (integer): The ID of the user to be retrieved (specified in the URL).

- **Response Codes:**
  - 200 (OK): If the user is found and successfully retrieved.
  - 401 (Unauthorized): If the provided `admin_password` is incorrect.
  - 404 (Not Found): If the admin specified by `admin_id` is not found or if the user specified by `id` is not found.
  - 500 (Internal Server Error): If an error occurs during retrieval.

### Update User (`PUT /<int:id>`)

- **Description:** This route allows an admin to update the details of a user.

- **Parameters:**
  - `admin_id` (integer): The ID of the admin making the request.
  - `admin_password` (string): The password of the admin making the request.
  - `id` (integer): The ID of the user to be updated (specified in the URL).
  - `username` (string, optional): The new username for the user.
  - `email` (string, optional): The new email address for the user.
  - `password` (string, optional): The new password for the user.

- **Request Example:**
  ```json
  {
    "username": "updated_user_username",
    "email": "updated_user@example.com",
    "password": "new_user_password"
  }
  ```

- **Response Codes:**
  - 200 (OK): If the user is found and successfully updated.
  - 401 (Unauthorized): If the provided `admin_password` is incorrect.
  - 404 (Not Found): If the admin specified by `admin_id` is not found or if the user specified by `id` is not found.
  - 500 (Internal Server Error): If an error occurs during the update.

### Delete User (`DELETE /<int:id>`)

- **Description:** This route allows an admin to delete a user.

- **Parameters:**
  - `admin_id` (integer): The ID of the admin making the request.
  - `admin_password` (string): The password of the admin making the request.
  - `id` (integer): The ID of the user to be deleted (specified in the URL).

- **Response Codes:**
  - 200 (OK): If the user is found and successfully deleted.
  - 401 (Unauthorized): If the provided `admin_password` is incorrect.
  - 404 (Not Found): If the admin specified by `admin_id` is not found or if the user specified by `id` is not found.
  - 500 (Internal Server Error): If an error occurs during deletion.

### Curl Examples:

Here are `curl` examples for each of the user routes:

#### User Registration (`POST /register`)

```bash
# Register a new user
curl -X POST http://your-api-url/user/register -H "Content-Type: application/json" -d '{
  "username": "new_user",
  "email": "user@example.com",
  "password": "new_user_password"
}'
```

#### User Login (`POST /login`)

```bash
# Log in as a user
curl -X POST http://your-api-url/user/login -H "Content-Type: application/json" -d '{
  "email": "user@example.com",
  "password": "user_password"
}'
```

#### Get All Users (`GET /`)

```bash
# Get a list of all user entities (admin authentication required)
curl -X GET http://your-api-url/user/ -H "Content-Type: application/json" -d '{
  "admin_id": 1,
  "admin_password": "admin_password"
}'
```

#### Get User by ID (`GET /<int:id>`)

```bash
# Get a specific user entity by ID (admin authentication required)
curl -X GET http://your-api-url/user/1 -H "Content-Type: application/json" -d '{
  "admin_id": 1,
  "admin_password": "admin_password"
}'
```

#### Update User (`PUT /<int:id>`)

```bash
# Update a user's details (admin authentication required)
curl -X PUT http://your-api-url/user/1 -H "Content-Type: application/json" -d '{
  "username": "updated_user_username",
  "email": "updated_user@example.com",
  "password": "new_user_password"
}'
```

#### Delete User (`DELETE /<int:id>`)

```bash
# Delete a user (admin authentication required)
curl -X DELETE http://your-api-url/user/1 -H "Content-Type: application/json" -d '{
  "admin_id": 1,
  "admin_password": "admin_password"
}'
```

Replace `http://your-api-url` with the actual URL of your Flask API, and provide the correct authentication and data in the requests according to your specific use case.

Here's a usage documentation for the provided routes in the Flask application:

### Admin Registration (`POST /register`)

- **Description:** This route allows the registration of a new admin user.

- **Parameters:**
  - `app_password` (string): A password required to access this registration route. It must match the predefined app password.

- **Request Example:**
  ```json
  {
    "app_password": "KQQbfA93uPdjgsUv",
    "username": "new_admin",
    "email": "admin@example.com",
    "password": "new_admin_password"
  }
  ```

- **Response Codes:**
  - 201 (Created): If the admin is successfully registered.
  - 401 (Unauthorized): If the provided `app_password` is incorrect.
  - 500 (Internal Server Error): If an error occurs during registration.

### Assign Role to Entity (`POST /assign_role`)

- **Description:** This route allows assigning a role to an entity (e.g., user or admin).

- **Parameters:**
  - `admin_id` (integer): The ID of the admin performing the role assignment.
  - `admin_password` (string): The password of the admin performing the role assignment.
  - `entity_id` (integer): The ID of the entity (user or admin) to which the role is being assigned.
  - `role_name` (string): The name of the role being assigned.

- **Request Example:**
  ```json
  {
    "admin_id": 1,
    "admin_password": "admin_password",
    "entity_id": 2,
    "role_name": "editor"
  }
  ```

- **Response Codes:**
  - 200 (OK): If the role is successfully assigned.
  - 400 (Bad Request): If `entity_id` is missing or invalid.
  - 401 (Unauthorized): If the provided `admin_password` is incorrect.
  - 404 (Not Found): If the admin or role specified is not found.
  - 500 (Internal Server Error): If an error occurs during role assignment.

### Update Admin (`PUT /update/<int:id>`)

- **Description:** This route allows updating the details of an admin user.

- **Parameters:**
  - `id` (integer): The ID of the admin to be updated (specified in the URL).
  - `username` (string, optional): The new username for the admin.
  - `email` (string, optional): The new email address for the admin.
  - `password` (string, optional): The new password for the admin.

- **Request Example:**
  ```json
  {
    "username": "updated_admin_username",
    "email": "updated_admin@example.com",
    "password": "new_admin_password"
  }
  ```

- **Response Codes:**
  - 200 (OK): If the admin is successfully updated.
  - 404 (Not Found): If the admin specified by the `id` is not found.
  - 500 (Internal Server Error): If an error occurs during the update.

### Delete Admin (`DELETE /delete/<int:id>`)

- **Description:** This route allows deleting an admin user.

- **Parameters:**
  - `id` (integer): The ID of the admin to be deleted (specified in the URL).

- **Response Codes:**
  - 200 (OK): If the admin is successfully deleted.
  - 404 (Not Found): If the admin specified by the `id` is not found.
  - 500 (Internal Server Error): If an error occurs during deletion.

### List Admins (`GET /list_admins`)

- **Description:** This route allows retrieving a list of all admin users.

- **Parameters:**
  - `admin_id` (integer): The ID of the admin making the request.
  - `admin_password` (string): The password of the admin making the request.

- **Response Codes:**
  - 200 (OK): If the list of admin users is successfully retrieved.
  - 401 (Unauthorized): If the provided `admin_password` is incorrect.
  - 404 (Not Found): If the admin specified by `admin_id` is not found.
  - 500 (Internal Server Error): If an error occurs during retrieval.

### List Users (`GET /list_users`)

- **Description:** This route allows retrieving a list of all user entities.

- **Parameters:**
  - `admin_id` (integer): The ID of the admin making the request.
  - `admin_password` (string): The password of the admin making the request.

- **Response Codes:**
  - 200 (OK): If the list of user entities is successfully retrieved.
  - 401 (Unauthorized): If the provided `admin_password` is incorrect.
  - 404 (Not Found): If the admin specified by `admin_id` is not found.
  - 500 (Internal Server Error): If an error occurs during retrieval.

### Approve User (`POST /approve_user/<int:user_id>`)

- **Description:** This route allows approving a user entity, changing its status to 'active.'

- **Parameters:**
  - `admin_id` (integer): The ID of the admin performing the approval.
  - `admin_password` (string): The password of the admin performing the approval.
  - `user_id` (integer): The ID of the user to be approved (specified in the URL).

- **Response Codes:**
  - 200 (OK): If the user is successfully approved.
  - 401 (Unauthorized): If the provided `admin_password` is incorrect.
  - 404 (Not Found): If the user specified by `user_id` is not found.
  - 500 (Internal Server Error): If an error occurs during approval.

### Revoke User (`POST /revoke_user/<int:user_id>`)

- **Description:** This route allows revoking a user entity, changing its status to 'revoked.'

- **Parameters:**
  - `admin_id` (integer): The ID of the admin performing the revocation.
  - `admin_password` (string): The password of the admin performing the revocation.
  - `user_id` (integer): The ID of the user to be revoked (specified in the URL).

- **Response Codes:**
  - 200 (OK): If the user is successfully revoked.
  - 401 (Unauthorized): If the provided `admin_password` is incorrect.
  - 404 (Not Found): If the user specified by `user_id` is not found.
  - 500 (Internal Server Error): If an error occurs during revocation.

Please ensure that you provide the necessary authentication and data in your requests to these routes as specified in the documentation.



Here are step-by-step `curl` examples for each of the provided routes, along with the necessary authentication and data in the requests.

Please note that you should replace the placeholders with actual values as needed.

#### Admin Registration (`POST /register`)

```bash
# Register a new admin user
curl -X POST http://your-api-url/admin/register -H "Content-Type: application/json" -d '{
  "app_password": "KQQbfA93uPdjgsUv",
  "username": "new_admin",
  "email": "admin@example.com",
  "password": "new_admin_password"
}'
```

#### Assign Role to Entity (`POST /assign_role`)

```bash
# Assign a role to an entity
curl -X POST http://your-api-url/admin/assign_role -H "Content-Type: application/json" -d '{
  "admin_id": 1,
  "admin_password": "admin_password",
  "entity_id": 2,
  "role_name": "editor"
}'
```

#### Update Admin (`PUT /update/<int:id>`)

```bash
# Update an admin's details
curl -X PUT http://your-api-url/admin/update/1 -H "Content-Type: application/json" -d '{
  "username": "updated_admin_username",
  "email": "updated_admin@example.com",
  "password": "new_admin_password"
}'
```

#### Delete Admin (`DELETE /delete/<int:id>`)

```bash
# Delete an admin user
curl -X DELETE http://your-api-url/admin/delete/1
```

#### List Admins (`GET /list_admins`)

```bash
# List all admin users
curl -X GET http://your-api-url/admin/list_admins -H "Content-Type: application/json" -d '{
  "admin_id": 1,
  "admin_password": "admin_password"
}'
```

#### List Users (`GET /list_users`)

```bash
# List all user entities
curl -X GET http://your-api-url/admin/list_users -H "Content-Type: application/json" -d '{
  "admin_id": 1,
  "admin_password": "admin_password"
}'
```

#### Approve User (`POST /approve_user/<int:user_id>`)

```bash
# Approve a user
curl -X POST http://your-api-url/admin/approve_user/2 -H "Content-Type: application/json" -d '{
  "admin_id": 1,
  "admin_password": "admin_password"
}'
```

#### Revoke User (`POST /revoke_user/<int:user_id>`)

```bash
# Revoke a user
curl -X POST http://your-api-url/admin/revoke_user/2 -H "Content-Type: application/json" -d '{
  "admin_id": 1,
  "admin_password": "admin_password"
}'
```

Make sure to replace `http://your-api-url` with the actual URL of your Flask API, and provide the correct authentication and data in the requests according to your specific use case.

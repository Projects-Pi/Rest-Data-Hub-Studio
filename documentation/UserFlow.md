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

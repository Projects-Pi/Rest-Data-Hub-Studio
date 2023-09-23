Here's a usage documentation for the routes in your Node.js Express application for managing labs, followed by `curl` examples for each route:

### Create Lab (`POST /labs`)

- **Description:** This route allows you to create a new lab.

- **Request Body:**
  - `lab_id` (string): The unique identifier for the lab (required).
  - `lab_name` (string): The name of the lab.
  - `location` (string): The location of the lab.
  - `lab_head` (string): The head or director of the lab.
  - `lab_description` (string): A description of the lab.
  - `lab_website` (string): The website of the lab.
  - `established_year` (number): The year the lab was established.

- **Request Example:**
  ```json
  {
    "lab_id": "LAB001",
    "lab_name": "Lab A",
    "location": "City X",
    "lab_head": "Dr. John Doe",
    "lab_description": "Research lab in biology",
    "lab_website": "https://labwebsite.com",
    "established_year": 2000
  }
  ```

- **Response Codes:**
  - 201 (Created): If the lab is successfully created.
  - 400 (Bad Request): If there is an issue with the request body.
  - 500 (Internal Server Error): If an error occurs during lab creation.

### Get All Labs (`GET /labs`)

- **Description:** This route allows you to retrieve a list of all labs.

- **Response Codes:**
  - 200 (OK): If the list of labs is successfully retrieved.
  - 500 (Internal Server Error): If an error occurs during retrieval.

### Get Lab by ID (`GET /labs/:labId`)

- **Description:** This route allows you to retrieve a specific lab by its ID.

- **Parameters:**
  - `labId` (string): The unique identifier of the lab (specified in the URL).

- **Response Codes:**
  - 200 (OK): If the lab is found and successfully retrieved.
  - 404 (Not Found): If the lab specified by `labId` is not found.
  - 500 (Internal Server Error): If an error occurs during retrieval.

### Update Lab by ID (`PUT /labs/:labId`)

- **Description:** This route allows you to update an existing lab by its ID.

- **Parameters:**
  - `labId` (string): The unique identifier of the lab (specified in the URL).

- **Request Body:** (similar to the create request body)

- **Request Example:**
  ```json
  {
    "lab_name": "Updated Lab A",
    "lab_description": "Updated description"
  }
  ```

- **Response Codes:**
  - 200 (OK): If the lab is found and successfully updated.
  - 404 (Not Found): If the lab specified by `labId` is not found.
  - 500 (Internal Server Error): If an error occurs during lab update.

### Delete Lab by ID (`DELETE /labs/:labId`)

- **Description:** This route allows you to delete a lab by its ID.

- **Parameters:**
  - `labId` (string): The unique identifier of the lab (specified in the URL).

- **Response Codes:**
  - 200 (OK): If the lab is found and successfully deleted.
  - 404 (Not Found): If the lab specified by `labId` is not found.
  - 500 (Internal Server Error): If an error occurs during lab deletion.

### Curl Examples:

Here are `curl` examples for each of the lab routes:

#### Create Lab (`POST /labs`)

```bash
# Create a new lab
curl -X POST http://your-api-url/labs -H "Content-Type: application/json" -d '{
  "lab_id": "LAB001",
  "lab_name": "Lab A",
  "location": "City X",
  "lab_head": "Dr. John Doe",
  "lab_description": "Research lab in biology",
  "lab_website": "https://labwebsite.com",
  "established_year": 2000
}'
```

#### Get All Labs (`GET /labs`)

```bash
# Get a list of all labs
curl -X GET http://your-api-url/labs
```

#### Get Lab by ID (`GET /labs/:labId`)

```bash
# Get a specific lab by ID
curl -X GET http://your-api-url/labs/LAB001
```

#### Update Lab by ID (`PUT /labs/:labId`)

```bash
# Update an existing lab by ID
curl -X PUT http://your-api-url/labs/LAB001 -H "Content-Type: application/json" -d '{
  "lab_name": "Updated Lab A",
  "lab_description": "Updated description"
}'
```

#### Delete Lab by ID (`DELETE /labs/:labId`)

```bash
# Delete a lab by ID
curl -X DELETE http://your-api-url/labs/LAB001
```

Replace `http://your-api-url` with the actual URL of your Node.js Express API, and provide the correct data in the requests according to your specific use case.

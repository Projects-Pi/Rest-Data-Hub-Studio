Here's the usage documentation for the routes in the Node.js Express application for managing researcher records, followed by `curl` examples for each route:

### Create a New Researcher (`POST /researchers`)

- **Description:** This route allows you to create a new researcher record.

- **Request Body:**
  - `researcher_id` (string): The unique identifier for the researcher (required).
  - `researcher_name` (string): The name of the researcher.
  - `affiliation` (string): The affiliation of the researcher.
  - `research_interests` (array of strings): Research interests of the researcher.
  - `email` (string): The email address of the researcher.
  - `phone_number` (string): The phone number of the researcher.
  - `research_publications` (array of strings): List of research publications by the researcher.

- **Request Example:**
  ```json
  {
    "researcher_id": "RES001",
    "researcher_name": "Dr. Jane Smith",
    "affiliation": "ABC University",
    "research_interests": ["Machine Learning", "Data Science"],
    "email": "jane.smith@example.com",
    "phone_number": "123-456-7890",
    "research_publications": ["Publication 1", "Publication 2"]
  }
  ```

- **Response Codes:**
  - 201 (Created): If the researcher record is successfully created.
  - 400 (Bad Request): If there is an issue with the request body.
  - 500 (Internal Server Error): If an error occurs during record creation.

### Get All Researchers (`GET /researchers`)

- **Description:** This route allows you to retrieve a list of all researcher records.

- **Response Codes:**
  - 200 (OK): If the list of researcher records is successfully retrieved.
  - 500 (Internal Server Error): If an error occurs during retrieval.

### Get Researcher by ID (`GET /researchers/:researcherId`)

- **Description:** This route allows you to retrieve a specific researcher record by its ID.

- **Parameters:**
  - `researcherId` (string): The unique identifier of the researcher (specified in the URL).

- **Response Codes:**
  - 200 (OK): If the researcher record is found and successfully retrieved.
  - 404 (Not Found): If the researcher record specified by `researcherId` is not found.
  - 500 (Internal Server Error): If an error occurs during retrieval.

### Update Researcher by ID (`PUT /researchers/:researcherId`)

- **Description:** This route allows you to update an existing researcher record by its ID.

- **Parameters:**
  - `researcherId` (string): The unique identifier of the researcher (specified in the URL).

- **Request Body:** (similar to the create request body)

- **Request Example:**
  ```json
  {
    "researcher_name": "Updated Dr. Jane Smith",
    "affiliation": "XYZ University",
    "research_interests": ["AI", "Deep Learning"],
    "email": "jane.updated@example.com",
    "phone_number": "987-654-3210",
    "research_publications": ["Updated Publication 1", "Publication 3"]
  }
  ```

- **Response Codes:**
  - 200 (OK): If the researcher record is found and successfully updated.
  - 404 (Not Found): If the researcher record specified by `researcherId` is not found.
  - 500 (Internal Server Error): If an error occurs during record update.

### Delete Researcher by ID (`DELETE /researchers/:researcherId`)

- **Description:** This route allows you to delete a researcher record by its ID.

- **Parameters:**
  - `researcherId` (string): The unique identifier of the researcher (specified in the URL).

- **Response Codes:**
  - 200 (OK): If the researcher record is found and successfully deleted.
  - 404 (Not Found): If the researcher record specified by `researcherId` is not found.
  - 500 (Internal Server Error): If an error occurs during record deletion.

### Curl Examples:

Here are `curl` examples for each of the researcher record routes:

#### Create a New Researcher (`POST /researchers`)

```bash
# Create a new researcher record
curl -X POST http://your-api-url/researchers -H "Content-Type: application/json" -d '{
  "researcher_id": "RES001",
  "researcher_name": "Dr. Jane Smith",
  "affiliation": "ABC University",
  "research_interests": ["Machine Learning", "Data Science"],
  "email": "jane.smith@example.com",
  "phone_number": "123-456-7890",
  "research_publications": ["Publication 1", "Publication 2"]
}'
```

#### Get All Researchers (`GET /researchers`)

```bash
# Get a list of all researcher records
curl -X GET http://your-api-url/researchers
```

#### Get Researcher by ID (`GET /researchers/:researcherId`)

```bash
# Get a specific researcher record by ID
curl -X GET http://your-api-url/researchers/RES001
```

#### Update Researcher by ID (`PUT /researchers/:researcherId`)

```bash
# Update an existing researcher record by ID
curl -X PUT http://your-api-url/researchers/RES001 -H "Content-Type: application/json" -d '{
  "researcher_name": "Updated Dr. Jane Smith",
  "affiliation": "XYZ University",
  "research_interests": ["AI", "Deep Learning"],
  "email": "jane.updated@example.com",
  "phone_number": "987-654-3210",
  "research_publications": ["Updated Publication 1", "Publication 3"]
}'
```

#### Delete Researcher by ID (`DELETE /researchers/:researcherId`)

```bash
# Delete a researcher record by ID
curl -X DELETE http://your-api-url/researchers/RES001
```

Replace `http://your-api-url` with the actual URL of your Node.js Express API, and provide the correct data in the requests according to your specific use case.

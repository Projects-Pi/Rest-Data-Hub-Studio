Here's the usage documentation for the routes in your Node.js Express application for managing medical history records, followed by `curl` examples for each route:

### Create Medical History Record (`POST /medical-histories`)

- **Description:** This route allows you to create a new medical history record.

- **Request Body:**
  - `history_id` (string): The unique identifier for the medical history record (required).
  - `medical_condition` (string): Description of the medical condition.
  - `medications` (array of strings): List of medications.
  - `allergies` (array of strings): List of allergies.
  - `surgical_history` (string): Description of surgical history.
  - `family_medical_history` (string): Description of family medical history.

- **Request Example:**
  ```json
  {
    "history_id": "HIST001",
    "medical_condition": "Hypertension",
    "medications": ["Medication A", "Medication B"],
    "allergies": ["Allergy X", "Allergy Y"],
    "surgical_history": "Appendectomy in 2010",
    "family_medical_history": "Heart disease"
  }
  ```

- **Response Codes:**
  - 201 (Created): If the medical history record is successfully created.
  - 400 (Bad Request): If there is an issue with the request body.
  - 500 (Internal Server Error): If an error occurs during record creation.

### Get All Medical History Records (`GET /medical-histories`)

- **Description:** This route allows you to retrieve a list of all medical history records.

- **Response Codes:**
  - 200 (OK): If the list of medical history records is successfully retrieved.
  - 500 (Internal Server Error): If an error occurs during retrieval.

### Get Medical History Record by ID (`GET /medical-histories/:historyId`)

- **Description:** This route allows you to retrieve a specific medical history record by its ID.

- **Parameters:**
  - `historyId` (string): The unique identifier of the medical history record (specified in the URL).

- **Response Codes:**
  - 200 (OK): If the medical history record is found and successfully retrieved.
  - 404 (Not Found): If the medical history record specified by `historyId` is not found.
  - 500 (Internal Server Error): If an error occurs during retrieval.

### Update Medical History Record by ID (`PUT /medical-histories/:historyId`)

- **Description:** This route allows you to update an existing medical history record by its ID.

- **Parameters:**
  - `historyId` (string): The unique identifier of the medical history record (specified in the URL).

- **Request Body:** (similar to the create request body)

- **Request Example:**
  ```json
  {
    "medical_condition": "Updated Hypertension",
    "medications": ["Updated Medication A"],
    "allergies": ["Updated Allergy X", "Updated Allergy Y"],
    "surgical_history": "Updated appendectomy in 2020",
    "family_medical_history": "Updated heart disease"
  }
  ```

- **Response Codes:**
  - 200 (OK): If the medical history record is found and successfully updated.
  - 404 (Not Found): If the medical history record specified by `historyId` is not found.
  - 500 (Internal Server Error): If an error occurs during record update.

### Delete Medical History Record by ID (`DELETE /medical-histories/:historyId`)

- **Description:** This route allows you to delete a medical history record by its ID.

- **Parameters:**
  - `historyId` (string): The unique identifier of the medical history record (specified in the URL).

- **Response Codes:**
  - 200 (OK): If the medical history record is found and successfully deleted.
  - 404 (Not Found): If the medical history record specified by `historyId` is not found.
  - 500 (Internal Server Error): If an error occurs during record deletion.

### Curl Examples:

Here are `curl` examples for each of the medical history record routes:

#### Create Medical History Record (`POST /medical-histories`)

```bash
# Create a new medical history record
curl -X POST http://your-api-url/medical-histories -H "Content-Type: application/json" -d '{
  "history_id": "HIST001",
  "medical_condition": "Hypertension",
  "medications": ["Medication A", "Medication B"],
  "allergies": ["Allergy X", "Allergy Y"],
  "surgical_history": "Appendectomy in 2010",
  "family_medical_history": "Heart disease"
}'
```

#### Get All Medical History Records (`GET /medical-histories`)

```bash
# Get a list of all medical history records
curl -X GET http://your-api-url/medical-histories
```

#### Get Medical History Record by ID (`GET /medical-histories/:historyId`)

```bash
# Get a specific medical history record by ID
curl -X GET http://your-api-url/medical-histories/HIST001
```

#### Update Medical History Record by ID (`PUT /medical-histories/:historyId`)

```bash
# Update an existing medical history record by ID
curl -X PUT http://your-api-url/medical-histories/HIST001 -H "Content-Type: application/json" -d '{
  "medical_condition": "Updated Hypertension",
  "medications": ["Updated Medication A"],
  "allergies": ["Updated Allergy X", "Updated Allergy Y"],
  "surgical_history": "Updated appendectomy in 2020",
  "family_medical_history": "Updated heart disease"
}'
```

#### Delete Medical History Record by ID (`DELETE /medical-histories/:historyId`)

```bash
# Delete a medical history record by ID
curl -X DELETE http://your-api-url/medical-histories/HIST001
```

Replace `http://your-api-url` with the actual URL of your Node.js Express API, and provide the correct data in the requests according to your specific use case.

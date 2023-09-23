Here's the usage documentation for the routes in your Node.js Express application for managing patient records, followed by `curl` examples for each route:

### Create a New Patient (`POST /patients`)

- **Description:** This route allows you to create a new patient record.

- **Request Body:**
  - `patient_id` (string): The unique identifier for the patient (required).
  - `patient_name` (string): The name of the patient.
  - `birthdate` (date): The birthdate of the patient.
  - `gender` (string): The gender of the patient.
  - `contact_info` (object):
    - `phone` (string): The phone number of the patient.
    - `address` (string): The address of the patient.
  - `blood_type` (string): The blood type of the patient.
  - `emergency_contact` (string): The emergency contact information for the patient.

- **Request Example:**
  ```json
  {
    "patient_id": "PAT001",
    "patient_name": "John Doe",
    "birthdate": "1990-01-15",
    "gender": "Male",
    "contact_info": {
      "phone": "123-456-7890",
      "address": "123 Main Street"
    },
    "blood_type": "O+",
    "emergency_contact": "Jane Doe (Spouse)"
  }
  ```

- **Response Codes:**
  - 201 (Created): If the patient record is successfully created.
  - 400 (Bad Request): If there is an issue with the request body.
  - 500 (Internal Server Error): If an error occurs during record creation.

### Get All Patients (`GET /patients`)

- **Description:** This route allows you to retrieve a list of all patient records.

- **Response Codes:**
  - 200 (OK): If the list of patient records is successfully retrieved.
  - 500 (Internal Server Error): If an error occurs during retrieval.

### Get Patient by ID (`GET /patients/:patientId`)

- **Description:** This route allows you to retrieve a specific patient record by its ID.

- **Parameters:**
  - `patientId` (string): The unique identifier of the patient (specified in the URL).

- **Response Codes:**
  - 200 (OK): If the patient record is found and successfully retrieved.
  - 404 (Not Found): If the patient record specified by `patientId` is not found.
  - 500 (Internal Server Error): If an error occurs during retrieval.

### Update Patient by ID (`PUT /patients/:patientId`)

- **Description:** This route allows you to update an existing patient record by its ID.

- **Parameters:**
  - `patientId` (string): The unique identifier of the patient (specified in the URL).

- **Request Body:** (similar to the create request body)

- **Request Example:**
  ```json
  {
    "patient_name": "Updated John Doe",
    "birthdate": "1990-01-15",
    "gender": "Male",
    "contact_info": {
      "phone": "987-654-3210",
      "address": "456 Elm Street"
    },
    "blood_type": "A-",
    "emergency_contact": "Jane Doe (Spouse)"
  }
  ```

- **Response Codes:**
  - 200 (OK): If the patient record is found and successfully updated.
  - 404 (Not Found): If the patient record specified by `patientId` is not found.
  - 500 (Internal Server Error): If an error occurs during record update.

### Delete Patient by ID (`DELETE /patients/:patientId`)

- **Description:** This route allows you to delete a patient record by its ID.

- **Parameters:**
  - `patientId` (string): The unique identifier of the patient (specified in the URL).

- **Response Codes:**
  - 200 (OK): If the patient record is found and successfully deleted.
  - 404 (Not Found): If the patient record specified by `patientId` is not found.
  - 500 (Internal Server Error): If an error occurs during record deletion.

### Curl Examples:

Here are `curl` examples for each of the patient record routes:

#### Create a New Patient (`POST /patients`)

```bash
# Create a new patient record
curl -X POST http://your-api-url/patients -H "Content-Type: application/json" -d '{
  "patient_id": "PAT001",
  "patient_name": "John Doe",
  "birthdate": "1990-01-15",
  "gender": "Male",
  "contact_info": {
    "phone": "123-456-7890",
    "address": "123 Main Street"
  },
  "blood_type": "O+",
  "emergency_contact": "Jane Doe (Spouse)"
}'
```

#### Get All Patients (`GET /patients`)

```bash
# Get a list of all patient records
curl -X GET http://your-api-url/patients
```

#### Get Patient by ID (`GET /patients/:patientId`)

```bash
# Get a specific patient record by ID
curl -X GET http://your-api-url/patients/PAT001
```

#### Update Patient by ID (`PUT /patients/:patientId`)

```bash
# Update an existing patient record by ID
curl -X PUT http://your-api-url/patients/PAT001 -H "Content-Type: application/json" -d '{
  "patient_name": "Updated John Doe",
  "birthdate": "1990-01-15",
  "gender": "Male",
  "contact_info": {
    "phone": "987-654-3210",
    "address": "456 Elm Street"
  },
  "blood_type": "A-",
  "emergency_contact": "Jane Doe (Spouse)"
}'
```

#### Delete Patient by ID (`DELETE /patients/:patientId`)

```bash
# Delete a patient record by ID
curl -X DELETE http://your-api-url/patients/PAT001
```

Replace `http://your-api-url` with the actual URL of your Node.js Express API, and provide the correct data in the requests according to your specific use case.

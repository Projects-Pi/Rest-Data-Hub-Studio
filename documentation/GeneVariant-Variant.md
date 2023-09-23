Here's the documentation for the routes in your Node.js Express application for managing variant records, along with `curl` examples for each route:

### Create a New Variant (`POST /variants`)

- **Description:** This route allows you to create a new variant record.

- **Request Body:**
  - `variant_id` (string): The unique identifier for the variant (required).
  - `variant_name` (string): The name of the variant.
  - `variant_type` (string): The type of the variant.
  - `location` (string): The location of the variant.
  - `allele_frequency` (number): The allele frequency of the variant.
  - `impact` (string): The impact of the variant.
  - `mutation_description` (string): A description of the variant mutation.
  - `dbSNP_id` (string): The dbSNP ID of the variant.

- **Request Example:**
  ```json
  {
    "variant_id": "VAR001",
    "variant_name": "Variant A",
    "variant_type": "SNP",
    "location": "Chromosome 1",
    "allele_frequency": 0.05,
    "impact": "Moderate",
    "mutation_description": "A single nucleotide change",
    "dbSNP_id": "rs123456"
  }
  ```

- **Response Codes:**
  - 201 (Created): If the variant record is successfully created.
  - 400 (Bad Request): If there is an issue with the request body.
  - 500 (Internal Server Error): If an error occurs during record creation.

### Get All Variants (`GET /variants`)

- **Description:** This route allows you to retrieve a list of all variant records.

- **Response Codes:**
  - 200 (OK): If the list of variant records is successfully retrieved.
  - 500 (Internal Server Error): If an error occurs during retrieval.

### Get Variant by ID (`GET /variants/:variantId`)

- **Description:** This route allows you to retrieve a specific variant record by its ID.

- **Parameters:**
  - `variantId` (string): The unique identifier of the variant (specified in the URL).

- **Response Codes:**
  - 200 (OK): If the variant record is found and successfully retrieved.
  - 404 (Not Found): If the variant record specified by `variantId` is not found.
  - 500 (Internal Server Error): If an error occurs during retrieval.

### Update Variant by ID (`PUT /variants/:variantId`)

- **Description:** This route allows you to update an existing variant record by its ID.

- **Parameters:**
  - `variantId` (string): The unique identifier of the variant (specified in the URL).

- **Request Body:** (similar to the create request body)

- **Request Example:**
  ```json
  {
    "variant_name": "Updated Variant A",
    "variant_type": "Indel",
    "location": "Chromosome 2",
    "allele_frequency": 0.1,
    "impact": "High",
    "mutation_description": "A deletion in the gene",
    "dbSNP_id": "rs654321"
  }
  ```

- **Response Codes:**
  - 200 (OK): If the variant record is found and successfully updated.
  - 404 (Not Found): If the variant record specified by `variantId` is not found.
  - 500 (Internal Server Error): If an error occurs during record update.

### Delete Variant by ID (`DELETE /variants/:variantId`)

- **Description:** This route allows you to delete a variant record by its ID.

- **Parameters:**
  - `variantId` (string): The unique identifier of the variant (specified in the URL).

- **Response Codes:**
  - 200 (OK): If the variant record is found and successfully deleted.
  - 404 (Not Found): If the variant record specified by `variantId` is not found.
  - 500 (Internal Server Error): If an error occurs during record deletion.

### Curl Examples:

Here are `curl` examples for each of the variant record routes:

#### Create a New Variant (`POST /variants`)

```bash
# Create a new variant record
curl -X POST http://your-api-url/variants -H "Content-Type: application/json" -d '{
  "variant_id": "VAR001",
  "variant_name": "Variant A",
  "variant_type": "SNP",
  "location": "Chromosome 1",
  "allele_frequency": 0.05,
  "impact": "Moderate",
  "mutation_description": "A single nucleotide change",
  "dbSNP_id": "rs123456"
}'
```

#### Get All Variants (`GET /variants`)

```bash
# Get a list of all variant records
curl -X GET http://your-api-url/variants
```

#### Get Variant by ID (`GET /variants/:variantId`)

```bash
# Get a specific variant record by ID
curl -X GET http://your-api-url/variants/VAR001
```

#### Update Variant by ID (`PUT /variants/:variantId`)

```bash
# Update an existing variant record by ID
curl -X PUT http://your-api-url/variants/VAR001 -H "Content-Type: application/json" -d '{
  "variant_name": "Updated Variant A",
  "variant_type": "Indel",
  "location": "Chromosome 2",
  "allele_frequency": 0.1,
  "impact": "High",
  "mutation_description": "A deletion in the gene",
  "dbSNP_id": "rs654321"
}'
```

#### Delete Variant by ID (`DELETE /variants/:variantId`)

```bash
# Delete a variant record by ID
curl -X DELETE http://your-api-url/variants/VAR001
```

Replace `http://your-api-url` with the actual URL of your Node.js Express API, and provide the correct data in the requests according to your specific use case.

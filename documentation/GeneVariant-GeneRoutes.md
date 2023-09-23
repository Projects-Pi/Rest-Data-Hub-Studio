Here's a usage documentation for the routes in your Node.js Express application for managing genes, followed by `curl` examples for each route:

### Create Gene (`POST /genes`)

- **Description:** This route allows you to create a new gene.

- **Request Body:**
  - `gene_id` (string): The unique identifier for the gene (required).
  - `gene_name` (string): The name of the gene.
  - `gene_symbol` (string): The symbol representing the gene.
  - `sequence` (string): The gene's DNA sequence.
  - `chromosomal_location` (string): The chromosomal location of the gene.
  - `gene_function` (string): The function or role of the gene.
  - `exon_count` (number): The number of exons in the gene.
  - `chromosome` (string): The chromosome on which the gene is located.

- **Request Example:**
  ```json
  {
    "gene_id": "GENE001",
    "gene_name": "Gene A",
    "gene_symbol": "GA",
    "sequence": "ATCG...",
    "chromosomal_location": "Xq12",
    "gene_function": "DNA replication",
    "exon_count": 5,
    "chromosome": "X"
  }
  ```

- **Response Codes:**
  - 201 (Created): If the gene is successfully created.
  - 400 (Bad Request): If there is an issue with the request body.
  - 500 (Internal Server Error): If an error occurs during gene creation.

### Get All Genes (`GET /genes`)

- **Description:** This route allows you to retrieve a list of all genes.

- **Response Codes:**
  - 200 (OK): If the list of genes is successfully retrieved.
  - 500 (Internal Server Error): If an error occurs during retrieval.

### Get Gene by ID (`GET /genes/:geneId`)

- **Description:** This route allows you to retrieve a specific gene by its ID.

- **Parameters:**
  - `geneId` (string): The unique identifier of the gene (specified in the URL).

- **Response Codes:**
  - 200 (OK): If the gene is found and successfully retrieved.
  - 404 (Not Found): If the gene specified by `geneId` is not found.
  - 500 (Internal Server Error): If an error occurs during retrieval.

### Update Gene by ID (`PUT /genes/:geneId`)

- **Description:** This route allows you to update an existing gene by its ID.

- **Parameters:**
  - `geneId` (string): The unique identifier of the gene (specified in the URL).

- **Request Body:** (similar to the create request body)

- **Request Example:**
  ```json
  {
    "gene_name": "Updated Gene A",
    "gene_function": "DNA repair"
  }
  ```

- **Response Codes:**
  - 200 (OK): If the gene is found and successfully updated.
  - 404 (Not Found): If the gene specified by `geneId` is not found.
  - 500 (Internal Server Error): If an error occurs during gene update.

### Delete Gene by ID (`DELETE /genes/:geneId`)

- **Description:** This route allows you to delete a gene by its ID.

- **Parameters:**
  - `geneId` (string): The unique identifier of the gene (specified in the URL).

- **Response Codes:**
  - 200 (OK): If the gene is found and successfully deleted.
  - 404 (Not Found): If the gene specified by `geneId` is not found.
  - 500 (Internal Server Error): If an error occurs during gene deletion.

### Curl Examples:

Here are `curl` examples for each of the gene routes:

#### Create Gene (`POST /genes`)

```bash
# Create a new gene
curl -X POST http://your-api-url/genes -H "Content-Type: application/json" -d '{
  "gene_id": "GENE001",
  "gene_name": "Gene A",
  "gene_symbol": "GA",
  "sequence": "ATCG...",
  "chromosomal_location": "Xq12",
  "gene_function": "DNA replication",
  "exon_count": 5,
  "chromosome": "X"
}'
```

#### Get All Genes (`GET /genes`)

```bash
# Get a list of all genes
curl -X GET http://your-api-url/genes
```

#### Get Gene by ID (`GET /genes/:geneId`)

```bash
# Get a specific gene by ID
curl -X GET http://your-api-url/genes/GENE001
```

#### Update Gene by ID (`PUT /genes/:geneId`)

```bash
# Update an existing gene by ID
curl -X PUT http://your-api-url/genes/GENE001 -H "Content-Type: application/json" -d '{
  "gene_name": "Updated Gene A",
  "gene_function": "DNA repair"
}'
```

#### Delete Gene by ID (`DELETE /genes/:geneId`)

```bash
# Delete a gene by ID
curl -X DELETE http://your-api-url/genes/GENE001
```

Replace `http://your-api-url` with the actual URL of your Node.js Express API, and provide the correct data in the requests according to your specific use case.

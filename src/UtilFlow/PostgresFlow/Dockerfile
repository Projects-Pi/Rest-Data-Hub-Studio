# Use the official PostgreSQL image as the base image
FROM postgres:12

# Copy the .env file into the container
COPY .env /docker-entrypoint-initdb.d/.env

# Expose the PostgreSQL port
EXPOSE 5432
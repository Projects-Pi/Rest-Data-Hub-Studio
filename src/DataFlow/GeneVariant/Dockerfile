# Use an official Node.js runtime as the base image
FROM node:14

# Create and set the working directory
WORKDIR /api/v1/app

# Copy the entire project directory into the container
COPY /api /api

# Install the required Python packages
RUN npm install

# Expose the port your Flask application will run on
EXPOSE 4005

CMD ["node", "app.js"]


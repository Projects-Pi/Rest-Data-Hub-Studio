require('dotenv').config(); // Load environment variables from .env file

const env = {
  PORT: process.env.PORT || 4005, // Example: Set the default port to 3000
  MONGODB_URI: process.env.MONGODB_URI || 'mongodb://localhost/your-database-name',
  // Add more environment variables as needed
};

module.exports = env;

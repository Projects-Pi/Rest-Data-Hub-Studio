const mongoose = require('mongoose');

const connectDB = async () => {
  try {
    const connection = await mongoose.connect("mongodb+srv://visio:KQQbfA93uPdjgsUv@cluster0.gwyv9zd.mongodb.net/PharmaData", {
      useNewUrlParser: true,
      useUnifiedTopology: true,
    });
    console.log(`Connected to MongoDB: ${connection.connection.host}`);
  } catch (error) {
    console.error(`MongoDB Connection Error: ${error.message}`);
    process.exit(1); // Exit the application if unable to connect to MongoDB
  }
};

module.exports = connectDB;

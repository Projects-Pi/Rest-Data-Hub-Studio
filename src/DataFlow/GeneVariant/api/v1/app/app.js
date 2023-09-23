const express = require('express');
const connectDB = require('./config/database');
const env = require('./config/env');
const app = express();

// Connect to MongoDB
connectDB();

// Middleware
app.use(express.json());

// Routes
app.use('/api/gene', require('./routes/geneRoutes'));
app.use('/api/variant', require('./routes/variantRoutes'));
app.use('/api/researcher', require('./routes/researcherRoutes'));
app.use('/api/lab', require('./routes/labRoutes'));
app.use('/api/patient', require('./routes/patientRoutes'));
app.use('/api/medical-history', require('./routes/medicalHistoryRoutes'));
app.use('/api/clinical-trial', require('./routes/clinicalTrialRoutes'));

// Start the server
const PORT = process.env.PORT || 4005;
const HOST = '0.0.0.0'; // Listen on all available network interfaces

app.listen(PORT, HOST, () => {
  console.log(`Server is running on ${HOST}:${PORT}`);
});

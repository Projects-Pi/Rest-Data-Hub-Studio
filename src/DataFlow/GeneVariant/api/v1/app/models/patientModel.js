const mongoose = require('mongoose');

const patientSchema = new mongoose.Schema({
  patient_id: {
    type: String,
    unique: true,
    required: true,
  },
  patient_name: String,
  birthdate: Date,
  gender: String,
  contact_info: {
    phone: String,
    address: String,
  },
  blood_type: String,
  emergency_contact: String
});

module.exports = mongoose.model('Patient', patientSchema);

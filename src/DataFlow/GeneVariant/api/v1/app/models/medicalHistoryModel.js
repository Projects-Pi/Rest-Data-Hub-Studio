const mongoose = require('mongoose');

const medicalHistorySchema = new mongoose.Schema({
  history_id: {
    type: String,
    unique: true,
    required: true,
  },
  medical_condition: String,
  medications: [String],
  allergies: [String],
  surgical_history: String,
  family_medical_history: String
});

module.exports = mongoose.model('MedicalHistory', medicalHistorySchema);

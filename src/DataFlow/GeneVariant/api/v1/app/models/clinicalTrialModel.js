const mongoose = require('mongoose');

const clinicalTrialSchema = new mongoose.Schema({
  trial_id: {
    type: String,
    unique: true,
    required: true,
  },
  trial_name: String,
  principal_investigator: String,
  trial_description: String,
  start_date: Date,
  end_date: Date,
  enrollment_status: String,
  trial_location: String
});

module.exports = mongoose.model('ClinicalTrial', clinicalTrialSchema);

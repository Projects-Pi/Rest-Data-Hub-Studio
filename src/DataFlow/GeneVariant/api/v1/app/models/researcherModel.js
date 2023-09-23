const mongoose = require('mongoose');

const researcherSchema = new mongoose.Schema({
  researcher_id: {
    type: String,
    unique: true,
    required: true,
  },
  researcher_name: String,
  affiliation: String,
  research_interests: [String],
  email: String,
  phone_number: String,
  research_publications: [String]
});

module.exports = mongoose.model('Researcher', researcherSchema);

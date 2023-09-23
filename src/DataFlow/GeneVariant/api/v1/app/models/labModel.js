const mongoose = require('mongoose');

const labSchema = new mongoose.Schema({
  lab_id: {
    type: String,
    unique: true,
    required: true,
  },
  lab_name: String,
  location: String,
  lab_head: String,
  lab_description: String,
  lab_website: String,
  established_year: Number
});

module.exports = mongoose.model('Lab', labSchema);

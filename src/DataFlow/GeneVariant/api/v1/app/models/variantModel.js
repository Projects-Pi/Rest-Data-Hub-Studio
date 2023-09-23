const mongoose = require('mongoose');

const variantSchema = new mongoose.Schema({
  variant_id: {
    type: String,
    unique: true,
    required: true,
  },
  variant_name: String,
  variant_type: String,
  location: String,
  allele_frequency: Number,
  impact: String,
  mutation_description: String,
  dbSNP_id: String,
});

module.exports = mongoose.model('Variant', variantSchema);

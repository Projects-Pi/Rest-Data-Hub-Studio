const mongoose = require('mongoose');

const geneSchema = new mongoose.Schema({
  gene_id: {
    type: String,
    unique: true,
    required: true,
  },
  gene_name: String,
  gene_symbol: String,
  sequence: String,
  chromosomal_location: String,
  gene_function: String,
  exon_count: Number,
  chromosome: String
});

module.exports = mongoose.model('Gene', geneSchema);

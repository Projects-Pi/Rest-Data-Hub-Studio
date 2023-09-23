const express = require('express');
const router = express.Router();
const Gene = require('../models/geneModel'); // Import the Gene model

// Create a new gene
router.post('/genes', async (req, res) => {
  try {
    const gene = new Gene(req.body);
    await gene.save();
    res.status(201).json(gene);
  } catch (err) {
    res.status(400).json({ error: err.message });
  }
});

// Get all genes
router.get('/genes', async (req, res) => {
  try {
    const genes = await Gene.find();
    res.json(genes);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// Get a specific gene by ID
router.get('/genes/:geneId', async (req, res) => {
  const { geneId } = req.params;
  try {
    const gene = await Gene.findById(geneId);
    if (!gene) {
      return res.status(404).json({ error: 'Gene not found' });
    }
    res.json(gene);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// Update a gene by ID
router.put('/genes/:geneId', async (req, res) => {
  const { geneId } = req.params;
  try {
    const gene = await Gene.findByIdAndUpdate(geneId, req.body, { new: true });
    if (!gene) {
      return res.status(404).json({ error: 'Gene not found' });
    }
    res.json(gene);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// Delete a gene by ID
router.delete('/genes/:geneId', async (req, res) => {
  const { geneId } = req.params;
  try {
    const gene = await Gene.findByIdAndRemove(geneId);
    if (!gene) {
      return res.status(404).json({ error: 'Gene not found' });
    }
    res.json({ message: 'Gene deleted successfully' });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

module.exports = router;

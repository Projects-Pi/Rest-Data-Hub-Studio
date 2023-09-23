const express = require('express');
const router = express.Router();
const Variant = require('../models/variantModel'); // Import the Variant model

// Create a new variant
router.post('/variants', async (req, res) => {
  try {
    const variant = new Variant(req.body);
    await variant.save();
    res.status(201).json(variant);
  } catch (err) {
    res.status(400).json({ error: err.message });
  }
});

// Get all variants
router.get('/variants', async (req, res) => {
  try {
    const variants = await Variant.find();
    res.json(variants);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// Get a specific variant by ID
router.get('/variants/:variantId', async (req, res) => {
  const { variantId } = req.params;
  try {
    const variant = await Variant.findById(variantId);
    if (!variant) {
      return res.status(404).json({ error: 'Variant not found' });
    }
    res.json(variant);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// Update a variant by ID
router.put('/variants/:variantId', async (req, res) => {
  const { variantId } = req.params;
  try {
    const variant = await Variant.findByIdAndUpdate(variantId, req.body, { new: true });
    if (!variant) {
      return res.status(404).json({ error: 'Variant not found' });
    }
    res.json(variant);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// Delete a variant by ID
router.delete('/variants/:variantId', async (req, res) => {
  const { variantId } = req.params;
  try {
    const variant = await Variant.findByIdAndRemove(variantId);
    if (!variant) {
      return res.status(404).json({ error: 'Variant not found' });
    }
    res.json({ message: 'Variant deleted successfully' });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

module.exports = router;

const express = require('express');
const router = express.Router();
const Researcher = require('../models/researcherModel'); // Import the Researcher model

// Create a new researcher
router.post('/researchers', async (req, res) => {
  try {
    const researcher = new Researcher(req.body);
    await researcher.save();
    res.status(201).json(researcher);
  } catch (err) {
    res.status(400).json({ error: err.message });
  }
});

// Get all researchers
router.get('/researchers', async (req, res) => {
  try {
    const researchers = await Researcher.find();
    res.json(researchers);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// Get a specific researcher by ID
router.get('/researchers/:researcherId', async (req, res) => {
  const { researcherId } = req.params;
  try {
    const researcher = await Researcher.findById(researcherId);
    if (!researcher) {
      return res.status(404).json({ error: 'Researcher not found' });
    }
    res.json(researcher);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// Update a researcher by ID
router.put('/researchers/:researcherId', async (req, res) => {
  const { researcherId } = req.params;
  try {
    const researcher = await Researcher.findByIdAndUpdate(researcherId, req.body, { new: true });
    if (!researcher) {
      return res.status(404).json({ error: 'Researcher not found' });
    }
    res.json(researcher);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// Delete a researcher by ID
router.delete('/researchers/:researcherId', async (req, res) => {
  const { researcherId } = req.params;
  try {
    const researcher = await Researcher.findByIdAndRemove(researcherId);
    if (!researcher) {
      return res.status(404).json({ error: 'Researcher not found' });
    }
    res.json({ message: 'Researcher deleted successfully' });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

module.exports = router;

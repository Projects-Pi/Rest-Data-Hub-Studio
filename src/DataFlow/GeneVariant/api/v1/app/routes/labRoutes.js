const express = require('express');
const router = express.Router();
const Lab = require('../models/labModel'); // Import the Lab model

// Create a new lab
router.post('/labs', async (req, res) => {
  try {
    const lab = new Lab(req.body);
    await lab.save();
    res.status(201).json(lab);
  } catch (err) {
    res.status(400).json({ error: err.message });
  }
});

// Get all labs
router.get('/labs', async (req, res) => {
  try {
    const labs = await Lab.find();
    res.json(labs);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// Get a specific lab by ID
router.get('/labs/:labId', async (req, res) => {
  const { labId } = req.params;
  try {
    const lab = await Lab.findById(labId);
    if (!lab) {
      return res.status(404).json({ error: 'Lab not found' });
    }
    res.json(lab);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// Update a lab by ID
router.put('/labs/:labId', async (req, res) => {
  const { labId } = req.params;
  try {
    const lab = await Lab.findByIdAndUpdate(labId, req.body, { new: true });
    if (!lab) {
      return res.status(404).json({ error: 'Lab not found' });
    }
    res.json(lab);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// Delete a lab by ID
router.delete('/labs/:labId', async (req, res) => {
  const { labId } = req.params;
  try {
    const lab = await Lab.findByIdAndRemove(labId);
    if (!lab) {
      return res.status(404).json({ error: 'Lab not found' });
    }
    res.json({ message: 'Lab deleted successfully' });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

module.exports = router;

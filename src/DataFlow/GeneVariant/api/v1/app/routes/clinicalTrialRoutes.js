const express = require('express');
const router = express.Router();
const ClinicalTrial = require('../models/clinicalTrialModel'); // Import the ClinicalTrial model

// Create a new clinical trial
router.post('/clinical-trials', async (req, res) => {
  try {
    const clinicalTrial = new ClinicalTrial(req.body);
    await clinicalTrial.save();
    res.status(201).json(clinicalTrial);
  } catch (err) {
    res.status(400).json({ error: err.message });
  }
});

// Get all clinical trials
router.get('/clinical-trials', async (req, res) => {
  try {
    const clinicalTrials = await ClinicalTrial.find();
    res.json(clinicalTrials);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// Get a specific clinical trial by ID
router.get('/clinical-trials/:trialId', async (req, res) => {
  const { trialId } = req.params;
  try {
    const clinicalTrial = await ClinicalTrial.findById(trialId);
    if (!clinicalTrial) {
      return res.status(404).json({ error: 'Clinical trial not found' });
    }
    res.json(clinicalTrial);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// Update a clinical trial by ID
router.put('/clinical-trials/:trialId', async (req, res) => {
  const { trialId } = req.params;
  try {
    const clinicalTrial = await ClinicalTrial.findByIdAndUpdate(trialId, req.body, { new: true });
    if (!clinicalTrial) {
      return res.status(404).json({ error: 'Clinical trial not found' });
    }
    res.json(clinicalTrial);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// Delete a clinical trial by ID
router.delete('/clinical-trials/:trialId', async (req, res) => {
  const { trialId } = req.params;
  try {
    const clinicalTrial = await ClinicalTrial.findByIdAndRemove(trialId);
    if (!clinicalTrial) {
      return res.status(404).json({ error: 'Clinical trial not found' });
    }
    res.json({ message: 'Clinical trial deleted successfully' });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

module.exports = router;

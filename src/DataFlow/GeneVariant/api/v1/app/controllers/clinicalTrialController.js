const ClinicalTrial = require('../models/clinicalTrialModel');

// Create a new clinical trial
exports.createClinicalTrial = async (req, res) => {
  try {
    const clinicalTrial = new ClinicalTrial(req.body);
    await clinicalTrial.save();
    res.status(201).json(clinicalTrial);
  } catch (err) {
    res.status(400).json({ error: err.message });
  }
};

// Get all clinical trials
exports.getAllClinicalTrials = async (req, res) => {
  try {
    const clinicalTrials = await ClinicalTrial.find();
    res.json(clinicalTrials);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
};

// Get a specific clinical trial by ID
exports.getClinicalTrialById = async (req, res) => {
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
};

// Update a clinical trial by ID
exports.updateClinicalTrial = async (req, res) => {
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
};

// Delete a clinical trial by ID
exports.deleteClinicalTrial = async (req, res) => {
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
};

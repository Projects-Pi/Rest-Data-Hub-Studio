const Lab = require('../models/labModel');

// Create a new lab
exports.createLab = async (req, res) => {
  try {
    const lab = new Lab(req.body);
    await lab.save();
    res.status(201).json(lab);
  } catch (err) {
    res.status(400).json({ error: err.message });
  }
};

// Get all labs
exports.getAllLabs = async (req, res) => {
  try {
    const labs = await Lab.find();
    res.json(labs);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
};

// Get a specific lab by ID
exports.getLabById = async (req, res) => {
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
};

// Update a lab by ID
exports.updateLab = async (req, res) => {
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
};

// Delete a lab by ID
exports.deleteLab = async (req, res) => {
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
};

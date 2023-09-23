const Researcher = require('../models/researcherModel');

// Create a new researcher
exports.createResearcher = async (req, res) => {
  try {
    const researcher = new Researcher(req.body);
    await researcher.save();
    res.status(201).json(researcher);
  } catch (err) {
    res.status(400).json({ error: err.message });
  }
};

// Get all researchers
exports.getAllResearchers = async (req, res) => {
  try {
    const researchers = await Researcher.find();
    res.json(researchers);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
};

// Get a specific researcher by ID
exports.getResearcherById = async (req, res) => {
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
};

// Update a researcher by ID
exports.updateResearcher = async (req, res) => {
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
};

// Delete a researcher by ID
exports.deleteResearcher = async (req, res) => {
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
};

const MedicalHistory = require('../models/medicalHistoryModel');

// Create a new medical history record
exports.createMedicalHistory = async (req, res) => {
  try {
    const medicalHistory = new MedicalHistory(req.body);
    await medicalHistory.save();
    res.status(201).json(medicalHistory);
  } catch (err) {
    res.status(400).json({ error: err.message });
  }
};

// Get all medical history records
exports.getAllMedicalHistory = async (req, res) => {
  try {
    const medicalHistoryRecords = await MedicalHistory.find();
    res.json(medicalHistoryRecords);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
};

// Get a specific medical history record by ID
exports.getMedicalHistoryById = async (req, res) => {
  const { historyId } = req.params;
  try {
    const medicalHistory = await MedicalHistory.findById(historyId);
    if (!medicalHistory) {
      return res.status(404).json({ error: 'Medical history record not found' });
    }
    res.json(medicalHistory);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
};

// Update a medical history record by ID
exports.updateMedicalHistory = async (req, res) => {
  const { historyId } = req.params;
  try {
    const medicalHistory = await MedicalHistory.findByIdAndUpdate(historyId, req.body, { new: true });
    if (!medicalHistory) {
      return res.status(404).json({ error: 'Medical history record not found' });
    }
    res.json(medicalHistory);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
};

// Delete a medical history record by ID
exports.deleteMedicalHistory = async (req, res) => {
  const { historyId } = req.params;
  try {
    const medicalHistory = await MedicalHistory.findByIdAndRemove(historyId);
    if (!medicalHistory) {
      return res.status(404).json({ error: 'Medical history record not found' });
    }
    res.json({ message: 'Medical history record deleted successfully' });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
};

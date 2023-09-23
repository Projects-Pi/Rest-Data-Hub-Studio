const express = require('express');
const router = express.Router();
const Patient = require('../models/patientModel'); // Import the Patient model

// Create a new patient
router.post('/patients', async (req, res) => {
  try {
    const patient = new Patient(req.body);
    await patient.save();
    res.status(201).json(patient);
  } catch (err) {
    res.status(400).json({ error: err.message });
  }
});

// Get all patients
router.get('/patients', async (req, res) => {
  try {
    const patients = await Patient.find();
    res.json(patients);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// Get a specific patient by ID
router.get('/patients/:patientId', async (req, res) => {
  const { patientId } = req.params;
  try {
    const patient = await Patient.findById(patientId);
    if (!patient) {
      return res.status(404).json({ error: 'Patient not found' });
    }
    res.json(patient);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// Update a patient by ID
router.put('/patients/:patientId', async (req, res) => {
  const { patientId } = req.params;
  try {
    const patient = await Patient.findByIdAndUpdate(patientId, req.body, { new: true });
    if (!patient) {
      return res.status(404).json({ error: 'Patient not found' });
    }
    res.json(patient);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// Delete a patient by ID
router.delete('/patients/:patientId', async (req, res) => {
  const { patientId } = req.params;
  try {
    const patient = await Patient.findByIdAndRemove(patientId);
    if (!patient) {
      return res.status(404).json({ error: 'Patient not found' });
    }
    res.json({ message: 'Patient deleted successfully' });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

module.exports = router;

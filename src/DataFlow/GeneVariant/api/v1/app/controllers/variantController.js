const Variant = require('../models/variantModel');

// Create a new variant
exports.createVariant = async (req, res) => {
  try {
    const variant = new Variant(req.body);
    await variant.save();
    res.status(201).json(variant);
  } catch (err) {
    res.status(400).json({ error: err.message });
  }
};

// Get all variants
exports.getAllVariants = async (req, res) => {
  try {
    const variants = await Variant.find();
    res.json(variants);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
};

// Get a specific variant by ID
exports.getVariantById = async (req, res) => {
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
};

// Update a variant by ID
exports.updateVariant = async (req, res) => {
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
};

// Delete a variant by ID
exports.deleteVariant = async (req, res) => {
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
};

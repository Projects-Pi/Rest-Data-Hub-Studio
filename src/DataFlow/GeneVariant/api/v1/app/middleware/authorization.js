// Middleware for user authorization
const authorizeUser = (requiredRole) => {
  return (req, res, next) => {
    const user = req.user; // Assuming you have user information in the request (e.g., from authentication middleware)

    // Check if the user has the required role or permission
    if (user && user.role === requiredRole) {
      next(); // User is authorized, continue to the next middleware/route handler
    } else {
      res.status(403).json({ error: 'Forbidden - Insufficient permissions' });
    }
  };
};

module.exports = authorizeUser;

/*
const express = require('express');
const router = express.Router();
const authorizeUser = require('../middleware/authorization');

// Example route protected by authorization middleware
router.get('/admin-dashboard', authorizeUser('admin'), (req, res) => {
  // Only users with the 'admin' role can access this route
  res.json({ message: 'Admin dashboard' });
});

module.exports = router;

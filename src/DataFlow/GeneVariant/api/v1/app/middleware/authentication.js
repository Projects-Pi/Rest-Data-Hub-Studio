const jwt = require('jsonwebtoken');
const { SECRET_KEY } = require('../config/env');

// Middleware for user authentication
const authenticateUser = (req, res, next) => {
  // Extract the token from the request headers
  const token = req.header('Authorization');

  // Check if a token is present
  if (!token) {
    return res.status(401).json({ error: 'Unauthorized - Token not provided' });
  }

  try {
    // Verify the token
    const decoded = jwt.verify(token, SECRET_KEY);

    // Attach the user information to the request for further use
    req.user = decoded.user;
    next();
  } catch (err) {
    return res.status(401).json({ error: 'Unauthorized - Invalid token' });
  }
};
/*
module.exports = authenticateUser;


const express = require('express');
const router = express.Router();
const authenticateUser = require('../middleware/authentication');

// Example protected route that requires authentication
router.get('/protected', authenticateUser, (req, res) => {
  // This route is protected, and req.user contains the user information
  res.json({ message: 'Authenticated route', user: req.user });
});

module.exports = router;


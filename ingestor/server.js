import express from 'express';
import logger from './app/utils/logger.js';
import corsMiddleware from './app/config/cors.js';
import requestLogger from './app/middleware/requestLogger.js';


const app = express();

// Middleware
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(corsMiddleware);
app.use(requestLogger);

// Routes
app.use(routes);


const PORT = process.env.PORT || 3000;


app.listen(PORT, () => {
  logger.info(`Server is running on port ${PORT}`);
});
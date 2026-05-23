import express from 'express';
import logger from './app/utils/logger.js';

const app = express();

app.get('/', (req, res) => {
  logger.info('GET /');
  res.send('Hello, World!');
});

const PORT = process.env.PORT || 3000;

app.listen(PORT, () => {
  logger.info({ port: PORT }, 'Server is running');
});
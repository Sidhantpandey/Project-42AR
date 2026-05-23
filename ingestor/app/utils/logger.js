import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import pino from 'pino';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const logDir = path.join(__dirname, '../../logs');

fs.mkdirSync(logDir, { recursive: true });
const logPath = path.join(logDir, 'server.log');

const transport = pino.transport({
  target: 'pino/file',
  level: 'info',
  options: { destination: logPath }
});

const logger = pino({ level: 'info' }, transport);
export default logger;

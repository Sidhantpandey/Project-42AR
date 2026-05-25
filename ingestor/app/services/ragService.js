import { ApiError } from '../utils/ApiError.js';

const PYTHON_URL = process.env.PYTHON_SERVICE_URL || 'http://localhost:8000';

async function getServiceStatus() {
  try {
    const res = await fetch(`${PYTHON_URL}/health`);

    if (!res.ok) {
      throw new ApiError(503, 'Python service is not healthy');
    }

    const data = await res.json();
    return { status: data.status || 'healthy' };
  } catch (error) {
    if (error instanceof ApiError) throw error;
    throw new ApiError(503, 'Python service is unreachable');
  }
}

export default { getServiceStatus };

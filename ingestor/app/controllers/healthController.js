import { ApiResponse } from '../utils/ApiResponse.js';
import { asyncHandler } from '../utils/asyncHandler.js';
import ragService from '../services/ragService.js';

export const getHealth = asyncHandler(async (req, res) => {
  const python = await ragService.getServiceStatus();

  return res.status(200).json(
    new ApiResponse(
      200,
      {
        server: 'healthy',
        python_service: python.status,
      },
      'Health check successful'
    )
  );
});

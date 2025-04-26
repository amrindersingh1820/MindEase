import API from './api';

// Fetch meditation guides
export const fetchMeditations = async () => {
  try {
    const response = await API.get('/api/meditations/');
    return response.data;
  } catch (error) {
    throw error.response.data;
  }
};
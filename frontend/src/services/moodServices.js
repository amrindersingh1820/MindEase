import API from './api';

// Submit Mood
export const submitMood = async (moodData) => {
  try {
    const response = await API.post('/api/moods/', moodData);
    return response.data;
  } catch (error) {
    throw error.response.data;
  }
};

// Fetch Mood History
export const fetchMoods = async () => {
  try {
    const response = await API.get('/api/moods/');
    return response.data;
  } catch (error) {
    throw error.response.data;
  }
};
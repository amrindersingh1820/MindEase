import API from './api';

// REGISTER
export const registerUser = async (userData) => {
  try {
    const response = await API.post('/api/auth/register', userData);
    return response.data;
  } catch (error) {
    throw error.response.data;
  }
};

// LOGIN
export const loginUser = async (loginData) => {
  try {
    const response = await API.post('/api/auth/login', loginData);
    return response.data;
  } catch (error) {
    throw error.response.data;
  }
};
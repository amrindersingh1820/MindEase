import { loginUser } from '../services/authService';
import { useState } from 'react';

function LoginPage() {
  const [loginData, setLoginData] = useState({ email: '', password: '' });

  const handleLogin = async (e) => {
    e.preventDefault();
    try {
      const result = await loginUser(loginData);
      console.log('✅ User Logged In:', result);

      // Save token to localStorage
      localStorage.setItem('token', result.token);

      alert('Login Successful!');
      // Redirect or move to dashboard
    } catch (error) {
      console.error('❌ Login Error:', error.message);
      alert(error.message);
    }
  };

  return (
    <form onSubmit={handleLogin}>
      <input
        type="email"
        placeholder="Email"
        value={loginData.email}
        onChange={(e) => setLoginData({ ...loginData, email: e.target.value })}
      />
      <input
        type="password"
        placeholder="Password"
        value={loginData.password}
        onChange={(e) => setLoginData({ ...loginData, password: e.target.value })}
      />
      <button type="submit">Login</button>
    </form>
  );
}

export default LoginPage;
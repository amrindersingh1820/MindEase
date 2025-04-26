import React from 'react';

const Login = () => {
  return (
    <div>
      <h2>Login</h2>
      <form>
        <label>
          Username:
          <input type="text" name="username" required />
        </label>
        <label>
          Password:
          <input type="password" name="password" required />
        </label>
        <button type="submit">Login</button>
      </form>
    </div>
  );
};

export default Login;
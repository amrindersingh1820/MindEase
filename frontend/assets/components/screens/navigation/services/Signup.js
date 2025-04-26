import React from 'react';

const Signup = () => {
  return (
    <div>
      <h2>Sign Up</h2>
      <form>
        <label>
          Username:
          <input type="text" name="username" required />
        </label>
        <label>
          Email:
          <input type="email" name="email" required />
        </label>
        <label>
          Password:
          <input type="password" name="password" required />
        </label>
        <button type="submit">Sign Up</button>
      </form>
    </div>
  );
};

export default Signup;
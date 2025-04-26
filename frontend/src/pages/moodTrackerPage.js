import { submitMood, fetchMoods } from '../services/moodService';
import { useState, useEffect } from 'react';

function MoodTrackerPage() {
  const [mood, setMood] = useState('');
  const [moodHistory, setMoodHistory] = useState([]);

  const handleMoodSubmit = async (e) => {
    e.preventDefault();
    try {
      await submitMood({ mood });
      alert('Mood submitted successfully!');
      setMood('');
      loadMoods(); // Refresh mood history
    } catch (error) {
      console.error('❌ Error submitting mood:', error.message);
      alert(error.message);
    }
  };

  const loadMoods = async () => {
    try {
      const moods = await fetchMoods();
      setMoodHistory(moods);
    } catch (error) {
      console.error('❌ Error fetching moods:', error.message);
    }
  };

  useEffect(() => {
    loadMoods();
  }, []);

  return (
    <div>
      <h2>Submit your Mood</h2>
      <form onSubmit={handleMoodSubmit}>
        <input
          type="text"
          placeholder="How are you feeling?"
          value={mood}
          onChange={(e) => setMood(e.target.value)}
        />
        <button type="submit">Submit</button>
      </form>

      <h3>Your Mood History:</h3>
      <ul>
        {moodHistory.map((m, index) => (
          <li key={index}>{m.mood} - {new Date(m.timestamp).toLocaleString()}</li>
        ))}
      </ul>
    </div>
  );
}

export default MoodTrackerPage;
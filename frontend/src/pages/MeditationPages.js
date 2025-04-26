import { useEffect, useState } from 'react';
import { fetchMeditations } from '../services/meditationService';

function MeditationPage() {
  const [meditations, setMeditations] = useState([]);

  const loadMeditations = async () => {
    try {
      const data = await fetchMeditations();
      setMeditations(data);
    } catch (error) {
      console.error('❌ Error fetching meditations:', error.message);
    }
  };

  useEffect(() => {
    loadMeditations();
  }, []);

  return (
    <div>
      <h2>Meditation Guides</h2>
      {meditations.length === 0 ? (
        <p>Loading...</p>
      ) : (
        <ul>
          {meditations.map((meditation, index) => (
            <li key={index}>
              <h4>{meditation.title}</h4>
              <p>{meditation.description}</p>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default MeditationPage;
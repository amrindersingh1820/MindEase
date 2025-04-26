// Adjust canvas size dynamically for responsiveness
function adjustCanvasSize() {
  const canvas = document.getElementById('gameCanvas');
  if (canvas) {
    const container = document.getElementById('game-container');
    canvas.width = container.offsetWidth * 0.9; // Set canvas width to 90% of container
    canvas.height = canvas.width * 0.75; // Maintain a 4:3 aspect ratio
  }
}

// Adjust font sizes dynamically for responsiveness
function adjustFontSizes() {
  const heroMsg = document.querySelector('.hero-msg h2');
  if (heroMsg) {
    heroMsg.style.fontSize = window.innerWidth < 768 ? '1.5rem' : '2.5rem';
  }
}

// Add event listeners for window resize
window.addEventListener('resize', () => {
  adjustCanvasSize();
  adjustFontSizes();
});

// Initial adjustments on page load
window.addEventListener('DOMContentLoaded', () => {
  adjustCanvasSize();
  adjustFontSizes();
});

const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');
let animationFrameId;
let isGameRunning = false; // Prevent multiple game instances
const cornerHitSound = new Audio('bell-meditation-75335.mp3'); // Load sound file

function getRandomColor() {
  return `#${Math.floor(Math.random() * 16777215).toString(16)}`;
}

function drawCircle(x, y, radius, color) {
  ctx.beginPath();
  ctx.arc(x, y, radius, 0, Math.PI * 2);
  ctx.fillStyle = color;
  ctx.fill();
  ctx.closePath();
}

function clearCanvas() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
}

function adjustCanvasSize() {
  const container = document.getElementById('game-container');
  canvas.width = container.offsetWidth * 0.9; // Set canvas width to 90% of container
  canvas.height = canvas.width * 0.75; // Maintain a 4:3 aspect ratio
}

function startGame() {
  if (isGameRunning) return; // Prevent multiple game instances
  isGameRunning = true;

  let x = canvas.width / 2;
  let y = canvas.height / 2;
  let dx = 2;
  let dy = 2;
  const radius = 20;
  let ballColor = 'blue';

  function animate() {
    clearCanvas();
    drawCircle(x, y, radius, ballColor);
    x += dx;
    y += dy;

    const isCornerHit =
      (x + radius >= canvas.width && y + radius >= canvas.height) || // Bottom-right corner
      (x - radius <= 0 && y - radius <= 0) || // Top-left corner
      (x + radius >= canvas.width && y - radius <= 0) || // Top-right corner
      (x - radius <= 0 && y + radius >= canvas.height); // Bottom-left corner

    if (isCornerHit) {
      cornerHitSound.play(); // Play sound on corner hit
    }

    if (x + radius > canvas.width || x - radius < 0) {
      dx = -dx;
      ballColor = getRandomColor(); // Change color on horizontal collision
    }
    if (y + radius > canvas.height || y - radius < 0) {
      dy = -dy;
      ballColor = getRandomColor(); // Change color on vertical collision
    }

    animationFrameId = requestAnimationFrame(animate);
  }

  animate();
}

document.getElementById('startGameBtn').addEventListener('click', () => {
  if (animationFrameId) cancelAnimationFrame(animationFrameId); // Stop previous animation
  adjustCanvasSize(); // Ensure canvas is resized before starting
  startGame();
});

// Adjust canvas size on window resize
window.addEventListener('resize', adjustCanvasSize);

// Initial canvas adjustment
window.addEventListener('DOMContentLoaded', adjustCanvasSize);
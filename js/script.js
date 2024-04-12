let score = 0;

const coin = document.getElementById('coin');
const scoreDisplay = document.getElementById('score');

coin.addEventListener('click', () => {
    score++;
    scoreDisplay.textContent = score;
});

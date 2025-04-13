let soundEnabled = true;
let darkMode = false;
let isPvP = false;  // Mode Player vs Player ou IA
let currentPlayer = 'X';
let player1Motif = 'X';  // Motif du joueur 1
let player2Motif = 'O';  // Motif du joueur 2
let volume = 1;  // Volume du jeu (de 0 à 1)
let board = ['', '', '', '', '', '', '', '', ''];
let gameOver = false;
// Fonction pour afficher/masquer le menu
function toggleMenu() {
  const menu = document.getElementById('dropdown-menu');
  menu.style.display = menu.style.display === 'block' ? 'none' : 'block';
}
// Fonction pour activer/désactiver le son
function toggleSound() {
  soundEnabled = !soundEnabled;
  alert('Son ' + (soundEnabled ? 'activé' : 'désactivé'));
}
// Fonction pour changer le mode sombre
function toggleDarkMode() {
  darkMode = !darkMode;
  document.body.classList.toggle('dark-mode', darkMode);
  alert('Mode ' + (darkMode ? 'sombre' : 'clair') + ' activé');
}
// Fonction pour démarrer le mode Player vs Player
function startPvPGame() {
  isPvP = true;
  resetGame();
  alert('Mode Player vs Player lancé!');
}
// Fonction pour démarrer le mode Player vs IA
function startPvEGame() {
  isPvP = false;
  resetGame();
  alert('Mode Player vs IA lancé!');
}
// Fonction pour choisir les motifs
function changeMotifs() {
  const motif = prompt("Entrez le motif pour le joueur (ex : ♥, ★, ☀)");
  if (motif) {
    player1Motif = motif;
    player2Motif = motif === 'X' ? 'O' : 'X'; // Assure-toi que les motifs des deux joueurs sont différents
    alert('Motif du joueur 1 : ' + player1Motif + ', joueur 2 : ' + player2Motif);
  }
}
// Fonction pour afficher le classement (en l'état, juste un exemple)
function showRank() {
  alert("Affichage des classements à venir...");
}
// Réinitialiser le jeu
function resetGame() {
  board = ['', '', '', '', '', '', '', '', ''];
  currentPlayer = 'X';
  gameOver = false;
  renderBoard();
}
// Affichage du plateau de jeu
function renderBoard() {
  const gameBoard = document.getElementById('game-board');
  gameBoard.innerHTML = '';
  for (let i = 0; i < 9; i++) {
    const cell = document.createElement('div');
    cell.classList.add('cell');
    cell.textContent = board[i];
    cell.onclick = () => handleCellClick(i);
    gameBoard.appendChild(cell);
  }
}
// Gérer les clics sur les cases
function handleCellClick(index) {
  if (board[index] === '' && !gameOver) {
    board[index] = currentPlayer === 'X' ? player1Motif : player2Motif;
    renderBoard();
    checkWinner();
    togglePlayer();
    if (!isPvP && currentPlayer === 'O' && !gameOver) {
      aiMove();
    }
  }
}
// Changer de joueur
function togglePlayer() {
  currentPlayer = currentPlayer === 'X' ? 'O' : 'X';
}
// Vérifier si un joueur a gagné
function checkWinner() {
  const winPatterns = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8], // Lignes
    [0, 3, 6], [1, 4, 7], [2, 5, 8], // Colonnes
    [0, 4, 8], [2, 4, 6], // Diagonales
  ];

  for (const pattern of winPatterns) {
    const [a, b, c] = pattern;
    if (board[a] && board[a] === board[b] && board[a] === board[c]) {
      alert(`${board[a]} a gagné !`);
      gameOver = true;
      return;
    }
  }

  if (!board.includes('')) {
    alert("Match nul!");
    gameOver = true;
  }
}
// IA qui joue contre le joueur (très simple)
function aiMove() {
  let availableCells = board.map((cell, index) => cell === '' ? index : null).filter(val => val !== null);
  let randomCell = availableCells[Math.floor(Math.random() * availableCells.length)];
  board[randomCell] = player2Motif;
  renderBoard();
  checkWinner();
  togglePlayer();
}
/* ============================================================
   MAIN.JS — Sidebar toggle + Add task card
   ============================================================ */

// ─── SIDEBAR ───


function toggleSidebar() {
  const sidebar     = document.getElementById('sidebar');
  const sidebarWrap = document.querySelector('.app-layout__sidebar');
  if (!sidebar) return;

  sidebar.classList.toggle('sidebar--closed');
  sidebarWrap.classList.toggle('sidebar-collapsed');

}
let taskCardReady = false;
// Always start closed on page load
document.addEventListener('DOMContentLoaded', function () {
  const sidebar     = document.getElementById('sidebar');
  const sidebarWrap = document.querySelector('.app-layout__sidebar');
  if (!sidebar) return;

  sidebar.classList.add('sidebar--closed');
  sidebarWrap.classList.add('sidebar-collapsed');
  setTimeout(() => { taskCardReady = true; }, 300);

});

// ─── ADD TASK CARD ───

function addtaskopen() {
  const card = document.getElementById('cardAddTask');
  if (!taskCardReady) return;
  if (!card) return;
  card.classList.add('open');
  document.body.style.overflow = 'hidden';
  setTimeout(() => {
    const input = card.querySelector('.task-card__title-input');
    if (input) input.focus();
  }, 50);
}

function addtaskclose() {
  const card = document.getElementById('cardAddTask');
  if (!card) return;
  card.classList.remove('open');
  document.body.style.overflow = '';
}

document.addEventListener('click', function (e) {
  const card = document.getElementById('cardAddTask');
  if (!card) return;
  if (card.classList.contains('open') && e.target === card) addtaskclose();
});

document.addEventListener('keydown', function (e) {
  if (e.key === 'Escape') addtaskclose();
});

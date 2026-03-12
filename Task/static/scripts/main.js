/* ============================================================
   MAIN.JS — Sidebar toggle + Add task card
   ============================================================ */

// ─── SIDEBAR ───

function updateTitle(sidebarIsOpen) {
  const title = document.querySelector('.title__head');
  const floatBtn = document.querySelector('.sidebar__float-btn');
  if (!title) return;

  if (sidebarIsOpen) {
    title.classList.add('title__head-hidden');
    if (floatBtn) floatBtn.classList.remove('visible');
  } else {
    title.classList.remove('title__head-hidden');
    if (floatBtn) floatBtn.classList.add('visible');
  }
}

function toggleSidebar() {
  const sidebar     = document.getElementById('sidebar');
  const sidebarWrap = document.querySelector('.app-layout__sidebar');
  if (!sidebar) return;

  const isOpen = !sidebar.classList.contains('sidebar--closed');

  if (isOpen) {
    // close
    sidebar.classList.add('sidebar--closed');
    sidebarWrap.classList.add('sidebar-collapsed');
    localStorage.setItem('sidebar', 'closed');
    updateTitle(false);
  } else {
    // open
    sidebar.classList.remove('sidebar--closed');
    sidebarWrap.classList.remove('sidebar-collapsed');
    localStorage.setItem('sidebar', 'open');
    updateTitle(true);
  }
}

// Restore sidebar state on page load
document.addEventListener('DOMContentLoaded', function () {
  const sidebar     = document.getElementById('sidebar');
  const sidebarWrap = document.querySelector('.app-layout__sidebar');
  if (!sidebar) return;

  const state = localStorage.getItem('sidebar');

  if (state === 'closed') {
    sidebar.classList.add('sidebar--closed');
    sidebarWrap.classList.add('sidebar-collapsed');
    updateTitle(false);
  } else {
    updateTitle(true);
  }
});

// ─── ADD TASK CARD ───

function addtaskopen() {
  const card = document.getElementById('cardAddTask');
  if (!card) return;
  card.classList.add('open');
  document.body.style.overflow = 'hidden';
  // focus title input
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

// Close card on overlay click
document.addEventListener('click', function (e) {
  const card = document.getElementById('cardAddTask');
  if (!card) return;
  if (card.classList.contains('open') && e.target === card) {
    addtaskclose();
  }
});

// Close on Escape
document.addEventListener('keydown', function (e) {
  if (e.key === 'Escape') addtaskclose();
});

/* ============================================================
   CONFIRM.JS — Delete confirm modal
   ============================================================ */

document.addEventListener('DOMContentLoaded', function () {
  const modal     = document.querySelector('.task_confirm');
  const deleteBtn = document.querySelector('.button-delete');
  const cancelBtn = document.querySelector('.cancel-btn');

  if (!modal) return;

  // open modal
  if (deleteBtn) {
    deleteBtn.addEventListener('click', function (e) {
      e.preventDefault();
      modal.classList.add('open');
      document.body.style.overflow = 'hidden';
    });
  }

  // close modal
  function closeConfirm() {
    modal.classList.remove('open');
    document.body.style.overflow = '';
  }

  if (cancelBtn) {
    cancelBtn.addEventListener('click', closeConfirm);
  }

  // close on overlay click
  modal.addEventListener('click', function (e) {
    if (e.target === modal) closeConfirm();
  });

  // close on Escape
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') closeConfirm();
  });
});

/* ============================================================
   CONFIRM.JS — Delete confirm modal
   ============================================================ */

document.addEventListener('DOMContentLoaded', function () {
  const modal     = document.querySelector('.task_confirm');
  const deleteBtn = document.querySelectorAll('.button-delete');
  const cancelBtn = document.querySelector('.cancel-btn');

  if (!modal) return;

  // open modal
  if (deleteBtn) {
    deleteBtn.forEach(function(dltbtn){
      dltbtn.addEventListener('click', function (e) {
      e.preventDefault();
      const taskId = this.dataset.taskId; // for form 
      const taskTitle = this.dataset.taskTitle; // for display content
      // Update the form action dynamically
      const form = modal.querySelector('form');
      const spanTitle = form.querySelector('.title-confirm-info').querySelector('span');
      const url = this.dataset.deleteUrl;
      if (form && taskId && spanTitle) {
        form.action = url;
        spanTitle.textContent = taskTitle;

      }
      modal.classList.add('open');
      document.body.style.overflow = 'hidden';
    });
  })
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




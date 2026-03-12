/* ============================================================
   TASK_FORM.JS — Dropdown logic for add/edit task card
   ============================================================ */

document.addEventListener('DOMContentLoaded', function () {

  // ─── DATE LABEL ───
  const dateInput = document.getElementById('dueDateInput');
  const dateLabel = document.getElementById('dueDateLabel');

  if (dateInput && dateLabel) {
    dateInput.addEventListener('change', function () {
      if (this.value) {
        // parse as local date to avoid timezone shift
        const [year, month, day] = this.value.split('-').map(Number);
        const date = new Date(year, month - 1, day);
        dateLabel.textContent = date.toLocaleDateString('en-US', { month: 'short', day: 'numeric' });
      } else {
        dateLabel.textContent = 'Due date';
      }
    });

    // set label on load if editing (value already set)
    if (dateInput.value) {
      const [year, month, day] = dateInput.value.split('-').map(Number);
      const date = new Date(year, month - 1, day);
      dateLabel.textContent = date.toLocaleDateString('en-US', { month: 'short', day: 'numeric' });
    }
  }

  // ─── SUBMIT GUARD (title required) ───
  const submitBtn  = document.querySelector('.task-card__submit');
  const titleInput = document.querySelector('.task-card__title-input');

  if (submitBtn && titleInput) {
    function checkTitle() {
      submitBtn.disabled = titleInput.value.trim() === '';
    }
    titleInput.addEventListener('input', checkTitle);
    checkTitle();
  }

  // ─── CLOSE DROPDOWNS ON OUTSIDE CLICK ───
  document.addEventListener('click', function (e) {
    if (!e.target.closest('.task-card__dropdown')) {
      document.querySelectorAll('.dropdown__menu').forEach(m => {
        m.classList.remove('dropdown__menu--open');
      });
    }
  });

});

// ─── DROPDOWN TOGGLE ───
function toggleDropdown(menuId) {
  document.querySelectorAll('.dropdown__menu').forEach(m => {
    if (m.id !== menuId) m.classList.remove('dropdown__menu--open');
  });
  const menu = document.getElementById(menuId);
  if (menu) menu.classList.toggle('dropdown__menu--open');
}

// ─── SELECT PRIORITY ───
function selectPriority(value, label, color) {
  const select = document.getElementById('prioritySelect');
  if (select) select.value = value;

  const lbl = document.getElementById('priorityLabel');
  if (lbl) { lbl.textContent = label; lbl.style.color = color; }

  // update icon color
  const icon = document.getElementById('priorityIcon');
  if (icon) {
    icon.querySelectorAll('path, line').forEach(el => {
      el.setAttribute('fill', color);
      el.setAttribute('stroke', color);
    });
  }

  const menu = document.getElementById('priorityMenu');
  if (menu) menu.classList.remove('dropdown__menu--open');
}

// ─── SELECT CATEGORY ───
function selectCategory(value, label) {
  const select = document.getElementById('categorySelect');
  if (select) select.value = value;

  const lbl = document.getElementById('categoryLabel');
  if (lbl) { lbl.textContent = label; lbl.style.color = '#202020'; }

  // mark selected
  document.querySelectorAll('#categoryMenu .dropdown__item').forEach(item => {
    item.classList.remove('dropdown__item--selected');
  });
  if (event && event.currentTarget) {
    event.currentTarget.classList.add('dropdown__item--selected');
  }

  const menu = document.getElementById('categoryMenu');
  if (menu) menu.classList.remove('dropdown__menu--open');
}

function updateTitle(isOpen) {
  const TitleApp = document.querySelector(".title__head");
  if (!TitleApp) return;

  if (isOpen) {
    TitleApp.classList.add("title__head-show");
  } else {
    TitleApp.classList.remove("title__head-show"); // sidebar closed → show title
  }
}

// ===== SIDEBAR TOGGLE =====
function toggleSidebar() {
  const sidebar = document.getElementById("sidebar");
  const sidebarWrap = document.querySelector(".app-layout__sidebar");
  const isOpen = !sidebar.classList.contains("sidebar--closed");

  if (isOpen) {
    sidebar.classList.add("sidebar--closed");
    sidebarWrap.classList.add("sidebar-collapsed");
    localStorage.setItem("sidebar", "closed");
  } else {
    sidebar.classList.remove("sidebar--closed");
    sidebarWrap.classList.remove("sidebar-collapsed");
    localStorage.setItem("sidebar", "open");
  }

  // ← call after toggling — passes NEW state
  updateTitle(!isOpen);
}

// ===== PAGE LOAD =====
document.addEventListener("DOMContentLoaded", function () {
  const sidebar = document.getElementById("sidebar");
  const sidebarWrap = document.querySelector(".app-layout__sidebar");
  const state = localStorage.getItem("sidebar");

  if (state === "closed") {
    sidebar.classList.add("sidebar--closed");
    sidebarWrap.classList.add("sidebar-collapsed");
  }
});

const btnToggleSideBar = document.getElementById("sidebarToggleBtn");
btnToggleSideBar.addEventListener("click", () => {
  const isOpen = !sidebar.classList.contains("sidebar--closed");
  updateTitle(isOpen);
});

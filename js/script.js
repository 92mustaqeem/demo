/* Shared JavaScript for all pages. */

// ---- EDIT HERE: sample notices. Replace with real ones (newest first). ----
// Fields: title, date (YYYY-MM-DD), category, text
const NOTICES = [
  { title: "Sample: Admission information", date: "2026-10-20", category: "Admissions", text: "Sample text. Replace with the official admission notice." },
  { title: "Sample: Examination schedule", date: "2026-10-15", category: "Examinations", text: "Sample text. Replace with the official date sheet." },
  { title: "Sample: Holiday announcement", date: "2026-10-10", category: "General", text: "Sample text. Replace with the official holiday notice." },
  { title: "Sample: Fee submission reminder", date: "2026-10-05", category: "Fees", text: "Sample text. Replace with the official fee notice." },
  { title: "Sample: Evening class timings", date: "2026-09-28", category: "General", text: "Sample text. Replace with confirmed class timings." },
  { title: "Sample: Seminar for students", date: "2026-09-20", category: "Events", text: "Sample text. Replace with the real event details." }
];
// Contact form target: replace with the college's verified email address.
const CONTACT_EMAIL = "college-email@example.com";

// Escape text before inserting into HTML
const esc = s => String(s).replace(/[&<>"']/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
const fmtDate = d => new Date(d + "T00:00:00").toLocaleDateString("en-GB", { day: "numeric", month: "short", year: "numeric" });
const noticeHTML = (n, cols) => `<div class="${cols}"><article class="card notice-card h-100 border-0 shadow-sm"><div class="card-body">
  <div class="notice-meta mb-1"><i class="bi bi-calendar3"></i> ${fmtDate(n.date)} &nbsp;<span class="badge text-bg-secondary">${esc(n.category)}</span></div>
  <h3 class="h6">${esc(n.title)}</h3><p class="mb-0 small">${esc(n.text)}</p></div></article></div>`;

document.addEventListener("DOMContentLoaded", () => {
  const year = document.getElementById("year"); if (year) year.textContent = new Date().getFullYear();

  // Home: latest 3 notices
  const latest = document.getElementById("latest-notices");
  if (latest) latest.innerHTML = NOTICES.slice(0, 3).map(n => noticeHTML(n, "col-md-4")).join("");

  // Notices page: search + category filter
  const list = document.getElementById("notice-list");
  if (list) {
    const search = document.getElementById("notice-search"), cat = document.getElementById("notice-category"), count = document.getElementById("notice-count");
    [...new Set(NOTICES.map(n => n.category))].sort().forEach(c => cat.insertAdjacentHTML("beforeend", `<option>${esc(c)}</option>`));
    const render = () => {
      const q = search.value.trim().toLowerCase();
      const found = NOTICES.filter(n => (!cat.value || n.category === cat.value) && (n.title + " " + n.text + " " + n.category).toLowerCase().includes(q));
      list.innerHTML = found.length ? found.map(n => noticeHTML(n, "col-md-6")).join("") : '<div class="col-12"><p>No notices match your search.</p></div>';
      count.textContent = found.length + " notice(s) shown";
    };
    search.addEventListener("input", render); cat.addEventListener("change", render); render();
  }

  // Contact form: validate, then open an email draft (no backend)
  const form = document.getElementById("contact-form");
  if (form) form.addEventListener("submit", e => {
    e.preventDefault();
    const ok = form.checkValidity();
    form.querySelectorAll("input,textarea").forEach(f => f.classList.toggle("is-invalid", !f.checkValidity()));
    const status = document.getElementById("form-status");
    if (!ok) { status.textContent = "Please fix the highlighted fields."; return; }
    const v = id => document.getElementById(id).value.trim();
    const body = `Name: ${v("c-name")}\nEmail: ${v("c-email")}\n\n${v("c-message")}`;
    window.location.href = `mailto:${CONTACT_EMAIL}?subject=${encodeURIComponent(v("c-subject"))}&body=${encodeURIComponent(body)}`;
    status.textContent = "Your email app should open with a draft.";
  });
});

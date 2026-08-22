const API_BASE = "http://127.0.0.1:8000";
const params = new URLSearchParams(window.location.search);
const employeeId = params.get("id");

async function loadProfile() {
  const res = await fetch(`${API_BASE}/employees/${employeeId}`);
  const emp = await res.json();

  const initials = emp.Name.split(" ").map(n => n[0]).join("");
  document.getElementById("profile-header").innerHTML = `
    <div class="avatar">${initials}</div>
    <h1>${emp.Name}</h1>
    <p>${emp.Desigation}</p>
  `;

  const isAdmin = emp.role?.toLowerCase() === "admin";
  const tabs = ["Personal", "Private Info", "Security"];
  if (isAdmin) tabs.splice(2, 0, "Salary Info");

  const tabButtons = document.getElementById("tab-buttons");
  const tabContent = document.getElementById("tab-content");

  tabs.forEach((tab, i) => {
    const btn = document.createElement("button");
    btn.className = "tab-btn" + (i === 0 ? " active" : "");
    btn.textContent = tab;
    btn.onclick = () => showTab(tab, tabs, emp);
    tabButtons.appendChild(btn);
  });

  showTab(tabs[0], tabs, emp);
}

function showTab(tab, tabs, emp) {
  document.querySelectorAll(".tab-btn").forEach((btn, i) => {
    btn.classList.toggle("active", tabs[i] === tab);
  });

  const content = document.getElementById("tab-content");
  let html = "";

  if (tab === "Personal") {
    html = `<p>Designation: ${emp.Desigation}</p><p>Role: ${emp.role}</p><p>Status: ${emp.status || "present"}</p>`;
  } else if (tab === "Private Info") {
    html = `<p>Address: ${emp.address || "-"}</p><p>Phone: ${emp.phone || "-"}</p>`;
  } else if (tab === "Salary Info") {
    html = `<p>Monthly Wage: ₹${emp.monthly_wage || "-"}</p>`;
  } else if (tab === "Security") {
    html = `<p>Password/security settings go here.</p>`;
  }

  content.innerHTML = `<div class="tab-panel">${html}</div>`;
}

loadProfile();
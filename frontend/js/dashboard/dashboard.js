const API_BASE = "http://127.0.0.1:8000";

async function loadEmployees() {
  const res = await fetch(`${API_BASE}/employees/`);
  const employees = await res.json();

  const grid = document.getElementById("employee-grid");
  grid.innerHTML = "";

  employees.forEach((emp) => {
    const initials = emp.Name.split(" ").map(n => n[0]).join("");
    const status = emp.status || "present"; // fallback if null

    const card = document.createElement("a");
    card.href = `profile.html?id=${emp.id}`;
    card.className = "card";
    card.innerHTML = `
      <div class="status-dot status-${status}"></div>
      <div class="avatar">${initials}</div>
      <p><strong>${emp.Name}</strong></p>
      <p>${emp.Desigation}</p>
    `;
    grid.appendChild(card);
  });
}

loadEmployees();
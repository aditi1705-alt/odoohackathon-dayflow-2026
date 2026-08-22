const API_URL = window.DAYFLOW_API_URL || "http://127.0.0.1:8000";

function getToken() {
    return localStorage.getItem("access_token");
}

function getStoredUser() {
    try {
        return JSON.parse(
            localStorage.getItem("dayflow_user") || "null"
        );
    } catch {
        return null;
    }
}

async function api(path, options = {}) {

    const headers = {
        "Content-Type": "application/json",
        ...(options.headers || {})
    };

    const token = getToken();

    if (token) {
        headers.Authorization = `Bearer ${token}`;
    }

    const response = await fetch(
        `${API_URL}${path}`,
        {
            ...options,
            headers
        }
    );

    let data = null;

    try {
        data = await response.json();
    } catch {
        // Response has no JSON body
    }

    if (!response.ok) {
        throw new Error(
            data?.detail || "Something went wrong"
        );
    }

    return data;
}

function initials(name = "User") {

    return name
        .split(/\s+/)
        .filter(Boolean)
        .slice(0, 2)
        .map(x => x[0].toUpperCase())
        .join("");
}

function formatTime(value) {

    if (!value) {
        return "--";
    }

    const date = new Date(value);

    if (Number.isNaN(date.getTime())) {
        return "--";
    }

    return date.toLocaleTimeString(
        [],
        {
            hour: "2-digit",
            minute: "2-digit"
        }
    );
}

function showToast(message) {

    let toast = document.querySelector(".toast");

    if (!toast) {

        toast = document.createElement("div");

        toast.className = "toast";

        document.body.appendChild(toast);
    }

    toast.textContent = message;

    toast.classList.add("show");

    setTimeout(() => {
        toast.classList.remove("show");
    }, 2400);
}

function logout() {

    localStorage.removeItem("access_token");
    localStorage.removeItem("refresh_token");
    localStorage.removeItem("dayflow_user");

    const base = window.location.pathname.includes("/pages/")
        ? "login.html"
        : "pages/login.html";
    window.location.href = base;
}

function requireAuth() {

    if (!getToken()) {

        window.location.href = "pages/login.html";

        return false;
    }

    return true;
}

function setupShell(active) {

    const user = getStoredUser();

    const name = user?.email
        ? user.email.split("@")[0]
        : "User";

    document
        .querySelectorAll("[data-user-name]")
        .forEach(el => {
            el.textContent = name;
        });

    document
        .querySelectorAll("[data-user-initials]")
        .forEach(el => {
            el.textContent = initials(name);
        });

    document
        .querySelectorAll(".nav a[data-page]")
        .forEach(link => {

            link.classList.toggle(
                "active",
                link.dataset.page === active
            );

        });

    document
        .querySelectorAll("[data-logout]")
        .forEach(btn => {

            btn.addEventListener(
                "click",
                logout
            );

        });
}
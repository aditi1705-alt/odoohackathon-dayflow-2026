const API_URL = "http://127.0.0.1:8000";

const signupForm = document.getElementById("signup-form");
const signupButton = document.getElementById("signup-button");
const signupMessage = document.getElementById("signup-message");

signupForm.addEventListener("submit", async (event) => {
    event.preventDefault();

    const email = document.getElementById("email").value.trim();
    const password = document.getElementById("password").value;
    const confirmPassword = document.getElementById("confirm-password").value;

    signupMessage.textContent = "";

    if (password !== confirmPassword) {
        signupMessage.textContent = "Passwords do not match.";
        return;
    }

    signupButton.disabled = true;
    signupButton.textContent = "Creating account...";

    try {
        const response = await fetch(`${API_URL}/auth/signup`, {
            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                email,
                password
            })
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.detail || "Signup failed");
        }

        signupMessage.textContent = "Account created successfully.";

        setTimeout(() => {
            window.location.href = "login.html";
        }, 1000);

    } catch (error) {

        signupMessage.textContent = error.message;

    } finally {

        signupButton.disabled = false;
        signupButton.textContent = "Create Account";
    }
});
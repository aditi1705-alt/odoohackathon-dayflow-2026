const loginForm = document.getElementById("login-form");
const loginButton = document.getElementById("login-button");
const loginMessage = document.getElementById("login-message");

const emailInput = document.getElementById("email");
const passwordInput = document.getElementById("password");


loginForm.addEventListener("submit", async (event) => {

    event.preventDefault();

    loginMessage.className = "auth-message";
    loginMessage.textContent = "";

    loginButton.disabled = true;
    loginButton.textContent = "Signing in...";


    try {

        const data = await api(
            "/auth/login",
            {
                method: "POST",

                body: JSON.stringify({
                    email: emailInput.value.trim(),
                    password: passwordInput.value
                })
            }
        );


        localStorage.setItem(
            "access_token",
            data.access_token
        );


        if (data.refresh_token) {

            localStorage.setItem(
                "refresh_token",
                data.refresh_token
            );

        }


        localStorage.setItem(
            "dayflow_user",
            JSON.stringify(
                data.user || {
                    email: emailInput.value.trim()
                }
            )
        );


        loginMessage.className =
            "auth-message success";

        loginMessage.textContent =
            "Signed in. Opening workspace...";


        setTimeout(() => {

            /*
             * CHANGE THIS WHEN THE REAL DASHBOARD
             * PAGE IS READY.
             */
            window.location.href = "../index.html";

        }, 350);


    } catch (error) {

        loginMessage.className =
            "auth-message error";

        loginMessage.textContent =
            error.message;

    } finally {

        loginButton.disabled = false;
        loginButton.textContent = "Sign in";

    }

});
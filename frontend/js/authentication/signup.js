const signupForm = document.getElementById("signup-form");
const signupButton = document.getElementById("signup-button");
const signupMessage = document.getElementById("signup-message");

const emailInput = document.getElementById("email");
const passwordInput = document.getElementById("password");
const confirmPasswordInput =
    document.getElementById("confirm-password");


signupForm.addEventListener("submit", async (event) => {

    event.preventDefault();

    signupMessage.className = "auth-message";
    signupMessage.textContent = "";


    if (
        passwordInput.value !==
        confirmPasswordInput.value
    ) {

        signupMessage.className =
            "auth-message error";

        signupMessage.textContent =
            "Passwords do not match.";

        return;
    }


    signupButton.disabled = true;
    signupButton.textContent = "Creating account...";


    try {

        await api(
            "/auth/signup",
            {
                method: "POST",

                body: JSON.stringify({
                    email: emailInput.value.trim(),
                    password: passwordInput.value
                })
            }
        );


        signupMessage.className =
            "auth-message success";

        signupMessage.textContent =
            "Account created successfully.";


        setTimeout(() => {

            window.location.href =
                "login.html";

        }, 900);


    } catch (error) {

        signupMessage.className =
            "auth-message error";

        signupMessage.textContent =
            error.message;

    } finally {

        signupButton.disabled = false;
        signupButton.textContent = "Create account";

    }

});
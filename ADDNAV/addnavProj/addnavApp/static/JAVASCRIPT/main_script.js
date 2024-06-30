document.addEventListener("DOMContentLoaded", function () {
    // Signup Script
    const toggleSignupPassword = document.querySelector("#toggleSignupPassword");
    const signupPassword = document.querySelector("#signup-password");

    if (toggleSignupPassword && signupPassword) {
        toggleSignupPassword.addEventListener("click", function () {
            const type = signupPassword.getAttribute("type") === "password" ? "text" : "password";
            signupPassword.setAttribute("type", type);
            this.querySelector("img").src = type === "password" ? "{% static 'images/password.png' %}" : "{% static 'images/pass-on.png' %}";
        });
    }

    // Login Script
    const togglePassword = document.getElementById("togglePassword");
    const passwordField = document.getElementById("password");

    if (togglePassword && passwordField) {
        togglePassword.addEventListener("click", function() {
            const passwordFieldType = passwordField.getAttribute("type") === "password" ? "text" : "password";
            passwordField.setAttribute("type", passwordFieldType);
            this.querySelector("img").src = passwordFieldType === "text" ? "{% static 'images/pass-on.png' %}" : "{% static 'images/password.png' %}";
        });
    }

    // FAQ Script
    const faqItems = document.querySelectorAll(".faq-item");

    if (faqItems.length > 0) {
        faqItems.forEach(item => {
            const button = item.querySelector(".faq-question button");
            const answer = item.querySelector(".faq-answer");

            if (button && answer) {
                button.addEventListener("click", () => {
                    const isVisible = answer.classList.contains("show");

                    // Hide all answers and reset buttons
                    document.querySelectorAll(".faq-answer").forEach(answer => answer.classList.remove("show"));
                    document.querySelectorAll(".faq-question button").forEach(btn => btn.textContent = "+");

                    // Toggle the clicked one
                    if (isVisible) {
                        answer.classList.remove("show");
                        button.textContent = "+";
                    } else {
                        answer.classList.add("show");
                        button.textContent = "-";
                    }
                });
            }
        });
    }
});


const password = document.getElementById("password");
const showPassword = document.getElementById("show-password");
const newPassword = document.getElementById("newPassword");
const hover = document.getElementById("hover")


if (showPassword) {
    showPassword.addEventListener('click', function () {
        showPassword.classList.toggle('fa-eye');
        showPassword.classList.toggle('fa-eye-slash');

        if (password.type === 'password') {
            hover.textContent = 'Hide password';
            password.type = 'text';
            newPassword.type = 'text';

        }
        else {
            password.type = 'password';
            newPassword.type = 'password';
            hover.textContent = 'Show password';
        }

    });
}










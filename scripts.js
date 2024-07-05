document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');
    const usernameInput = document.getElementById('username');
    const passwordInput = document.getElementById('password');

    form.addEventListener('submit', function(event) {
        let valid = true;

        if (usernameInput.value.trim() === '') {
            alert('Username is required.');
            valid = false;
        }

        if (passwordInput.value.trim() === '') {
            alert('Password is required.');
            valid = false;
        }

        if (!valid) {
            event.preventDefault();
        }
    });
});

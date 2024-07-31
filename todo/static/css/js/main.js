function checkAuthStatus() {
    fetch('/authentication/check-auth-status/')
        .then(response => response.json())
        .then(data => {
            if (data.is_authenticated) {
                window.location.href = '/';
            }
        });
}
document.addEventListener('DOMContentLoaded', checkAuthStatus);

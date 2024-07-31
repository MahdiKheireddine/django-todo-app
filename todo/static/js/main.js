function checkAuthStatus() {
    console.log('Checking auth status');

    // Check if redirection has already been handled
    if (localStorage.getItem('redirected')) {
        return;
    }

    fetch('/authentication/check-auth-status/')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            console.log('Auth data:', data);
            if (data.is_authenticated && window.location.pathname !== '/') {
                localStorage.setItem('redirected', 'true');
                window.location.href = '/';
            }
        })
        .catch(error => {
            console.error('Error checking authentication status:', error);
        });
}

document.addEventListener('DOMContentLoaded', checkAuthStatus);

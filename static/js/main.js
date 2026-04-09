// SlickDesk - main.js

// Auto-dismiss alerts after 4 seconds
document.addEventListener('DOMContentLoaded', () => {
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        setTimeout(() => {
            alert.style.transition = 'opacity 0.5s';
            alert.style.opacity = '0';
            setTimeout(() => alert.remove(), 500);
        }, 4000);
    });

    // Highlight current nav link
    const links = document.querySelectorAll('.nav-links a');
    links.forEach(link => {
        if (link.href === window.location.href) {
            link.style.color = '#00d4ff';
        }
    });
});

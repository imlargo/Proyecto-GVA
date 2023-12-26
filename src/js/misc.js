function changeMode(button) {
    const body = document.body;
    const isDark = body.classList.contains('dark');

    if (isDark) {
        body.classList.remove('dark');
        button.classList = "bi bi-moon theme-button";
    } else {
        body.classList.add('dark');
        button.classList = "bi bi-brightness-low theme-button";
    }
}
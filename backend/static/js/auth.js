const form = document.getElementById('auth-form');

if (form) {
    const errorMessageDiv = document.getElementById('error-message');

    form.addEventListener('submit', async function (event) {
        event.preventDefault();

        errorMessageDiv.textContent = '';
        const formData = new FormData(form);

        try {
            const response = await fetch(form.action, {
                method: 'POST',
                body: formData,
            });

            const result = await response.json();
			console.log(result)

            if (result.success) {
                console.log("Successfully log-in !")
            } else {
                console.log("Error trying to log-in !")
                errorMessageDiv.textContent = result.error || 'Login failed. Please try again.';
            }
        } catch (error) {
            console.error('Error:', error);
            errorMessageDiv.textContent = 'An unexpected error occurred. Please try again.';
        }
    });
}
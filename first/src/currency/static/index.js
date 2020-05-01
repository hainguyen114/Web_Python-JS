document.addEventListener('DOMContentLoaded', () => {

    document.querySelector('#form').onsubmit = () => {
<<<<<<< HEAD

        // Initialize new request
        const request = new XMLHttpRequest();
        const currency = document.querySelector('#currency').value;
        request.open('POST', '/convert');

        // Callback function for when request completes
        request.onload = () => {

            // Extract JSON data from request
            const data = JSON.parse(request.responseText);

            // Update the result div
            if (data.success) {
                const contents = `1 USD is equal to ${data.rate} ${currency}.`
=======
        request = new XMLHttpRequest();
        const currency = document.querySelector('#currency').value;
        request.open('POST', '/convert');

        request.onload = () => {
            const data = JSON.parse(request.responseText)

            if (data.success) {
                const contents = `1 USD is equal to ${data.rate} ${currency}.`;
>>>>>>> 3e5626ed68f221bedb6f9b976e74fd2cacf1a4d2
                document.querySelector('#result').innerHTML = contents;
            }
            else {
                document.querySelector('#result').innerHTML = 'There was an error.';
            }
        }

<<<<<<< HEAD
        // Add data to send with request
        const data = new FormData();
        data.append('currency', currency);

        // Send request
=======
        const data = new FormData();
        data.append('currency', currency);
>>>>>>> 3e5626ed68f221bedb6f9b976e74fd2cacf1a4d2
        request.send(data);
        return false;
    };
});
// Get the input fields

const query = document.getElementById("query")
const submitBtn = document.getElementById("submitBtn")




// submitBtn.addEventListener('click', function (e) {
//     performSearch(query)
// })


function performSearch(query) {
    const url = `/blog/search?query=${query.value}`;

    return fetch(url)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return true;
        }).then(() => {
            Location: reload()
        })
        .catch(error => {
            // Handle any errors that occurred during the fetch operation
            console.log('Error:', error);
            return true
        });
}
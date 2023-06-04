// Bring in the values you need to play with
const posts = document.getElementById("posts")
// URL to pull all posts
const url = "{% url 'blog:post_list' %}"

// Create headers and options for the fetch request
const headers = {
    "content-type": "application/json"
}

const options = {
    method: "GET",
    headers: headers
}

// Start loading the posts at
let start = 0;
// quantity of posts to load is 
let end = 3;

// Attatch a scroll event listener to the window object
window.onscroll = function () {
    if (window.innerHeight + window.scrollY > document.body.offsetHeight) {
        // load some more post when the user reaches end of page
        loadData(options, url, start, end)
        start += end;
        end = start + 3
    }
}

function loadData(options, url, start, end) {
    fetch(`${url}?start=${start}&end=${end}`, options)
        .then(response => response.json())
        .then(data => {
            // create post element
            data.forEach(post => {
                createPostElement(posts, post)
            });
        })

}

// function to create the post element and append to the page
function createPostElement(container, post) {
    container.innerHTML = "The posts are on their way"
    // create divs to make up the post element
    let postDiv = document.createElement("div")
    postDiv.className = "post"
    let infoDiv = document.createElement("div")
    infoDiv.className = "info"
    let postContentContainerDiv = document.createElement("div")
    postContentContainerDiv.className = "post-content-container"
    let postContentTextDiv = document.createElement("div")
    postContentTextDiv.className = "post-content-text"
    let postContentImageDiv = document.createElement("div")
    postContentImageDiv.className = "post-content-image"
    let tagsDiv = document.createElement("div")
    tagsDiv.className = "tags"


    let lineDiv = document.createElement("div")
    lineDiv.className = "line"


    let authorName = document.createElement("p")
    authorName.className = "author-name"
    authorName.innerText = "Miclem Abasie"
    let timeAgo = document.createElement("p")
    timeAgo.className = "time-ago"
    timeAgo.innerText = post.created
    // create element to hold images
    let authorImage = new Image()
    authorImage.src = post.image
    let postImage = new Image()
    authorImage.ser = post.image
    authorImage.className = "author-image"

    let postTitle = document.createElement("h2")
    // Create a new anchor element
    const anchor = document.createElement('a');
    // Set the href attribute
    anchor.setAttribute('href', post.url);
    // Set the text content
    anchor.textContent = post.title;
    postTitle.innerHTML = anchor

    // body paragraph
    let pbody = document.createElement("p")
    pbody.innerHTML = post.intro


    console.log(post)


}
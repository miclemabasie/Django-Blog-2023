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

loadData(options, url, 0, 3)
start += end;
end = start + 3
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
            if (data.message) {
                console.log("End of page")
            } else {
                data.forEach(post => {
                    createPostElement(posts, post)
                });

            }
        })

}

// function to create the post element and append to the page
function createPostElement(container, post) {


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
    authorImage.className = "author-image"
    let postImage = new Image()
    postImage.src = post.image
    postImage.className = "post-content-image"

    let postTitle = document.createElement("h2")
    // Create a new anchor element
    const anchor = document.createElement('a');
    // Set the href attribute
    anchor.setAttribute('href', post.url);
    // Set the text content
    anchor.textContent = post.title;
    postTitle.innerHTML = post.id

    // body paragraph
    let pbody = document.createElement("p")
    pbody.innerHTML = post.intro

    // create divs to make up the post element
    let postDiv = document.createElement("div")
    postDiv.className = "post"

    let infoDiv = document.createElement("div")
    infoDiv.className = "info"
    infoDiv.appendChild(authorImage)
    infoDiv.appendChild(authorName)
    infoDiv.appendChild(timeAgo)

    let postContentTextDiv = document.createElement("div")
    postContentTextDiv.className = "post-content-text"
    postContentTextDiv.appendChild(postTitle)
    postContentTextDiv.appendChild(pbody)

    let postContentContainerDiv = document.createElement("div")
    let postContentImageDiv = document.createElement("div")
    postContentImageDiv.appendChild(postImage)
    postContentContainerDiv.className = "post-content-container"
    postContentContainerDiv.appendChild(postContentTextDiv)
    postContentContainerDiv.appendChild(postContentImageDiv)



    let tagsDiv = document.createElement("div")
    tagsDiv.className = post.tags[0]

    postDiv.appendChild(infoDiv)
    postDiv.appendChild(postContentContainerDiv)
    postDiv.appendChild(tagsDiv)

    container.appendChild(postDiv)

}
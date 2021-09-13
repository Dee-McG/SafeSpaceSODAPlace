function showComments(id) {
    comments = document.getElementById("comments-" + id);
    if (comments.hasAttribute('hidden')) {
        comments.removeAttribute("hidden");
    }
    else {
        comments.setAttribute("hidden", true);
    }
}
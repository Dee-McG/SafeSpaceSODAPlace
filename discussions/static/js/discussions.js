/*---------------------------------------Django CSRF Token---------------------------------------*/

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        // Does this cookie string begin with the name we want?
        if (cookie.substring(0, name.length + 1) === (name + '=')) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }
  const csrftoken = getCookie('csrftoken');

/*--------------------------------------Show place comment--------------------------------------*/

let topic;

function showComments(id) {
    comments = document.getElementById("comments-" + id);
    if (comments.hasAttribute('hidden')) {
        comments.removeAttribute("hidden");
    }
    else {
        comments.setAttribute("hidden", true);
    }

    topic = id;
}

/*----------------------------------------Create an idea----------------------------------------*/

function sendComment(id) {
        url = `/discussions/create/`;

        let comment = document.getElementById('user-comment-'+id).value;
        let user = document.getElementById('get_id').innerHTML;

        console.log(id);
        console.log(comment);
        console.log(user);


        fetch(url, {
            method: 'POST',
            headers: {
              'Content-type': 'application/json',
              'X-CSRFToken': csrftoken,
            },
            body: JSON.stringify({
              'topic': id,
              'content': comment,  
              'user': user
            })
          }).then(function (response) {
            location.reload();
          });
    }

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

/*----------------------------------------Create an idea----------------------------------------*/

url = `/ideas/create/`;
const form = document.getElementById('ideaForm');

form.addEventListener('submit', function (e) {
  e.preventDefault();

  let idea_message = document.getElementById('idea_message').value;
  let board_id = document.getElementById('board_id').innerHTML;
  let user_id = document.getElementById('user_id').innerHTML;

  fetch(url, {
    method: 'POST',
    headers: {
      'Content-type': 'application/json',
      'X-CSRFToken': csrftoken,
    },
    body: JSON.stringify({
      'user': user_id,
      'closed': false,  
      'idea_message': idea_message,
      'board': board_id
    })
  }).then(function (response) {
    location.reload();
  });
});

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

/*----------------------------------------Create a board----------------------------------------*/

url = `/ideas/board_create/`;
const form = document.getElementById('boardForm');

form.addEventListener('submit', function (e) {
  e.preventDefault();

  let id_code = document.getElementById('id_code').value;
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
      'id_code': id_code
    })
  }).then(function (response) {
    //location.reload();
  });
});
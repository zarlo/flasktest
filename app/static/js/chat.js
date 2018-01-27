var islogedin = true;

var socket = io.connect('/chat');

//socket.emit('join', "test");

$(function() {
  $('#chatlog').scrollTop($('#chatlog')[0].scrollHeight)
});

socket.on('chat', function(data) {
  addtolog(data);
});

function addtolog(msg) {

  $('#Chat').append('<li>' + msg + '</li>');
  $('#chatlog').scrollTop($('#chatlog')[0].scrollHeight)
}

function login() {

}

function sendText() {
  if (islogedin == false) {
    addtolog("you need to set a user name");
  }
  if ($('#m').val().replace(/\s/g, '') == '') {
    return;
  }
  socket.emit('chat', $('#m').val());
  $('#m').val('');

}

$(document).keypress(function(e) {
  if (e.which == 13) {
    sendText();
  }
});

var socket = io.connect('http://' + document.domain + ':' + location.port);

socket.on( 'connect', function() {
  socket.emit( 'session', {
    data: 'User Connected'
  } )
  var form = $( 'form' ).on( 'submit', function( e ) {
    e.preventDefault()
    let user_name = $( 'input.username' ).val()
    socket.emit( 'session', {
      user_name : user_name,
    } )
  } )
} )

socket.on( 'my response', function( msg ) {
  console.log( 'Works!~', msg )
})

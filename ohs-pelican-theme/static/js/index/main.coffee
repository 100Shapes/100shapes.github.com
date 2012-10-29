
$window = $(window)
$body = $('body')
speed =
	background: 0.3

$window.scroll ->
	console.log 'hello'

	offset = Math.floor $window.scrollTop()
	$('body').css('background-position', "0 -#{offset * speed.background }px")
	return


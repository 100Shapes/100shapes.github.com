
$window = $(window)
$background = $('.background')
$nav = $('nav')
$nav_links = $('nav a')

nav_flip = 777
pink = "#C47382"
light = "#eee"

speed =
	background: 0.90

$window.scroll ->
	if pageYOffset > nav_flip
		$nav.css('background-color', light)
		$nav_links.css('color', pink)
	else
		$nav.css('background-color', "transparent")
		$nav_links.css('color', "#fff")
return



#		background-color: transparent;

#		a {
#			color: #fff;
#
#		}

	# $background.css('top', "#{pageYOffset}px")
	# $('nav').css('top', "#{pageYOffset}px")




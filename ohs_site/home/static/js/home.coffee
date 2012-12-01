
$window = $(window)

$nav = $('nav')
$nav_links = $('nav a')

$nav_about = $('.nav-about')
$nav_work = $('.nav-work')
$nav_contact = $('.nav-contact')
$nav_logo = $('.nav-logo')

$about = $('.about')
$work = $('.work')
$contact = $('.contact')

$intro_btn = $('.intro a')
$about_btn = $('.about a')

scroll_duration = 800
nav_flip = 777
pink = '#C47382'
light = '#eee'

$intro_btn.click (e) =>
	e.preventDefault()
	$about.ScrollTo({duration: scroll_duration})

$about_btn.click (e) =>
	e.preventDefault()
	$work.ScrollTo({duration: scroll_duration})

$nav_logo.click (e) => 
	e.preventDefault()
	$('body').ScrollTo({duration: scroll_duration})

$nav_about.click (e) => 
	e.preventDefault()
	$about.ScrollTo({duration: scroll_duration})

$nav_work.click (e) => 
	e.preventDefault()
	$work.ScrollTo({duration: scroll_duration})

$nav_contact.click (e) => 
	e.preventDefault()
	$contact.ScrollTo({duration: scroll_duration})

$window.scroll ->
	if pageYOffset > nav_flip
		$nav.css({'background-color': light, 'border-bottom-style' : 'solid'})
		$nav_links.css('color', pink)
		$nav_logo.css('background-image', "url('../theme/img/logo_small_pink.png')")
	else
		$nav.css({'background-color': 'transparent', 'border-bottom-style' : 'none'})
		$nav_links.css('color', "#fff")
		$nav_logo.css('background-image', "url('../theme/img/logo_small_white.png')")
return



#		background-color: transparent;

#		a {
#			color: #fff;
#
#		}

	# $background.css('top', "#{pageYOffset}px")
	# $('nav').css('top', "#{pageYOffset}px")



class Header

	transparentClassName: 'transparent',

	constructor: (@$el, @threshold) ->
		@$body = $ 'body'
		if @$body.width() > 800
			window.onscroll = @.refresh
		else
			if @isTransparent()
				return @$el.removeClass @transparentClassName
		@.refresh()

	refresh: =>
		scrollPosition = Math.max @$body.scrollTop(), 0
		if scrollPosition < @threshold
			if not @isTransparent()
				@$el.addClass @transparentClassName
		else
			if @isTransparent()
				@$el.removeClass @transparentClassName

	isTransparent: =>
		@$el.hasClass @transparentClassName

banner = $('.banner')
header = new Header banner, 800

$body = $('body')
$('a.jump-btn').click (evnt) ->
	evnt.preventDefault()
	$body.animate (scrollTop: $(this.hash).offset().top), 500
	false

$('.carousel').carousel({interval: 5000})


# $window = $(window)
# $sections = $('section')
# $nav = $('nav')
# $nav_links = $('nav a')

# $nav_about = $('.nav-about')
# $nav_work = $('.nav-work')
# $nav_contact = $('.nav-contact')
# $nav_logo = $('.nav-logo')
# $nav_logo_pink = $('.nav-logo.pink')

# $about = $('.about')
# $work = $('.work')
# $contact = $('.contact')

# $intro_btn = $('.intro a')
# $about_btn = $('.about a')

# scroll_duration = 800
# nav_flip = 640
# pink = '#C47382'
# light = '#eee'


# $intro_btn.click (e) =>
# 	e.preventDefault()
# 	$about.ScrollTo({duration: scroll_duration})

# $about_btn.click (e) =>
# 	e.preventDefault()
# 	$work.ScrollTo({duration: scroll_duration})

# $nav_logo.click (e) => 
# 	e.preventDefault()
# 	$('body').ScrollTo({duration: scroll_duration})

# $nav_about.click (e) => 
# 	e.preventDefault()
# 	$about.ScrollTo({duration: scroll_duration})

# $nav_work.click (e) => 
# 	e.preventDefault()
# 	$work.ScrollTo({duration: scroll_duration})

# $nav_contact.click (e) => 
# 	e.preventDefault()
# 	$contact.ScrollTo({duration: scroll_duration})

# $window.scroll ->
# 	if pageYOffset > nav_flip
# 		$nav.css({'background-color': light, 'border-bottom-style' : 'solid'})
# 		$nav_links.css('color', pink)
# 		$nav_logo.removeClass('white')
# 	else
# 		$nav.css({'background-color': 'transparent', 'border-bottom-style' : 'none'})
# 		$nav_links.css('color', "#fff")
# 		$nav_logo.addClass('white')


// Generated by CoffeeScript 1.4.0
(function() {
  var $background, $nav, $nav_links, $window, light, nav_flip, pink, speed;

  $window = $(window);

  $background = $('.background');

  $nav = $('nav');

  $nav_links = $('nav a');

  nav_flip = 777;

  pink = "#C47382";

  light = "#eee";

  speed = {
    background: 0.90
  };

  $window.scroll(function() {
    if (pageYOffset > nav_flip) {
      $nav.css('background-color', light);
      return $nav_links.css('color', pink);
    } else {
      $nav.css('background-color', "transparent");
      return $nav_links.css('color', "#fff");
    }
  });

  return;

}).call(this);

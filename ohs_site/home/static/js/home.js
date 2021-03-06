// Generated by CoffeeScript 1.3.3
var $body, Header, banner, header,
  __bind = function(fn, me){ return function(){ return fn.apply(me, arguments); }; };

Header = (function() {

  Header.prototype.transparentClassName = 'transparent';

  function Header($el, threshold) {
    this.$el = $el;
    this.threshold = threshold;
    this.isTransparent = __bind(this.isTransparent, this);

    this.refresh = __bind(this.refresh, this);

    this.$body = $('body');
    if (this.$body.width() > 800) {
      window.onscroll = this.refresh;
    } else {
      if (this.isTransparent()) {
        return this.$el.removeClass(this.transparentClassName);
      }
    }
    this.refresh();
  }

  Header.prototype.refresh = function() {
    var scrollPosition;
    scrollPosition = Math.max(this.$body.scrollTop(), 0);
    if (scrollPosition < this.threshold) {
      if (!this.isTransparent()) {
        return this.$el.addClass(this.transparentClassName);
      }
    } else {
      if (this.isTransparent()) {
        return this.$el.removeClass(this.transparentClassName);
      }
    }
  };

  Header.prototype.isTransparent = function() {
    return this.$el.hasClass(this.transparentClassName);
  };

  return Header;

})();

banner = $('.banner');

header = new Header(banner, 800);

$body = $('body');

$('a.jump-btn').click(function(evnt) {
  evnt.preventDefault();
  $body.animate({
    scrollTop: $(this.hash).offset().top
  }, 500);
  return false;
});

$('.carousel').carousel({
  interval: 5000
});

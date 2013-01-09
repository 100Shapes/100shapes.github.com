$(".carousel-nav a").click(function(e){
    e.preventDefault();
    var index = parseInt($(this).attr('data-to'));
    $('.carousel').carousel(index);
    var nav = $('.carousel-nav');
    var item = nav.find('a').get(index);
    nav.find('a.active').removeClass('active');
    $(item).addClass('active');
});

$(".carousel").bind('slide', function(e) {
    //e.preventDefault();
    var elements = 3;
    var nav = $('.carousel-nav');
    var index = $('.carousel').find('.item.active').index();
    index = (index == elements - 1) ? 0 : index + 1;
    var item = nav.find('a').get(index);
    nav.find('a.active').removeClass('active');
    $(item).addClass('active');
});

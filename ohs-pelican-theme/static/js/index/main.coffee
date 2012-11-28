
$window = $(window)
$body = $('body')
speed =
	background: 0.90

$window.scroll ->
	$('body').css('background-position', "0 #{pageYOffset * speed.background }px")
	return

function draw() {
  var canvas = document.getElementById("canvas");
  var ctx = canvas.getContext("2d");
ctx.save();
ctx.fillStyle = "rgba(0, 0, 0, 0)";
ctx.strokeStyle = "#000000";
ctx.lineWidth = 8;
ctx.beginPath();
ctx.moveTo(400,300);
ctx.lineTo(400,1025);
ctx.bezierCurveTo(400,1095,417,1132,258,1213);
ctx.bezierCurveTo(258,1213,5,1323,5,1600);
ctx.bezierCurveTo(5,1838.677,154.23,1927.38,314,1980.622);
ctx.fill();
ctx.stroke();
ctx.restore();
};

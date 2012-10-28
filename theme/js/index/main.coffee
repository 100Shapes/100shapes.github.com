
$window = $(window)
$line = $('#line')
$point = $('#point')
$svg = $('svg')
$h1 = $('h1')

initY = 300
initX = $window.width() / 2



# Functions
Point = (x,y) ->
  if !x
    x = 0
  if !y
    y = 0
  {x: x, y: y}

B_21 = (t) ->
  t*t
B_22 = (t) ->
  2*t*(1-t)
B_23 = (t) ->
  (1-t)*(1-t)
B_31 = (t) ->
  t*t*t
B_32 = (t) ->
  3*t*t*(1-t)
B_33 = (t) ->
  3*t*(1-t)*(1-t)
B_34 = (t) ->
  (1-t)*(1-t)*(1-t)

bezier_2 = (t, p1, p2, p3) ->
  r = Point()
  r.x = Math.ceil(p1.x * B_21(t) + p2.x * B_22(t) + p3.x * B_23(t))
  r.y = Math.ceil(p1.y * B_21(t) + p2.y * B_22(t) + p3.y * B_23(t))
  r

bezier_3 = (t, p1, p2, p3, p4) ->
  r = Point()
  r.x = Math.ceil(p1.x * B_31(t) + p2.x * B_32(t) + p3.x * B_33(t) + p4.x * B_34(t))
  r.y = Math.ceil(p1.y * B_31(t) + p2.y * B_32(t) + p3.y * B_33(t) + p4.y * B_34(t))
  r


p_0 = Point(initX, initY)
p_1 = Point(initX - 200, initY + 200)
p_2 = Point(initX+200, 700)
p_3 = Point(initX, 700)

drawLine = (p0, p1, p2, p3) ->
  $line.attr "d", "M #{p0.x}, #{p0.y} Q #{p1.x}, #{p1.y} #{p2.x}, #{p2.y} T #{p3.x}, #{p3.y}" 


scrollableArea = $('body').height() - $window.height() # minus window size!!


updateLine = (t, p0, p1, p2, p3) ->

  # q is the dot the defines the Bezier curve  
  q = bezier_3(t, p0, p1, p2, p3)
  # q --> p_3

  c = bezier_2(t, p0, p1, q)
  # c --> q

  drawLine p0, p1, c, q

updateLine(0, p_0, p_1, p_2, p_3)

$window.scroll ->


  t =  ($window.scrollTop() / scrollableArea)
  if t > 1
    t = 1


  # Move the header
  $h1.css 'top', 240 + Math.ceil($window.scrollTop() * $h1.data 'speed')

  # Move the svg component
  p_0 = Point(initX, initY + Math.ceil($window.scrollTop() * $svg.data 'speed'))

  updateLine(t, p_0, p_1, p_2, p_3)
  


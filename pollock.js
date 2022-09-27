var canvas = document.querySelector('canvas');

canvas.width = innerWidth;
canvas.height = innerHeight;

var c = canvas.getContext('2d');

c.fillRect(100, 100, 10, 10);

console.log(canvas);
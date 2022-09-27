// JavaScript source code
const canvas = document.getElementById('canvas1')

canvas.width = innerWidth;
canvas.height = innerHeight;

var c = canvas.getContext('2d');

let img_pollock;
img_pollock = document.getElementById('img_pollock');
let img_pollock2;
img_pollock2 = document.getElementById('img_pollock2');
let img_pollock3;
img_pollock3 = document.getElementById('img_pollock3');

let btn_clear;
let btn_exit;

const pallet0 = [
    'white',               //white  0
    'DarkOliveGreen',      //tan   1
    'SandyBrown',          //orange 2
    'PapayaWhip',          //tan    3
    'FireBrick',           //orange 4
    'SlateGrey',           //brown  5     
    'DarkCyan',            //red    6
    'Black'                //black 7
]	

const button = document.getElementById('button');

var bg_color = 'White';
var current_pallet = pallet0;
var dibble_COLORS = []
var dribble_COLORS = current_pallet;
var color_choice = 0;
var radius = 10;
var dragging = false;
var oldX = 0;
var oldY = 0;
var delta = 0;
var brush_num = 4;
var dribble_count = 0;
var randColor_Opt = true;

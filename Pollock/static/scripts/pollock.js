const canvas = document.getElementById('canvas1')
canvas.width = innerWidth;
canvas.height = innerHeight-135;
var c = canvas.getContext('2d');
var dataUrl = canvas.toDataURL("image/png");

var img = new Image();
img.crossOrigin = "Anonymous";
//img.data = c.getImageData(400, 0, 1000, 600);

//var img
//img = new Image();
//img.data = dataUrl; // c.createImageData(600, 600);
//

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

const pallet1 = [
     'white',               //white  0
     'Grey',                //grey   1
     'Brown',               //red  brn2
     'GoldenRod',           //tan    3
     'Thistle',             //orange 4
     'DimGrey',             //brown  5     
     'MediumBlue',          //blue   6
     'Black'                //black  7
]	

const pallet2 = [
     'white',           //white  0
     'Maroon',          //rust   1
     'OrangeRed',       //red    2
     'Peru',            //orange 3
     'DarkGoldenRod',   //tan    4    
     'DarkSlateGray',   //brown  5     
     'Cyan',            //teal   6
     'Black'            //black  7
]	

const button = document.getElementById('button');

var bg_color = 'White';
var COLORS = [];
var current_pallet = pallet0;
var COLORS = current_pallet;
var dibble_COLORS = []
var dribble_COLORS = current_pallet;
var color_choice;
var radius = 10;
var dragging = false;
var oldX;
var oldY;
var delta;
var brush_num;
var oldX = 0;
var oldY = 0;
var delta = 0;
var dribble_count = 0;
var brush_num = 4;
var randColor_Opt;
randColor_Opt = false;
color_choice = 0;
const arr = new Uint8ClampedArray(40_000);

var putPoint = function (e, dragging, dribble_COLORS, COLORS) {
    c2 = canvas.getContext('2d');
    delta = (e.clientX * e.clientX) + (e.clientY * e.clientY);
    if (e.clientX > 410) {
        if (e.clientX < 1400) {
            if (e.clientY > 90) {
                if (e.clientY < 676 - radius) {
                    c.beginPath();
                    c.arc(e.clientX, e.clientY - 75, radius, 0, Math.PI * 2);
                    c.fill();
                    c.arc(1800 - e.clientX, 700 - e.clientY, radius, 0, Math.PI * 2);
                    c.fill();
                }
                else dragging = false;
            }
            else dragging = false;
        }
        else dragging = false;
    }
    else dragging = false;
    radius -= (delta / 30000000);    
    if (radius<=0){
        radius = 0;
    }
    oldX = e.clientX;
    oldY = e.clientY;
    dribble(e, dribble_COLORS);    
}

var dribble = function (e) {
    temp = c.fillStyle;
    dribble_count += 1;
    if (dribble_count > 1) {
        ranX = (Math.random() * 160) - 80;
        ranY = (Math.random() * 160) - 80;
        ranR1 = Math.random() * 10;
        ranR2 = Math.random() * 10;
        if (e.clientX - ranX > 520) {
            if (e.clientX + ranX < 1400) {
                if (e.clientY + ranY > 90) {
                    if (e.clientY + ranY < 676 - radius) {
                        c.beginPath();
                        if (randColor_Opt) {
                            ranC = Math.round(Math.random() * 7);
                            c.fillStyle = dribble_COLORS[ranC];
                        }
                        c.arc(e.clientX + ranX, e.clientY + ranY - 75, ranR1, 0, Math.PI * 2);
                        c.arc(1900 - e.clientX + ranX, 670 - e.clientY + ranY, ranR2, 0, Math.PI * 2);
                        c.fill();
                        dribble_count = 0;
                    }
                }
            }
        }

    }
    c.fillStyle = temp;
}

var color_check = function (e){
    if (e.clientY > 164) {
        if (e.clientY < 196) {
            if (e.clientX > 189) {
                if (e.clientX < 216) {
                    brush_num = 8;
                    c.fillStyle = current_pallet[7]
                }
                else if (e.clientX < 246) {
                    brush_num = 5;
                    c.fillStyle = current_pallet[4]
                }
                else if (e.clientX < 275) {
                    brush_num = 6;
                    c.fillStyle = current_pallet[5]
                }
                else if (e.clientX < 307) {
                    brush_num = 7;
                    c.fillStyle = current_pallet[6]
                }
            }
        }
    }
    else if (e.clientY > 134) {
        if (e.clientY < 164) {
            if (e.clientX > 187) {
                if (e.clientX < 217) {
                    brush_num = 1;
                    c.fillStyle = current_pallet[0]
                }
                else if (e.clientX < 246) {
                    brush_num = 2;
                    c.fillStyle = current_pallet[1]

                }
                else if (e.clientX < 275) {
                    brush_num = 3;
                    c.fillStyle = current_pallet[2]
                }
                else if (e.clientX < 307) {
                    brush_num = 4;
                    c.fillStyle = current_pallet[3]
                }
            }
        }
    }
    if (e.clientY < 263) {
        if (e.clientY > 239) {
            if (e.clientX > 187) {
                if (e.clientX < 216) {
                    bg_color = current_pallet[0]
                    change_bg()
                }
                else if (e.clientX < 246) {
                    bg_color = 5;
                    bg_color = current_pallet[1]
                    change_bg()
                }
                else if (e.clientX < 275) {
                    bg_color = 6;
                    bg_color = current_pallet[2]
                    change_bg()
                }
                else if (e.clientX < 307) {
                    bg_color = 7;
                    bg_color = current_pallet[3]
                    change_bg()
                }
            }
        }
    }

    else if (e.clientY > 263) {
        if (e.clientY < 292) {
            if (e.clientX > 187) {
                if (e.clientX < 216) {
                    bg_color = 1;
                    bg_color = current_pallet[7]
                    change_bg()
                }
                else if (e.clientX < 246) {
                    bg_color = 2;
                    bg_color = current_pallet[4]
                    change_bg()
                }
                else if (e.clientX < 277) {
                    bg_color = 3;
                    bg_color = current_pallet[5]
                    change_bg()
                }
                else if (e.clientX < 307) {
                    bg_color = 4;
                    bg_color = current_pallet[6]
                    change_bg()
                }
            }
        }
    }
    if (e.clientY > 321) {       
        if (e.clientY < 397) {
            if (e.clientX > 187) {
                if (e.clientX < 320) {
                    current_pallet = pallet0;
                    dribble_COLORS = pallet0;
                    change_pallet1()

                }
            }
        }
    }
    if (e.clientY > 420) {            
        if (e.clientY < 499) {     
            if (e.clientX > 188) {
                if (e.clientX < 308) {
                    current_pallet = pallet1;
                    dribble_COLORS = pallet1;
                    change_pallet2()
                }
            }
        }
    }
    if (e.clientY > 520) {         
        if (e.clientY < 599) {            
            if (e.clientX > 188) {
                if (e.clientX < 308) {
                    current_pallet = pallet2;
                    dribble_COLORS = pallet2;
                    change_pallet3()
                }
            }
        }
    }
/*    if (e.clientY > 613) {            
        if (e.clientY < 636) {
            if (e.clientX > 212) {
                if (e.clientX < 291) {
                    
                }
            }
        }
    }*/
    if (e.clientY > 620) {
        if (e.clientY < 650) {
            if (e.clientX > 190) {
                if (e.clientX < 284) {
                    disengage();
                    c.clearRect(400, 0, 1000, 600);
                    change_bg();
                    //c.fillStyle = 'White';
                    //c.fillRect(400, 0, 1000, 600);
                    c.strokeStyle = 'Black';
                    c.strokeRect(400, 0, 1000, 600);
                    c.fillStyle = current_pallet[brush_num - 1];
                }
            }
        }
    }
}

var change_pallet1 = function () {
    c.fillStyle = 'White';
    c.fillRect(100, 0, 280, 600);
    c.strokeStyle = 'Black';
    c.strokeRect(100, 0, 280, 600);
    c.fillStyle='White';
    c.fillRect(400, 0, 1000, 600);
    c.strokeStyle = 'Black';
    c.strokeRect(400, 0, 1000, 600);

    c.fillStyle = 'Black';
    c.font = "16px Georgia";
    c.fillText("Paint Brush", 200, 46);
    c.fillStyle = 'Black';
    c.strokeRect(181, 56, 28, 28);
    c.fillStyle = 'DarkOliveGreen';
    c.fillRect(210, 55, 30, 30);
    c.fillStyle = 'SandyBrown';
    c.fillRect(240, 55, 30, 30)
    c.fillStyle = 'PapayaWhip';
    c.fillRect(270, 55, 30, 30)
    c.fillStyle = 'Black';
    c.fillRect(180, 85, 30, 30)
    c.fillStyle = 'FireBrick';
    c.fillRect(210, 85, 30, 30)
    c.fillStyle = 'SlateGrey';
    c.fillRect(240, 85, 30, 30)
    c.fillStyle = 'DarkCyan';
    c.fillRect(270, 85, 30, 30)

    c.fillStyle = 'Black';
    c.fillText("Background", 200, 146);
    c.strokeRect(181, 156, 28, 28)
    c.fillStyle = 'DarkOliveGreen';
    c.fillRect(210, 155, 30, 30)
    c.fillStyle = 'SandyBrown';
    c.fillRect(240, 155, 30, 30)
    c.fillStyle = 'PapayaWhip';
    c.fillRect(270, 155, 30, 30)
    c.fillStyle = 'Black';
    c.fillRect(180, 185, 30, 30)
    c.fillStyle = 'FireBrick';
    c.fillRect(210, 185, 30, 30)
    c.fillStyle = 'SlateGrey';
    c.fillRect(240, 185, 30, 30)
    c.fillStyle = 'DarkCyan';
    c.fillRect(270, 185, 30, 30)

    c.strokeStyle = 'White';
    c.strokeRect(179, 239, 121, 81)
    c.strokeStyle = 'Black';
    c.drawImage(img_pollock, 180, 240, 120, 80)
    c.drawImage(img_pollock2, 180, 340, 120, 80)
    c.drawImage(img_pollock3, 180, 440, 120, 80)

    c.drawImage(document.getElementById('undo'), 190, 540, 90, 30)
    //c.drawImage(document.getElementById('clear'), 240, 540, 90, 30)
}

var change_pallet2 = function () {
    c.strokeRect(100, 0, 280, 600);
    c.strokeRect(400, 0, 1000, 600);

    c.fillStyle = 'Black'
    c.font = "16px Georgia";
    c.fillText("Paint Brush", 200, 46);
    c.fillStyle = 'Black';
    c.strokeRect(181, 56, 28, 28);
    c.fillStyle = 'Grey'
    c.fillRect(210, 55, 30, 30);
    c.fillStyle = 'Brown'
    c.fillRect(240, 55, 30, 30)
    c.fillStyle = 'GoldenRod'
    c.fillRect(270, 55, 30, 30)
    c.fillStyle = 'Black'
    c.fillRect(180, 85, 30, 30)
    c.fillStyle = 'Thistle'
    c.fillRect(210, 85, 30, 30)
    c.fillStyle = 'DimGrey'
    c.fillRect(240, 85, 30, 30)
    c.fillStyle = 'MediumBlue'
    c.fillRect(270, 85, 30, 30)

    c.fillStyle = 'Black'
    c.fillText("Background", 200, 146);
    c.strokeRect(181, 156, 28, 28)
    c.fillStyle = 'Grey'
    c.fillRect(210, 155, 30, 30)
    c.fillStyle = 'Brown'
    c.fillRect(240, 155, 30, 30)
    c.fillStyle = 'GoldenRod'
    c.fillRect(270, 155, 30, 30)
    c.fillStyle = 'Black' 
    c.fillRect(180, 185, 30, 30)
    c.fillStyle = 'Thistle'
    c.fillRect(210, 185, 30, 30)
    c.fillStyle = 'DimGrey'
    c.fillRect(240, 185, 30, 30)
    c.fillStyle = 'MediumBlue'
    c.fillRect(270, 185, 30, 30)

    c.strokeStyle = 'White'
    c.strokeRect(179, 239, 121, 81)
    c.strokeStyle = 'Black'
    c.drawImage(img_pollock, 180, 240, 120, 80)
    c.drawImage(img_pollock2, 180, 340, 120, 80)
    c.drawImage(img_pollock3, 180, 440, 120, 80)

    c.drawImage(document.getElementById('clear'), 190, 540, 90, 30)
    //c.drawImage(document.getElementById('clear'), 240, 540, 90, 30)
}

var change_pallet3 = function () {
    c.strokeRect(100, 0, 280, 600);
    c.strokeRect(400, 0, 1000, 600);

    c.fillStyle = 'Black'
    c.font = "16px Georgia";
    c.fillText("Paint Brush", 200, 46);
    c.fillStyle = 'Black' 
    c.strokeRect(181, 56, 28, 28);
    c.fillStyle = 'Maroon'
    c.fillRect(210, 55, 30, 30);
    c.fillStyle = 'OrangeRed'
    c.fillRect(240, 55, 30, 30)
    c.fillStyle = 'Peru'
    c.fillRect(270, 55, 30, 30)
    c.fillStyle = 'Black'
    c.fillRect(180, 85, 30, 30)
    c.fillStyle = 'DarkGoldenRod'
    c.fillRect(210, 85, 30, 30)
    c.fillStyle = 'DarkSlateGray'
    c.fillRect(240, 85, 30, 30)
    c.fillStyle = 'Cyan'
    c.fillRect(270, 85, 30, 30)

    c.fillStyle = 'Black'
    c.fillText("Background", 200, 146);
    c.strokeRect(181, 156, 28, 28)
    c.fillStyle = 'Maroon'
    c.fillRect(210, 155, 30, 30)
    c.fillStyle = 'OrangeRed'
    c.fillRect(240, 155, 30, 30)
    c.fillStyle = 'Peru'
    c.fillRect(270, 155, 30, 30)
    c.fillStyle = 'Black'
    c.fillRect(180, 185, 30, 30)
    c.fillStyle = 'DarkGoldenRod'
    c.fillRect(210, 185, 30, 30)
    c.fillStyle = 'DarkSlateGray'
    c.fillRect(240, 185, 30, 30)
    c.fillStyle = 'Cyan'
    c.fillRect(270, 185, 30, 30)

    c.strokeStyle = 'White'
    c.strokeRect(179, 239, 121, 81)
    c.strokeStyle = 'Black'
    c.drawImage(img_pollock, 180, 240, 120, 80)
    c.drawImage(img_pollock2, 180, 340, 120, 80)
    c.drawImage(img_pollock3, 180, 440, 120, 80)

    c.drawImage(document.getElementById('clear'), 190, 540, 90, 30);
    //c.drawImage(document.getElementById('clear'), 240, 540, 90, 30)
}

var change_bg = function () {
    c.fillStyle = bg_color;
    c.fillRect(400, 1, 1000, 599);
    c.fill();
}

var engage = function (e) {
    color_check(e);
    dragging = true;
    radius = 14;
    putPoint(e);    
}

var moving_clicked = function (e) {
    if (dragging) {
        if (radius > 0) {
            putPoint(e);
        }
    }
}

var disengage = function (e) {
    dragging = false;  

    function convertCanvasToImage() {
        let canvasTemp = document.getElementById("canvas1");
        img.src = canvasTemp.toDataURL("image/jpeg");
        return img;
    }

    let pnGImage = convertCanvasToImage();
    document.appendChild(pnGImage);

    window.sessionStorage;
    localStorage.setItem('imgData', img);  
}    

function assignColors(COLORS) {    
    if (color_choice = 0) {
        current_pallet = pallet0;
    }
    else if (color_choice = 1) {
        current_pallet = pallet1;
    }
    else if (color_choice = 2) {
        current_pallet = pallet2;
    }
    let i = 0
    for (i = 0; i < 7; i++) {
        COLORS[i] = current_pallet[i];
    }
    change_pallet1(COLORS)
}

change_pallet1()
canvas.addEventListener('resize', function () {
    canvas.width = innerWidth;
    canvas.height = innerHeight;
});
canvas.addEventListener('mousedown', engage)
canvas.addEventListener('mousemove', moving_clicked)
canvas.addEventListener('mouseup', disengage)

// Team RUFF :: Ivan Yeung, Andrew Piatetsky
// SoftDev pd8
// K30 -- JS Paint
// 2023-04-24w
// --------------------------------------------------

//retrieve node in DOM via ID
var c = document.getElementById("slate");

//instantiate a CanvasRenderingContext2D object
var ctx = c.getContext("2d");

//init global state var
var mode = "rect";

//var toggleMode = function(e){
var toggleMode = (e) => {
    console.log("toggling...");
    var text = document.getElementById("buttonToggle");
    if (mode === "rect") {
        mode = "circ";
        text.innerHTML = "circle";
    }
    else {
        mode = "rect";
        text.innerHTML = "rectangle"
    }
}

var drawRect = function(e) {
    var mouseX = e.offsetX; //gets X-coor of mouse when event is fired
    var mouseY = e.offsetY; //gets Y-coor of mouse when event is fired
    console.log("mouseclick registered at ", mouseX, mouseY);
    ctx.fillStyle = "red";
    //ctx.fillRect(mouseX, mouseY, 100, 150); //combines rect() and fill() and beginPath()
    ctx.beginPath(); //VERY IMPORTANT WHEN YOU WANT TO CLEAR IF NOT USING A "everything-in-one" function (e.g. fillRect())
    ctx.rect(mouseX, mouseY, 100, 150);
    ctx.fill();
}

var drawCircle = function(e) {
    var mouseX = e.offsetX; //gets X-coor of mouse when event is fired
    var mouseY = e.offsetY; //gets Y-coor of mouse when event is fired
    console.log("cirlce: mouseclick registered at ", mouseX, mouseY);
    ctx.fillStyle = "red";
    ctx.arc(mouseX,mouseY,75,0,Math.PI*2);
    ctx.stroke(); //creates a black outline by default
    ctx.fill();
}

var draw = function(e) {
    if (mode == "rect") {
        drawRect(e);
    }
    else {
        ctx.beginPath() //without this, circles become meshed with each other and don't wipe correctly
        drawCircle(e);
    }
}

var clear = function(e) {
    ctx.clearRect(0, 0, c.width, c.height); //just wipes everything inside the slate
}

c.addEventListener("click", draw); //passes the mouse event as parameter for the function

var toggle = document.getElementById("buttonToggle");
toggle.addEventListener("click",toggleMode);

var wipe = document.getElementById("buttonClear");
wipe.addEventListener("click",clear);
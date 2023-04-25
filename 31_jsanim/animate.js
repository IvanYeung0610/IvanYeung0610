//  Ivan Yeung, Andrew Gabriel Thompson
// SoftDev pd8
//  K31 -- canvas based JS animation
//  2023-04-25t
// --------------------------------------------------

//retrieve node in DOM via ID
var c = document.getElementById("playground");
var dotButton = document.getElementById("buttonCircle");
var stopButton = document.getElementById("buttonStop");

//instantiate a CanvasRenderingContext2D object
var ctx = c.getContext("2d");
ctx.fillStyle = "rgb(0, 255, 255)";
var requestID;

var clear = function(e) {
    ctx.clearRect(0, 0, c.width, c.height); //just wipes everything inside the slate
}

var radius = 0;
var growing = true;

var drawDot = () => {
    /*
        Wipe the canvas,
        Repaint the circle,

        ...and somewhere (where/when is the right time?)
        Update request ID to propagate the animation.
        You wil need
        window.cancelAnimationFrame()
        window.requestAnimationFrame()
    */
    clear(e);

    if (radius == 250) {
        growing = false;
    }

    if (radius == 0) {
        growing = true;
    }

    if (growing) {
        radius++;
    } else {
        radius--;
    }
};

//var stopIt = function() {
var stopIt = ()=> {
    console.log("stopIt invoked...");
    console.log( requestID );

    /* YOUR CODE HERE
        ... to stop the animation
        You will need window.cancelAnimationFrame()
    */
};

dotButton.addEventListener("click", drawDot);
stopButton.addEventListener("click", stopIt);
/*
   your PPTASK:
   
   Test drive each bit of code in this file,
    and insert comments galore, indicating anything
     you discover,
    	have questions about,
    		or otherwise deem notable.
    		
    		Write with your future self or teammates in mind.
    		
    		If you find yourself falling out of flow mode, consult 
    		other teams
    		MDN

   A few comments have been pre-filled for you...
   
   (delete this block comment once you are done)
*/

// Team RUFF :: Ivan Yeung, Andrew Piatetsky
// SoftDev pd8
// K28 -- Getting more comfortable with the dev console and the DOM
// 2023-04-05w
// --------------------------------------------------


//send diagnostic output to console
//(Ctrl-Shift-K in Firefox to reveal console)
console.log("AYO"); //equivilant to print statement?

//var's can be called in the console 
//able to use operators(including comparisions) with console
var i = "hello";
var j = 20;


//assign an anonymous fxn to a var
//function can be called and used with the the var name with the parameter: f(x)
//calling f in console returns the code of the function
//this way of creating functions is a lot like the scheme syntax
var f = function(x) { 
  var j=30;
  return j+x;
};


//instantiate an object
//calling o returns a mongodb type document: 
//  {name: 'Thluffy', age: 1024, items: Array(4), morestuff: {…}, func: ƒ}
//can't call individual items without referencing o (ex: o.items -> [10, 20, 30, 40])
//can call functions like normal with reference to o
//can call object inside object like a nested reference (ex: o.morestuff.a -> 1)
var o = { 'name' : 'Thluffy',
          age : 1024,
          items : [10, 20, 30, 40],
          morestuff : {a : 1, b : 'ayo'},
          func : function(x) {
            return x+30;
          }
        };

//this function references items on the html portion of the assignment
//html file is not actually changed when function in run in console
//reverts back to origianl state if the page is reloaded
//console seems to return undefined for some reason but changes do appear after function is ran
//this function adds to the ordered list with the class tag "thelist"
//always adds to the bottom (is there a way to add to anywhere on the list?)
var addItem = function(text) {
  var list = document.getElementById("thelist"); //seems to get the list of items already in html
  var newitem = document.createElement("li"); //creates another list item marker for the new item being inserted
  newitem.innerHTML = text; //inserts the text from the function parameter inside the new marker
  list.appendChild(newitem); //adds the new item to the pre-existing list
};

//this function removes from the ordered list with the class tag "thelist"
//the list item you are trying to remove is actually 1 less than what is shown on the page in html
//if you remove item from the middle of the list, everything is shifted up
var removeItem = function(n) {
  var listitems = document.getElementsByTagName('li');
  listitems[n].remove();
};

//only turn items without a color in their class identification red
var red = function() {
  var items = document.getElementsByTagName("li");
  for(var i = 0; i < items.length; i++) {
    items[i].classList.add('red'); //this function doesn't seem to work for items that are already styled with a color
  }
};

//this function causes non-styled items to having alternating red and blue color
var stripe = function() {
  var items = document.getElementsByTagName("li");
  for(var i = 0; i < items.length; i++) {
    if (i%2==0){
      items[i].classList.add('red');
    } else {
      items[i].classList.add('blue');
    }
  }
};

//insert your implementations here for...
// FIB
var FIB = function(n) {
  if (n < 2) {
      return n;
  } else {
      return FIB(n - 1) + FIB(n - 2);
  }
}
// FAC
const FAC = (input) => { //seems to be called in the same fashion as other styles for writing functions
  if (input < 2) {
    return 1;
  } else {
      return input * FAC(input - 1);
  }
}
// GCD
const GCD = (num1, num2) => {
  var product = num1 * num2;
  return product / LCM(num1, num2);
}

var LCM = function(num1, num2) {
  var mult = num1;
  while (mult % num2 != 0) {
    mult = mult + num1;
  }
  return mult;
}
// In addition to the style shown above,
//  you are encouraged to test drive the "arrow function syntax" as shown below.
//  Note anything notable.
const myFxn = (param1, param2) => {
  // body
  return retVal;
};



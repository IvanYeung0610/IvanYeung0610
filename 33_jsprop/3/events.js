// demo 3
// JS event propagation

var tds = document.getElementsByTagName('td');
var trs = document.getElementsByTagName('tr');
var table = document.getElementsByTagName('table')[0];

var clicky = function(e) {
  alert( this.innerHTML );
  //Q: What will happen when next line is uncommented?
  // We think the cell event would be trigger while the subsequent row and table event won't pop-up
  //e.stopPropagation();
};

var clicky1 = function(e) {
  alert( this.innerHTML );
  //Q: What will happen when next line is uncommented?
  // We think the cell event would be trigger while the subsequent row and table event won't pop-up
  e.stopPropagation(); //stops pop-ups from appearing after showing the alert by the initial call
};


for (var x=0; x < tds.length; x++) {
  tds[x].addEventListener('click', clicky);
}

for (x=0; x < trs.length; x++) {
  trs[x].addEventListener('click', clicky);
  //trs[x].addEventListener('click', clicky, true); //Result: row -> cell -> table
}

//Predict, then test...
//Q: What effect does the boolean arg have?
// Reverses the order in which the pop-ups appear by default
// Result: table -> cell -> row
//   (Leave exactly 1 version uncommented to test...)

//table.addEventListener('click', clicky, true);
table.addEventListener('click', clicky, false); // results in order that we saw in 2

// Q: When user clicks on a cell, in what order will the pop-ups appear?
//Inner-most to outer-most unless the EventListeners have the added boolean arguement

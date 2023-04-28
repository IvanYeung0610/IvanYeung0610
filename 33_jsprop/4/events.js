// demo 4
// JS event propagation

// Name the collections of TDs, TRs, and overall table
var tds = document.getElementsByTagName('td');
var trs = document.getElementsByTagName('tr');
var table = document.getElementsByTagName('table')[0];


var clicky = function(e) {
  alert( this.innerHTML );
  //Q: What will happen when next line is uncommented?
  // The first pop-up that appears is the only pop-up that will appear when clicked.
  // e.stopPropagation();
};


//Q: Does the order in which the event listeners are attached matter?
// Yes, we think so when all the Event Listeners are set to true. Whichever one that is attached last will be on top of the "stack".

//Predict, then test...
//Q: What effect does the boolean arg have in each?
// It decides whether to put the event at the top of the "stack" (display order). <- seems CORRECT
//   (Leave exactly 1 version uncommented to test...)

// for (var x=0; x < tds.length; x++) {
//   tds[x].addEventListener('click', clicky, true);
//   //tds[x].addEventListener('click', clicky, false);
// }

// for (x=0; x < trs.length; x++) {
//   trs[x].addEventListener('click', clicky, true);
//   //trs[x].addEventListener('click', clicky, false);
// }

// table.addEventListener('click', clicky, true);
table.addEventListener('click', clicky, false);

for (var x=0; x < tds.length; x++) {
    // tds[x].addEventListener('click', clicky, true);
    tds[x].addEventListener('click', clicky, false);
}

for (x=0; x < trs.length; x++) {
  trs[x].addEventListener('click', clicky, true);
  //trs[x].addEventListener('click', clicky, false);
}

//Order doesn't seem to matter. If all are true order is table -> row -> cell
//We think that the events will appear with the true ones first from outermost to innermost and then the false ones from innermost to outermost.
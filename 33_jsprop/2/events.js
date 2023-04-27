// demo 2
// JS event propagation

var tds = document.getElementsByTagName('td');
var trs = document.getElementsByTagName('tr');
var table = document.getElementsByTagName('table')[0];

var clicky = function(e) {
  alert( this.innerHTML );
};

table.addEventListener('click', clicky);

for (x=0; x < trs.length; x++) {
  trs[x].addEventListener('click', clicky);
}

for (var x=0; x < tds.length; x++) {
  tds[x].addEventListener('click', clicky);
}

// for (x=0; x < trs.length; x++) {
//   trs[x].addEventListener('click', clicky);
// }

// table.addEventListener('click', clicky);

//Predicition: clicking on cell will trigger events for both the cell and the row that it belongs to.

// Q: When user clicks on a cell, in what order will the pop-ups appear?
// We think the cell event will appear first since it is listed first in the code.
//Result: cell -> row -> table
// When the order of the for loops are changed, the pop-ups still appear in the same order

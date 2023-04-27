// demo 1
// JS event propagation

var tds = document.getElementsByTagName('td');

var clicky = function(e) {
  alert( this.innerHTML ); //pulls up box with text of the cell we clicked on
};

for (var x=0; x < tds.length; x++) {
  tds[x].addEventListener('click', clicky);
}

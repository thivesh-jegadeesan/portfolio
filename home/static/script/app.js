const sidenava = document.getElementsByClassName("sidenava");
var urlval = window.location.href.split('/')[4];

for(let i=0; i<(document.getElementsByClassName('sidenava')).length; i++){
  if(document.getElementsByClassName('sidenava')[i].id == urlval)
  {
    document.getElementById(document.getElementsByClassName('sidenava')[i].id).classList.add("mystyle");
  }
}
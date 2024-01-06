var mydiv =document.getElementById("fst");
mydiv.style.backgroundColor='gray';
mydiv.innerHTML='new content>old';
var div=document.createElement('div');
div.classList.add('my-new-div');
div.innerHTML="1st new";
mydiv.appendChild(div);

var div2=document.createElement('div');
div2.innerHTML='2st new';

div.remove();

var op;

var n1=1000;var n2=1500;var n3=2000;
var m1=500; var m2=1000;var m3=5000;
var ccc=0; var cc=111;
var a=0;   var result=0; 
var l=0;
 

      window.addEventListener('DOMContentLoaded', function (event) {
  let s = document.getElementsByName("myselect");
  s[0].addEventListener("change", function(event) {
    let select = event.target;
    let radios = document.getElementById("myradios");
    console.log(select.value);
    let radio=event.target;

    if(select.value=="1")
   {
    a=n1;
    radios.style.display="none";
    
   }
   
   if(select.value=="2")
   {
    a=n2;
    radios.style.display="block";
    let r = document.querySelectorAll(".myradios input[type=radio]");
  r.forEach(function(radio) {
    radio.addEventListener("change", function(event) {
      let r = event.target;
      console.log(r.value);
    
      if(r.value=="r1")
    {
      l=m1;
    }
    if(r.value=="r2")
    {
      l=m2;
    }
    if(r.value=="r3")
    {
      l=m3;
    }
    });    
  });
   }
   else
   {
    l=0;
   }

   if(select.value=="3")
  { 
      a=n3;
     radios.style.display="none";
  }
  });
 

 /* let c = document.querySelectorAll(".cbox input[type=checkbox]");
  c.forEach(function(checkbox) {
    checkbox.addEventListener("change", function(event) {
      let c = event.target;
     if(c.checked)
     {
      ccc=cc;
     }

    })});
  */
  });

  


  function f1()
  {
    var chbox;
chbox=document.getElementById("one");
if (chbox.checked) {
		alert('Выбран');
	}
	else {
		alert ('Не выбран');
	}
  }
 


 
function click1(){
      let f2 = document.getElementsByName("field2");
         
result= l+f2[0].value*a+ccc;
document.getElementById("input2").value=result;
}

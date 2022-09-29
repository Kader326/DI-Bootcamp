         Entrez un nombre : <input id="myInput">
         function check(){
              var nbr;
              nbr = Number(document.getElementById("myInput").value);
              if(nbr%2 == 0)
              {
                     alert(+nbr"est un nombre pair");
              }
              else
              {
                     alert(+nbr" est un nombre impair");
              }
         }
      <button onclick="check()">Vérifier</button>
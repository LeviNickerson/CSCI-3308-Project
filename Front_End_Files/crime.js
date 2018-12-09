var state = 1;
var n_button_bool = false;
var c_button_bool = false;

var n_button_selected = "";
var c_button_selected = "";


function change_n_Selection(btn) {
    var n_button = document.getElementById(btn);
      if (n_button_bool == false) {
          n_button.style.backgroundColor = "#0066ff"
          n_button_bool = true;
          n_button_selected = n_button
      }
      else {

          n_button_selected.style.backgroundColor = "#eee"
          n_button.style.backgroundColor = "#0066ff"
          n_button_selected = n_button

        }
   }

function change_c_Selection(btn) {

    var c_button = document.getElementById(btn);
        if (c_button_bool == false) {
            c_button.style.backgroundColor = "#0066ff"
            c_button_bool = true;
            c_button_selected = c_button
         }
        else {

            c_button_selected.style.backgroundColor = "#eee"
            c_button.style.backgroundColor = "#0066ff"
            c_button_selected = c_button

           }
      }

function return_data() {

    if (n_button_bool == true && c_button_bool == true){

      document.getElementById('display_text').innerHTML = "SUCCESS"

    }else{

      document.getElementById('display_text').innerHTML = "SELECT BOTH A NEIGHBOORHOOD AND CRIME"

    }

    }


function print_results() {

  document.getElementById('display_text').innerHTML = "SUCCESS"

                        }

var state = 1;
var n_button_bool = false;
var c_button_bool = false;

var n_button_selected = "";
var c_button_selected = "";

var n_input= "";
var c_input= "";

var data = {
"nieghboorhood_one":{
  "Crime_One":"This is the data on crime one in neighboorhood one",
  "Crime_Two":"This is the data on crime two in neighboorhood one",
  "Crime_Three":"This is the data on crime one in neighboorhood one"
},
"nieghboorhood_two":{
  "Crime_One":"This is the data on crime one in neighboorhood two",
  "Crime_Two":"This is the data on crime two in neighboorhood two",
  "Crime_Three":"This is the data on crime one in neighboorhood two"
},
"nieghboorhood_three":{
  "Crime_One":"This is the data on crime one in neighboorhood three",
  "Crime_Two":"This is the data on crime two in neighboorhood three",
  "Crime_Three":"This is the data on crime one in neighboorhood three"
},
"nieghboorhood_four":{
  "Crime_One":"This is the data on crime one in neighboorhood four",
  "Crime_Two":"This is the data on crime two in neighboorhood four",
  "Crime_Three":"This is the data on crime one in neighboorhood four"
},
"nieghboorhood_five":{
  "Crime_One":"This is the data on crime one in neighboorhood five",
  "Crime_Two":"This is the data on crime two in neighboorhood five",
  "Crime_Three":"This is the data on crime one in neighboorhood five"
}

};



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

      var neighboorhood_input = ""
      var crime_input = ""

      var neighboorhood_data = data[n_input]
      var crime_data = neighboorhood_data["Crime_One"]

      document.getElementById('display_text').innerHTML = crime_data

    }else{

      document.getElementById('display_text').innerHTML = "SELECT BOTH A NEIGHBOORHOOD AND CRIME"

    }

    }

function set_n_input(input_string) {

  n_input= input_string;

}

function set_c_input(input_string) {

  c_input= input_string;

}

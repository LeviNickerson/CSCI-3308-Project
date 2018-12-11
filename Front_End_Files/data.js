
var data_topass = {"auraria":{
  "aggravated-assault":[],
  "drug-alcohol":["crime one","crime two","crime three","crime four","crime four"],
  "robbery":["crime one","crime two","crime three","crime four","crime four"]
},
"capitol_hill":{
  "aggravated-assault":["crime one","crime two","crime three","crime four","crime four"],
  "drug-alcohol":["crime one","crime two","crime three"],
  "robbery":["crime one","crime two","crime three","crime four","crime four"]
},
"cbd":{
  "aggravated-assault":["crime one","crime two","crime three"],
  "drug-alcohol":[],
  "robbery":["crime one","crime two"]
},
"civic_center":{
  "aggravated-assault":["crime one","crime two","crime three","crime four","crime four"],
  "drug-alcohol":["crime one","crime two","crime three","crime four","crime four"],
  "robbery":[]
},
"lincoln_park":{
  "aggravated-assault":[],
  "drug-alcohol":["crime one","crime two","crime three","crime four","crime four"],
  "robbery":["crime one","crime two","crime four"]
}

};


function load() {
    //var someData_notJSON = JSON.parse(data)
    ret = JSON.stringify(data_topass)
    //console.log(data_topass);
    //console.log(ret);
    return ret;
    }


var uik_month  = ["Jan","Feb","Mar","Apr","	May","Aug","Sep","Oct","Nov","Dec"]; 

function ConvDate(dateStr){
 dateStr = myFunction_dt(dateStr);
  var a=dateStr.split(" ");
var d=a[0].split("/");
var t=a[1].split(":");

var date = new Date(d[0],(d[1]-1),d[2],t[0],t[1],0);
var s = date.getDate()+"th "+uik_month[date.getMonth()]+" "+" "+date.getYear()+" "+formatAMPM(date);

return s;

}


function myFunction_dt(timestamp) {

var date = new Date(timestamp * 1000);
var formattedDate =  date.getFullYear()+ '/' + ('0' + (date.getMonth() + 1)).slice(-2) + '/' + ('0' + date.getDate()).slice(-2) +  ' ' + ('0' + date.getHours()).slice(-2) + ':' + ('0' + date.getMinutes()).slice(-2);

return formattedDate;

}

 function formatAMPM(date) {  
  var hours = date.getHours();
  var minutes = date.getMinutes();
  var ampm = hours >= 12 ? 'PM' : 'AM';
  hours = hours % 12;
  hours = hours ? hours : 12; // the hour '0' should be '12'
  minutes = minutes < 10 ? '0'+minutes : minutes;
  var strTime = hours + ':' + minutes + ' ' + ampm;
  return strTime;
} 
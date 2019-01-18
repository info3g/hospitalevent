function loadf(id,file){
 if($('#'+id).attr('data-fi') === file){
  $('#'+id).load(file); 
 }
}


  function getInsertDiv(em_Name, fil_Name,sho_ld ){                     
          
          if(sho_ld == 'yes'){
              $('#ajaxloader').show(); 
          }
                     
           $('#'+em_Name).load( fil_Name, function() {
                                  
                 if(sho_ld == 'yes'){
                    $('#ajaxloader').hide(); 
                  }
                        
             });                    
}

function insert(url,id,message){
               var fn = window[id.getAttribute('data-error')];
               if(!fn(id)){  return false; }
               $.post(url,$(id).serialize()).done(function( data ){
                  alert(message);
               })
return false; 
}

function toggle_clp(selector) {
  document.querySelector(selector).toggle();
}

function insert_upload(url,id,message){	
       var fn = window[id.getAttribute('data-error')];
       if(!fn(id)){  return false; }
       var formData = new FormData($(id)[0]);
 		$.ajax({
		url: url,
		type: 'POST',
		data: formData,
		async: false,
		cache: false,
		contentType: false,
		processData: false,
		success: function (returndata){
		 alert(message);
		} 
		});
 	return false;
}
	   
   

$(function(){

try{
  $("input.datepicker").Zebra_DatePicker({
	  format: 'd/M/Y'
  });
  
  $("#calendar").Zebra_DatePicker({
	  always_visible:$("#container")
  });
}catch(error) {

}  
  $(".loaddiv").each(function(){
	if(typeof $(this).attr("data-load") == 'undefined'){  
		$(this).attr("data-load","yes");  
		$(this).load($(this).attr("data-fi"));
	}
  });

});
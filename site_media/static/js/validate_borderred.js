function validateEmail(email) {
    var re = /^([\w-]+(?:\.[\w-]+)*)@((?:[\w-]+\.)*\w[\w-]{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?)$/i;
    return re.test(email);
}
var valid = true;

function border_run_for(form){

$(form).find(".checkbox, .radio").each(function() {


     if($(this).attr("data-validate") === 'true'){
       var attr = $(this).attr('data-min');
       if(typeof attr !== typeof undefined && attr !== false){

       }else if($(this).hasClass('radio')){
         attr = 1;
       }
       else{
         attr = 1;
       }
         if($(this).find('input:checked').length < parseInt(attr)){
            $(this).find('input').css('outline','1px solid red');
            valid = false;
         }
      }



});

}



function border(form){
valid= true;
$(form).find("input,textarea,select,.draggable").removeClass('error_inp');
$(form).find("input[type=checkbox],input[type=radio]").css("outline","");
border_run_for(form);
$( form).find("input,textarea,select").each(function( index ) {

var fom = $(this).attr("data-validate");

if(typeof fom == typeof undefined){
  return true;
}

    if(fom == 'true' || fom == 'false'){
		if($(this).attr("type") === 'file'){
    if(fom == 'true' && $(this).val() === ''){
			 $(this).addClass("error_inp");
			 valid= false;
       return ;
			}

		}

		if($(this).prop('tagName') === 'SELECT'){

			if(fom === 'true' && $(this).val() == '0'){
			$(this).addClass("error_inp");

			 valid= false;
             return ;
			}

		}
		 return;

	}


    if(fom[0] === 'Y'){
        if($(this).val() === "" || $(this).val() === null){
          $(this).addClass("error_inp");

		  valid= false;
        return;
        }
    }
    if(fom[1] === 'Y'){
        if(!validateEmail($(this).val())){
         $(this).addClass("error_inp");

		 valid= false;
          return;
        }
    }
    if(fom[2] === 'Y'){
        if($(this).val().indexOf(' ')> -1){
        $(this).addClass("error_inp");

		valid= false;
        return;
        }
    }
    if(fom[3] === 'Y')
    { var range = fom.substring(fom.indexOf('[')+1,fom.indexOf(']'));
      var attr = range.split('-');
     if(!($(this).val()>=parseInt(attr[0]) && $(this).val() <= parseInt(attr[1]))){
          $(this).addClass("error_inp");

		  valid= false;
         return;
      }

    }
    if(fom.substring(fom.indexOf(']')+1,fom.lastIndexOf('[')) === 'Y'){
      var range = fom.substring(fom.lastIndexOf('[')+1,fom.lastIndexOf(']'));

       console.log($(this).val().length+range);
       if(!eval($(this).val().length+range)){
          $(this).addClass("error_inp");

		  valid= false;
         return;
      }


    }
    if(fom.charAt(fom.length - 3) === 'Y' ){
        if(!(/\d/.test($(this).val()))){
            $(this).addClass("error_inp");

			valid= false;
         return;
        }

    }

    if(fom.charAt(fom.length - 2) === 'Y' ){
        if(!(/[A-Z]/.test($(this).val()))){
           $(this).addClass("error_inp");

		   valid= false;
         return;
        }
    }
    if(fom.charAt(fom.length - 1) === 'Y' ){
        if(!(/[^a-zA-Z\d]/.test($(this).val()))){
           $(this).addClass("error_inp");

		   valid= false;
         return;
        }
    }
	 if($(this).attr("data-regex") !== undefined){
         var patt = new RegExp($(this).attr("data-regex"));
        if(!patt.test($(this).val())){
         $(this).addClass("error_inp");

		 valid= false;
         return;
        }
    }

});

 return valid;
}

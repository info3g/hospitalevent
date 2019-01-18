/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */




var yes_child = 0;


function fg(fg){
   var space = ""; 
     yes_child = fg.parents().length -2;
    for(var i=0;i<=yes_child;i++ ){
       space = space +" &nbsp; ";
    }  
    
       if(fg.attr('id')!=undefined){
        $('#tree_st').append("<span>"+space+fg.attr('id')+" "+fg.prop("tagName")+"</span>");
        } 
        else if(fg.attr('class')!=undefined){
           $('#tree_st').append("<span>"+space+fg.attr('class')+" "+fg.prop("tagName")+"</span>");      
        }
        else{
          $('#tree_st').append("<span>"+space+fg.prop("tagName")+"</span>"); 
        } 
    
}



         

   
function run_tree(sel){


$('#tree_st').html('');

sel.find('*').each(function(){
    if($(this).children().length > 0 ){ 
        
        if(yes_child>0){
        
            fg($(this));
              
         yes_child = yes_child+1;    
          return;  
        }
         yes_child = yes_child+1;
        if($(this).attr('id')!=undefined){
        $('#tree_st').append("<span>+ "+$(this).attr('id')+" "+$(this).prop("tagName")+"</span>");
        }    
        else if($(this).attr('class') != undefined){
        $('#tree_st').append("<span>>+"+$(this).attr('class')+" "+$(this).prop("tagName")+"</span>");
        }   
       else{
             $('#tree_st').append("<span>"+$(this).prop("tagName")+"</span>"); 
       } 
    }
    else if(yes_child > 0){
        
         fg($(this));
    }
    
    else{
          yes_child = yes_child -1 ;        
        if($(this).attr('id')!=undefined){
        $('#tree_st').append("<span>"+$(this).attr('id')+" "+$(this).prop("tagName")+"</span>");
        } else if($(this).attr('class') != undefined){
        $('#tree_st').append("<span>+"+$(this).attr('class')+" "+$(this).prop("tagName")+"</span>");
        }   
       else{
             $('#tree_st').append("<span>"+$(this).prop("tagName")+"</span>"); 
       } 
    
    }    
     
  
});

}
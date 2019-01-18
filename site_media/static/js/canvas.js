function dragMoveListener (event) {

if((event.target.className).indexOf('webgcenter')> -1){
  parent.document.getElementById("toast1").text = "Element is centered";
  parent.document.getElementById("toast1").open();
  return false;

}

  var target = event.target,
      // keep the dragged position in the data-x/data-y attributes
      x = (parseFloat(target.style.left) || 0) + event.dx,
      y = (parseFloat(target.style.top) || 0) + event.dy;

  // translate the element
  target.style.webkitTransform =
  target.style.left = x + 'px';
  target.style.top =  y + 'px';


}

// this is used later in the resizing demo
window.dragMoveListener = dragMoveListener;


interact('#canvas').dropzone({
// only accept elements matching this CSS selector
accept: '.draggable',
// Require a 75% element overlap for a drop to be possible
overlap: 0.60,

// listen for drop related events:

ondropactivate: function (event) {
  // add active dropzone feedback
  //event.target.classList.add('drop-active');
},
ondragenter: function (event) {
  var draggableElement = event.relatedTarget,
      dropzoneElement = event.target;

  // feedback the possibility of a drop

},
ondragleave: function (event) {
  // remove the drop feedback style

},
ondrop: function (event) {

},
ondropdeactivate: function (event) {
  // remove active dropzone feedback

}
});



interact('.draggable').draggable({
inertia: true,
autoScroll: true,
  restrict: {
    restriction: "parent",
    endOnly: true

  },

  onmove: window.dragMoveListener
})
.resizable({
  edges: { left: true, right: true, bottom: true, top: true },
elementRect: { left: 1, right: 2, top: 1, bottom: 2 }
})
.on('resizemove', function (event) {
  var target = event.target;

  // update the element's style
target.style.height = event.rect.height + 'px';

  if(target.style.width === '100%'){

}else{
  target.style.width  = event.rect.width + 'px';
  }



});

String.prototype.replaceBetween = function(start, end, what) {
    return this.substring(0, start) + what + this.substring(end);
};

function addCSSToStyleTag(sel,prop,val){

    for(var i = 0;i<document.styleSheets.length;i++){
        if(document.styleSheets[i].title === 'webg'){

           for(var j=0;j<document.styleSheets[i].rules.length;j++){

              if(document.styleSheets[i].rules[j].selectorText === sel){

                if(sel.indexOf('hover')> -1){
                document.styleSheets[i].rules[j].style[prop]  = val;
                }else{
                document.styleSheets[i].rules[j].style[prop]  = val;
                }
                resetStyle(i); console.log('finsss');
                return false;
              }
           }


        }

    }

$('style[title="webg"]').append(sel+'  {   '+getCssName(prop)+' : '+val+ '   }');
};


function getCssName(p){

   if(p == 'backgroundColor'){
     return 'background-color';
   }
   if(p == 'margin' || p === 'display' || p === 'float'){
     return p;
   }

}

function resetStyle(i){

var st = '';
for(var j=0;j<document.styleSheets[i].rules.length;j++){

st  = st+' '+document.styleSheets[i].rules[j].cssText;

}

$('style[title="webg"]').text(st);


}


$(function(){


  $("#canvas").on('submit','form',function(e){
     e.preventDefault();
   });

 $('#canvas').on("click",".modal .close,.modal button[data-dismiss='modal']",function(){
   $(".modal").removeClass("in");
   $(".modal").css("display","none");
 });

  $("#canvas").on("click",".show_dailog",function(){

      $($(this).attr("data-target")).addClass('in');
      $($(this).attr("data-target")).css('display','block');
  });


$("#canvas").on("click",".nav a",function(e){
    e.stopPropagation();
     var hh = $(this).attr("href");
     $(hh).parent(".tab-content").find('>div').removeClass('in active');
     $(hh).addClass('in active');
});

$("#canvas").on("click",".panel .panel-title a",function(e){
    e.stopPropagation();
     var hh = $(this).attr("href");
     $(hh).toggleClass('in');
});



   $("#canvas").on("click","a",function(event){

      if($(this).hasClass("dropdown-toggle")){

      }else{
       event.preventDefault();
     }
   });





});

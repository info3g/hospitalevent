$(function(){
	
	

var items = $('.slider_content');
var genSlider = function(e){
   var self = this;
   self.currentIndex = 0;
   self.items = e.find('.image_slider .images');
   self.itemAmt = self.items.length;
   for(var l=0; l < self.itemAmt; l++){
    e.find('.bullets').append("<span></span>");
   }   
   
   self.cycleItems = function(){
     var item = e.find('.image_slider .images').eq(self.currentIndex);
     self.items.fadeOut();
     self.items.children('.title').removeClass('slide_up');
     self.make_bullet();
     item.children('.title').addClass('slide_up');
     item.fadeIn(1000);
     item = null;
   }
   
   e.find('.bullets span').click(function(){
      self.currentIndex = $(this).index();
      clearInterval(self.autoSlide);
      self.cycleItems();
      self.timer_slide();
   });

   e.find('.arrow_right').click(function() {
    self.clearInterval(autoSlide);
    self.currentIndex += 1;
    if (self.currentIndex > self.itemAmt - 1) {
      self.currentIndex = 0;
    }
    self.cycleItems($(this).parent().parent());
    self.timer_slide();
   });

   e.find('.arrow_left').click(function() {
     self.clearInterval(autoSlide);
     self.currentIndex -= 1;
     if (self.currentIndex < 0) {
       self.currentIndex = self.itemAmt - 1;
     }
     self.cycleItems();
     self.timer_slide();
    });

   //e.find(".images:gt(0)").hide(); 
   self.autoSlide;  
   self.timer_slide = function(){
     autoSlide = setInterval(function() {
       self.currentIndex += 1;
       if (self.currentIndex > self.itemAmt - 1) {
       self.currentIndex = 0;
       }
       self.cycleItems();
     },  3000);
   }
  self.timer_slide();
  self.make_bullet = function(){
   e.find('.bullets span').removeClass('select-bullet');
   e.find('.bullets span').eq(self.currentIndex).addClass('select-bullet');
  }
}

for(var k = 0;k<items.length;k++){
   new genSlider($(items[k]));   
}


	
})
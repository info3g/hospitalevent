  var barSlider = function(elm){
	
	    var self = this;
	    self.currentImage = 0;
	    self.imageWidth = parseInt(elm.css('width'));
		elm.find('li').css('width',self.imageWidth).css('height',elm.css('height'))
	    self.allImages = elm.find('li>.imgSrc').length;
        self.make_bullet = function(){
          elm.find('.bullets span').removeClass('select-bullet');
          elm.find('.bullets span').eq(self.currentImage).addClass('select-bullet');
        }
		for(var l=1; l<=self.allImages; l++){
         elm.find('.bullets').append("<span></span>");
        }  
		elm.find('ul').width(self.allImages*self.imageWidth);
		elm.find('.slideshow-next').click(function(){
        if(self.currentImage>=self.allImages){
		 self.setFlag();	
		 return false;
		}
 	    clearInterval(self.autoSlide);
        //increase image counter
        self.currentImage++;
        //calcualte and set position
        self.setFramePosition();
        self.timer_slide();
        });
		elm.find('.slideshow-prev').click(function(){
          if(self.currentImage<=0){
			 self.setFlag(); 
			 return false;
		 }
		clearInterval(self.autoSlide);
        self.currentImage--;      
        self.make_bullet();
        //calcualte and set position
        self.setFramePosition();
		self.timer_slide();
        });
		self.flag = true;
		self.autoSlide;
        self.timer_slide = function(){
			self.autoSlide = setInterval(function() {
				if(self.flag){
					self.currentImage += 1;
				}else{
					self.currentImage -= 1;
				}				
			    self.setFlag();
			    self.setFramePosition();
			},3000);
      }
	  self.setFlag = function(){
		  if(self.currentImage == self.allImages - 1) {
			   self.flag = false;
			}else if(self.currentImage == 0){
				self.flag = true;
			}
	  }
      elm.find('.bullets span').click(function(){
        self.currentImage = $(this).index();
        clearInterval(self.autoSlide);
		self.setFlag();
        self.setFramePosition();
        self.timer_slide();
      });
      
      self.setFramePosition = function(){
        //calculate position
        var px = self.imageWidth*self.currentImage*-1;
        //set ul left position
        elm.find('ul li').children('.title').removeClass('slide_up');
        self.make_bullet();
        elm.find('ul li').eq(self.currentImage).children('.title').addClass('slide_up');
        self.make_bullet();
        elm.find('ul').animate({
          left: px
        }, 300);
      }
      self.timer_slide();			
	}
	
		$(function(){
	 var sider_mixer_uk = $('.slideshow').length;	
	 for(var z=0;z<sider_mixer_uk;z++){
		new barSlider($('.slideshow').eq(z))  
	 }	
	  	 	
	});
	
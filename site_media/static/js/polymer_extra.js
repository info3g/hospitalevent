 function _toggle() {				  
                  var iconButton = Polymer.dom(event).localTarget;	  
                  var moreInfo = Polymer.dom(iconButton).parentNode;
				  moreInfo = moreInfo.querySelector(".more-info");
				  iconButton.icon = moreInfo.opened ? 'hardware:keyboard-arrow-up'
                                                    : 'hardware:keyboard-arrow-down';
                  moreInfo.toggle();
                }	
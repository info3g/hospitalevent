
function toggle_clp(selector) {
  document.querySelector(selector).toggle();
}

$(".ukbootstrapmenu li").click(function(){
   $(".navbar-nav li").removeClass("active");
   $(this).addClass("active");   
})

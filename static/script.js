$(function() {
   $('.article h2').hover( function(){
      $(this).parent().parent().parent().addClass("article-hover");
   },
   function(){
      $(this).parent().parent().parent().removeClass("article-hover");
   });
});
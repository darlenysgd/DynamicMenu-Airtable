
$( document ).ready(function() {
  $.get( "http://127.0.0.1:5000/menu", function( data ) {
  // $( ".result" ).html( data );
      $.each($.parseJSON(data), function(key,value){
          res = key.split(" ");
        $(".first").append("<li class='hassubs list1"+res[0]+"'"+"><a>"+res[0]+"</a></li>");
        $(".list1"+res[0]).append("<ul class='dropdown second"+res[0]+"'"+"></ul>");
          $.each(value.Submenu, function(ke,val){
              submenu = val;
              sm = submenu.split(" ");
              $(".second"+res[0]).append("<li class='subs hassubs list2"+res[0]+ke+"'"+"><a>"+val+"</a></li>")
              $(".list2"+res[0]+ke).append("<ul class='dropdown third"+res[0]+ke+"'"+"></ul>");
              $.each(value.action, function(k,v){
                if(v.Submenu === submenu){
                  console.log(v.Submenu + "/" + submenu);
                  $(".third"+res[0]+ke).append("<li class='subs'><a href="+v.url+">"+v.name+"</a><li>");
                }
              });
          });
      });
  })
});

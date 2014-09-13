
$(document).ready(function(){
$('.show_comment').click(function(e) {
    $(this).hide();
    $(this).next().show();
  });
});

$(document).ready(function(){
$('#show_all_comment').click(function(e) {
    $('.show_comment').hide();
    $('.show_comment').next().show();
  });
});

$(document).ready(function(){
$('#hide_all_comment').click(function(e) {
    $('.show_comment').show();
    $('.show_comment').next().hide();
  });
});


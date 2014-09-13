<script>
function AutoHide() {
  var elems = document.getElementsByClassName("all");
  alert(elems.length);
  for(var i = 0; i < elems.length; i++) {
    elems[i].style.visibility = "hidden";
  }
}
window.onload = AutoHide;
</script>

<!-- Let's add Vue here -->
<div id="app">
le message : {$ message $}
</div>

<script>

var app = new Vue({
      delimiters: ['{$', '$}'],
el: '#app',
data: {
message: 'Learning Vue',
}
});
</script>
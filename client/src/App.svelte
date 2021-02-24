<script>

  var bootstrap = document.createElement('script');
  bootstrap.src = 'https://code.jquery.com/jquery-3.3.1.slim.min.js';
  document.head.appendChild(bootstrap);
  var jquery = document.createElement('script');
  jquery.src = 'https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js';
  document.head.appendChild(jquery);
  var popper = document.createElement('script');
  popper.src = 'https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js';
  document.head.appendChild(popper);


  let str = "";
  let img = "";

  function makeRequest() {
    fetch("./stringtest")
      .then(d => d.text())
      .then(d => (str = d));
  }

  function loadImage(){
    fetch("./test")
      .then(response => response.blob())
      .then(blob => {
        img = URL.createObjectURL(blob)
      })

      console.log(img)
  }


</script>

<div class="container">
  <div class="row">
    <h1>Hello {str}</h1>
  </div>

  <button on:click={makeRequest} class="btn btn-primary">Make a request</button>
  <button on:click={loadImage} class="btn btn-secondary">Load image</button>
</div>

<div clas="container mt-5">
  <img src="{img}" alt="Queen of dragons">
</div>



<style>
  @import url("https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"); 
</style>
  
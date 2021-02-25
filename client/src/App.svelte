<script>

  // **** import di boostrap
  var bootstrap = document.createElement('script');
  bootstrap.src = 'https://code.jquery.com/jquery-3.3.1.slim.min.js';
  document.head.appendChild(bootstrap);
  var jquery = document.createElement('script');
  jquery.src = 'https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js';
  document.head.appendChild(jquery);
  var popper = document.createElement('script');
  popper.src = 'https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js';
  document.head.appendChild(popper);
  // ****** end
  
  import ImgEncoder from 'svelte-image-encoder';
  
  let url, src, realTime = true, uploadedimg;
  
	function loadFile(e) {
    src = URL.createObjectURL(e.target.files[0]);
	}

  // function loadImage(){
  //   fetch("./test")
  //     .then(response => response.blob())
  //     .then(blob => {
  //       img = URL.createObjectURL(blob)
  //     })
  // }
  
  function median(){
    fetch("./median")
      .then(response => response.blob())
      .then(blob => {
        uploadedimg = URL.createObjectURL(blob)
      })
  }

  function mean(){
    fetch("./mean")
      .then(response => response.blob())
      .then(blob => {
        uploadedimg = URL.createObjectURL(blob)
      })
  }

  function upload(){

    fetch('./upload', {
      method: 'POST',
      body: url
    })
    .then(response => response.blob())
    .then(blob => {
      uploadedimg = URL.createObjectURL(blob)
    })
    .catch(error => {
      console.error('Error:', error);
    });

  }


</script>

<div class="container">
  <div class="jumbotron">    
    <p><input on:change={loadFile} type='file'>
    <ImgEncoder {src} bind:url {realTime} width={256} height={256} crossOrigin='anonymous' classes='profile-image'/>

    <button class="btn btn-primary" on:click={upload}>Upload</button>
  </div>
</div>

<img src="{uploadedimg}" alt="uploaded img">


<div class="container mt-2">
  <div class="row">
    <div class="col">
      LOAD DEFAULT IMAGE...
      <!-- <button on:click={loadImage} class="btn btn-secondary">Load default image</button> -->
    </div>
    <div class="col">
      <button on:click={median} class="btn btn-warning">Median</button>
    </div>
    <div class="col">
      <button on:click={mean} class="btn btn-warning">Mean</button>
    </div>
  </div>
</div>

<div class="container mt-2 ">
  <div class="row justify-content-center align-items-center">
    <img src="{uploadedimg}" alt="Queen of dragons">
  </div>
</div>



<style>
  @import url("https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css");

	:global(.profile-image) { /* Ideally, something like this would go in a global theme definition CSS */
		box-shadow: 2px 2px 8px rgba(0,0,0,.85);
		margin: 1em;
	}
	p {
		word-break: break-word;
	}
	img {
		margin: 1em;
	}
</style>
  
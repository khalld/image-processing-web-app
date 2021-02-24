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

  import ImgEncoder from 'svelte-image-encoder';
  let str = "", img = "";

  let src='https://raw.githubusercontent.com/sveltejs/svelte/29052aba7d0b78316d3a52aef1d7ddd54fe6ca84/site/static/images/svelte-android-chrome-512.png';
  let url;
	let quality = 0.1;
	let imageChosen = false;
	let realTime = true;
	let showResult = true;

	function loadFile(e) {
		src = URL.createObjectURL(e.target.files[0]);
	}


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
  }
  
  function median(){
    fetch("./median")
      .then(response => response.blob())
      .then(blob => {
        img = URL.createObjectURL(blob)
      })
  }

  function mean(){
    fetch("./mean")
      .then(response => response.blob())
      .then(blob => {
        img = URL.createObjectURL(blob)
      })
  }

  function upload(){

    fetch('./uploadtest', {
      method: 'POST',
      body: url
    })
    .then(response => console.log(response))
    // .then(result => {
    //   console.log('Success:', result);
    // })
    // .catch(error => {
    //   console.error('Error:', error);
    // });

    console.log(url)

  }


</script>

<div class="container">
  <div class="jumbotron">
    <h1>Upload your image</h1>
    <p class="lead"></p>
    <!-- <form id="upload-form" action="{{ url_for('upload') }}" method="POST" enctype="multipart/form-data"> -->
      <!-- <input id="file-picker" type="file" name="file" accept="image/*" class="hidden" onchange="{() => console.log("AEE")}">
      <label for="file-picker" class="btn btn-lg btn-success">Select file</label> -->
    <!-- </form> -->
    <p><input on:change={loadFile} type='file' > Quality: <input type='number' bind:value={quality} min='0' max='1' step='0.05'></p>

    <ImgEncoder {src} bind:url {realTime} width={256} height={256} crossOrigin='anonymous' classes='profile-image'/>
    <img src={url} alt=''>

    <!-- <p>Result ({url && url.length} bytes):</p> -->
    <!-- <p>{ url }</p> -->

    <button class="btn btn-primary" on:click={upload}>Upload</button>
  </div>
</div>



<div class="container">
  <div class="row">
    <h1>Hello {str}</h1>
  </div>
  <button on:click={makeRequest} class="btn btn-primary">req return str</button>
</div>

<div class="container mt-2">
  <div class="row">
    <div class="col">
      <button on:click={loadImage} class="btn btn-secondary">Load default image</button>
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
    <img src="{img}" alt="Queen of dragons">
  </div>
</div>



<style>
  @import url("https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css");

  :global(body) {
		overflow: hidden;
		width: 100%;
	}
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
  
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
  import TableRow from './components/TableRow.svelte'
  
  let url, src, realTime = true, uploadedimg, processedImage, w = 256, h=256;
  
	function loadFile(e) {
    src = URL.createObjectURL(e.target.files[0]);
	}

  function median(){
    fetch("./median")
      .then(response => response.blob())
      .then(blob => {
        processedImage = URL.createObjectURL(blob)
      })
  }

  function mean(){
    fetch("./mean")
      .then(response => response.blob())
      .then(blob => {
        processedImage = URL.createObjectURL(blob)
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

<div class="d-flex">
  <div class="p-2 flex-fill">
    <input on:change={loadFile} type='file'>
  </div>
  <div class="p-2 flex-fill">
    <button class="btn btn-primary" on:click={upload}>UPLOAD</button>
  </div>
</div>

<div class="d-flex">
  <div class="p-2 flex-fill">
    <p>Choosed image</p>
    <ImgEncoder {src} bind:url {realTime} width={w} height={h} crossOrigin='anonymous' classes='image'/>
  </div>
  <div class="p-2 flex-fill">
    <p>Immagine di riferimento</p>
    <img src="{uploadedimg}" class="image" width={w} height={h} alt="uploaded img">
  </div>
  <div class="p-2 flex-fill">
    <p>Processed image</p>
    <img src="{processedImage}" class="image" width={w} height={h} alt="uploaded img">
  </div>
</div>

<table class="table">
  <thead>
    <tr>
      <th scope="col">#</th>
      <th scope="col">Method</th>
    </tr>
  </thead>

  <TableRow method={median} name="Median" numberRow="1"/>
  <TableRow method={mean} name="Mean" numberRow="2"/>
  <TableRow method={() => console.log("TODO..")} name="Bilateral" numberRow="3"/>
  <TableRow method={() => console.log("TODO..")} name="Guided" numberRow="4"/>

</table>


<style>
  @import url("https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css");

	:global(.image) {
		box-shadow: 2px 2px 8px rgba(0,0,0,.85);
	}
</style>
  
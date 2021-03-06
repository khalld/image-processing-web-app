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
  
  // import ImgEncoder from 'svelte-image-encoder';   // da cancelalre
  import TableRow from './components/TableRow.svelte';

  // Ho provato a togliere l'upload ma non ha senso! perché in qualche modo devo avere l'immagine di riferimento in backend!

  let urlBase64, //src, realTime = true, 
  uploadedimg, processedImage, filterName, loading = false,
      kernel_dim_median = 3, kernel_dim_mean = 3, bilateralObj = { 
        radius: 7,
        sigma_d: 7,
        sigma_r: 6.5
      };

  let fileinput;

  const loadFile =(e)=>{
    let image = e.target.files[0];
    let reader = new FileReader();
    reader.readAsDataURL(image);
    reader.onload = e => {
      // console.log("BASE 64 IMG", e.target.result)
      urlBase64 = e.target.result
    };
  }

  async function median(){
    loading = true;
    fetch("./median", {
      method: 'post',
      headers: {
        'Content-type': 'application/json'
      },
      body: JSON.stringify({
        kernel_dim: kernel_dim_median
      })
    })
      .then(response => response.blob())
      .then(blob => {
        loading = false;
        processedImage = URL.createObjectURL(blob)
        filterName = "median filter";
      })
  }

  function mean(){
    loading = true;
    fetch("./mean", {
      method: 'post',
      headers: {
        'Content-type': 'application/json'
      },
      body: JSON.stringify({
        kernel_dim: kernel_dim_mean
      })
    })
      .then(response => response.blob())
      .then(blob => {
        loading = false;
        processedImage = URL.createObjectURL(blob)
        filterName = "mean";
      })
  }


  function bilateral(){
    loading = true;
    fetch("./bilateral", {
      method: 'post',
      headers: {
        'Content-type': 'application/json'
      },
      body: JSON.stringify({
        radius: bilateralObj.radius,
        sigma_d: bilateralObj.sigma_d,
        sigma_r: bilateralObj.sigma_r
      })
    })
      .then(response => response.blob())
      .then(blob => {
        loading = false;
        processedImage = URL.createObjectURL(blob)
        filterName = "bilateral";
      })
  }

  function upload(){
    fetch('./upload', {
      method: 'POST',
      body: urlBase64
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
    <input on:change={(e) => loadFile(e)} bind:this={fileinput} type='file'>
  </div>
  <div class="p-2 flex-fill">
    <button class="btn btn-primary" on:click={upload}>UPLOAD</button>
  </div>
</div>

<div class="d-flex">
  <!-- <div class="p-2 flex-fill">
    <p>Choosed image</p>
    <img class="loaded-img" src="{loadedimg}" alt="d" />
  </div> -->
  <div class="p-2 flex-fill">
    <p>Immagine di riferimento</p>
    <img src="{uploadedimg}" class="image" alt="uploaded img">
  </div>

  <div class="p-2 flex-fill">
      <p>Processed image {#if filterName}with {filterName}{/if}</p>
    {#if loading == false}
      <img src="{processedImage}" class="image" alt="uploaded img">
    {:else if loading == true}
    (lo spinner non si vede, fixa)
    <div class="d-flex justify-content-center">
      <div class="spinner-border" role="status">
        <span class="sr-only">Loading...</span>
      </div>
    </div>
    {/if}
  </div>

</div>

<table class="table">
  <thead>
    <tr>
      <th scope="col">Name</th>
      <th scope="col">Variable</th>
      <th></th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <th scope="row">Median filter</th>
      <td>
        <label>Kernel dimension</label>
        <input type="number" bind:value={kernel_dim_median}/>
      </td>
      <td><button on:click={median} class="btn btn-warning">Apply</button></td>
    </tr>

    <tr>
      <th scope="row">Mean</th>
      <td>
        <label>Kernel dimension</label>
        <input type="number" bind:value={kernel_dim_mean}/>
      </td>
      <td><button on:click={mean} class="btn btn-warning">Apply</button></td>
    </tr>

    <tr>
      <th scope="row">Bilateral filter</th>
      <td>
        <div class="row">
          <div class="col">
            <label>Radius</label>
            <input type="number" bind:value={bilateralObj.radius}/>
          </div>
          <div class="col">
            <label>Sigma d</label>
            <input type="number" bind:value={bilateralObj.sigma_d}/>
          </div>
          <div class="col">
            <label>Sigma r</label>
            <input type="number" bind:value={bilateralObj.sigma_r}/>
          </div>
        </div>
      </td>
      <td><button on:click={bilateral} class="btn btn-warning">Apply</button></td>
    </tr>

  </tbody>

  <!-- <TableRow method={() => console.log("TODO..")} name="Guided" numberRow="4"/> -->

</table>


<style>
  @import url("https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css");

	:global(.image) {
		box-shadow: 2px 2px 8px rgba(0,0,0,.85);
	}
</style>
  
<script>
  // ***** IMPORT BOOTSTRAP ********
  var boostrapStile = document.createElement('link');
  boostrapStile.href = 'https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css';
  boostrapStile.rel = 'stylesheet';
  boostrapStile.integrity = 'sha384-BmbxuPwQa2lc/FVzBcNJ7UAyJxM6wuqIj61tLrc4wSX0szH/Ev+nYRRuWlolflfl';
  boostrapStile.crossOrigin = 'anonymous';
  document.head.appendChild(boostrapStile)

  var bootstrap = document.createElement('script');
  bootstrap.src = 'https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/js/bootstrap.bundle.min.js';
  bootstrap.integrity = 'sha384-b5kHyXgcpbZJO/tY9Ul7kGkf1S0CWuKcCD38l8YkeH8z8QjE0GmW1gYU5S9FOnJ0';
  bootstrap.crossOrigin = 'anonymous'
  document.head.appendChild(bootstrap);
  // ***** END IMPORT BOOTSTRAP ********

  // ***** variabili:
  let urlBase64, uploadedimg, processedImage, filterName, loading = false,
    kernel_dim_median = 3, kernel_dim_mean = 3, 
    bilateralObj = { 
      radius: 7,
      sigma_d: 7,
      sigma_r: 6.5
    };


  const loadFile =(e)=>{
    let reader = new FileReader();
    reader.readAsDataURL(e.target.files[0]);

    if(e.target.files[0].type.includes('image')){
      reader.onload = e => {
        urlBase64 = e.target.result
      };
    } else {
      alert("Il file importato non è un'immagine!");
    }

  }

  function upload(){
    fetch('./upload', {
      method: 'POST',
      headers: {
        'Content-type': 'application/json'
      },
      body: JSON.stringify({
        image: urlBase64
      })
    })
    .then(res => {
      if(res.ok){
        return res.blob()
      }
    })
    .then(blob => uploadedimg = URL.createObjectURL(blob))
    .catch(error => {
      alert("E' possibile caricare file solo con formato immagine");
      console.error('Error:', error)
    });
  }

  function download(){
    window.location.href = processedImage
  }


  function median(){
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

</script>



<div class="d-flex">
  <div class="p-2 flex-fill">
    <input on:change={(e) => loadFile(e)} type='file' accept='image/x-png,image/gif,image/jpeg'>
  </div>
  <div class="p-2 flex-fill">
    <button class="btn btn-primary text-uppercase" on:click={upload}>upload</button>
  </div>
  {#if processedImage}
  <div class="p-2 flex-fill">
    <button class="btn btn-secondary text-uppercase" on:click={download}>download</button>
  </div>
  {/if}
</div>


<div class="d-flex">
  <div class="p-2 flex-fill">
    {#if uploadedimg}
      <h3>Immagine di riferimento</h3>
      <img src="{uploadedimg}" class="image" alt="uploaded img">
    {:else}
      <h3>Seleziona un'immagine</h3>
    {/if}
  </div>

  <div class="p-2 flex-fill">
    {#if loading == false && processedImage}
      <p>Processed image {#if filterName}with {filterName}{/if}</p>
      <img src="{processedImage}" class="image" alt="uploaded img">
    {:else if loading == true}
    <div class="d-flex justify-content-center">
      <div class="spinner-border text-warning" style="width: 7rem; height: 7rem;" role="status">
        <span class="visually-hidden">Loading...</span>
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

</table>


<style>
	:global(.image) {
		box-shadow: 2px 2px 8px rgba(0,0,0,.85);
	}
</style>
  
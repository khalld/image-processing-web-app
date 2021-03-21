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
    meanObj = {kernelDim: 3},
    medianObj = { kernelDim: 3},
    bilateralObj = { 
      sigma_d: 8,
      sigma_r: 0.4
    },
    guidedObj = {
      radius: 8,
      eps: 0.16
    },
    cannyObj = {
      kernelDim: 3,
      lower_th: 0.1,
      higher_th: 0.8
    }
  
  function isUploaded() {
    if(uploadedimg != undefined){
      return true;
    } else {
      alert("Necessario upload di un'immagine prima di effettuare l'operazione!")
      return false;
    }
  }

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

  function mean(){
    if(meanObj.kernelDim < 3){
      alert("La dimensione minima consentita per la finestra è 3x3!")
    } else {
      if(isUploaded()) {
        loading = true;
        fetch("./mean", {
          method: 'post',
          headers: {
            'Content-type': 'application/json'
          },
          body: JSON.stringify({
            kernel_dim: meanObj.kernelDim
          })
        })
        .then(response => response.blob())
        .then(blob => {
          processedImage = URL.createObjectURL(blob)
          filterName = "di media arimetica";
          loading = false;
        })
      }
    }


  }

  function median(){
    if(medianObj.kernelDim < 3){
      alert("La dimensione minima consentita per la finestra è 3x3!")
    } else {
      if(isUploaded()){
        loading = true;
        fetch("./median", {
          method: 'post',
          headers: {
            'Content-type': 'application/json'
          },
          body: JSON.stringify({
            kernel_dim: medianObj.kernelDim
          })
        })
        .then(response => response.blob())
        .then(blob => {
          processedImage = URL.createObjectURL(blob)
          filterName = "mediano";
          loading = false;
        })
      }
    }


  }

  function bilateral(){
    if(bilateralObj.sigma_d < 2 || bilateralObj.sigma_r < 0.1 ){
      alert("Valore minimo per il sigma_d è 2, per sigma_r 0.01")
    } else {
      if(isUploaded()){
        loading = true;
        fetch("./bilateral", {
          method: 'post',
          headers: {
            'Content-type': 'application/json'
          },
          body: JSON.stringify({
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
    }

  }

  function guided(){

    if(guidedObj.radius < 2 || guidedObj.eps < 0.01){
      alert("Valore minimo per il raggio è 2, per la regolarizzazione 0.01")
    } else {
      if(isUploaded()){
        loading = true;
        fetch("./guided", {
          method: 'post',
          headers: {
            'Content-type': 'application/json'
          },
          body: JSON.stringify({
            radius: guidedObj.radius,
            eps: guidedObj.eps
          })
        })
        .then(response => response.blob())
        .then(blob => {
          loading = false;
          processedImage = URL.createObjectURL(blob)
          filterName = "guided"
        })
      }
    }


  }

  function canny(){
    if(cannyObj.kernelDim < 3 || cannyObj.lower_th < 0.1 || cannyObj.higher_th < 0.2){
      alert("Valore minimo per la dimensione della finestra è 3, per il lower threhsold 0.1 e per l'higher threhsold 0.2")
    } else {
      if(isUploaded()){
        loading = true;
        fetch("./canny", {
          method: 'post',
          headers: {
            'Content-type': 'application/json'
          },
          body: JSON.stringify({
            kernel_dim: cannyObj.kernelDim,
            lower_threshold: cannyObj.lower_th,
            higher_threshold: cannyObj.higher_th
          })
        })
          .then(response => response.blob())
          .then(blob => {
            loading = false;
            processedImage = URL.createObjectURL(blob)
            filterName = "canny"
          })
      }
    }
  }

  function psnr(){
    if(isUploaded()){
      fetch("./psnr", {
        method: 'get'
      })
      .then(response => response.text())
      .then(myPsnr => {
        console.log(myPsnr)
      })
      .catch(err => {console.log("error", err)})
    }

  }

</script>

<div class="d-flex">
  <div class="p-2 flex-fill">
    <input class="form-control form-control-lg" on:change={(e) => loadFile(e)} type='file' accept='image/x-png,image/gif,image/jpeg'>
  </div>
  <div class="p-2 flex-fill">
    <button class="btn btn-primary text-uppercase btn-lg" on:click={upload}>upload</button>
  </div>
  {#if processedImage}
  <div class="p-2 flex-fill">
    <button class="btn btn-success text-uppercase btn-lg" on:click={download}>download</button>
  </div>
  {/if}

  <button class="btn btn-info text-uppercase btn-lg" on:click={psnr}>PSNR</button>
</div>


<div class="d-flex">
  <div class="p-2 flex-fill">
    {#if uploadedimg}
      <h3>Immagine di riferimento</h3>
      <img src="{uploadedimg}" class="image img-thumbnail" alt="uploaded-img">
    {:else}
      <h3>Seleziona un'immagine</h3>
    {/if}
  </div>

  <div class="p-2 flex-fill">
    {#if loading == false && processedImage}
      <h3>Immagine processata {#if filterName}con: {filterName}{/if}</h3>
      <img src="{processedImage}" class="image img-thumbnail" alt="processed-img">
    {:else if loading == true}
    <div class="d-flex justify-content-center">
      <div class="spinner-border text-warning" style="width: 7rem; height: 7rem;" role="status">
        <span class="visually-hidden">Loading...</span>
      </div>
    </div>
    {/if}
  </div>

</div>

<table class="table table-light table-striped">
  <thead class="table-dark">
    <tr>
      <th scope="col">Nome filtro</th>
      <th></th>
      <th></th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <th scope="row">Filtro di media arimetica</th>
      <td>
        <div class="form-floating">
          <input type="number" class="form-control" id="mean-kernel" bind:value={meanObj.kernelDim}>
          <label for="mean-kernel">Dimensione finestra</label>
        </div>
      </td>
      <td><button on:click={mean} class="btn btn-warning">Applica</button></td>
    </tr>

    <tr>
      <th scope="row">Filtro mediano</th>
      <td>
        <div class="form-floating">
          <input type="number" class="form-control" id="median-kernel" bind:value={medianObj.kernelDim}>
          <label for="median-kernel">Dimensione finestra</label>
        </div>
      </td>
      <td><button on:click={median} class="btn btn-warning">Applica</button></td>
    </tr>

    <tr>
      <th scope="row">Bilateral filter</th>

      <td>
        <div class="row g-2">
          <div class="col-md">
            <div class="form-floating">
              <input type="number" class="form-control" id="sigmaDBilateral" bind:value={bilateralObj.sigma_d}>
              <label for="sigmaDBilateral">Sigma_d</label>
            </div>
          </div>
          <div class="col-md">
            <div class="form-floating">
              <input type="number" class="form-control" id="sigmaRBilateral" bind:value={bilateralObj.sigma_r}>
              <label for="sigmaRBilateral">Sigma_r</label>
            </div>
          </div>
        </div>
      </td>
      <td><button on:click={bilateral} class="btn btn-warning">Apply</button></td>
    </tr>

    <tr>
      <th scope="row">Filtro guided</th>
      <td>
        <div class="row g-2">
          <div class="col-md">
            <div class="form-floating">
              <input type="number" class="form-control" id="radiusGuided" min=2 bind:value={guidedObj.radius}>
              <label for="radiusGuided">Raggio</label>
            </div>
          </div>
          <div class="col-md">
            <div class="form-floating">
              <input type="number" class="form-control" id="regularization" min=0.01 bind:value={guidedObj.eps}>
              <label for="regularization">Regolarizzazione</label>
            </div>
          </div>
        </div>
      </td>
      <td><button on:click={guided} class="btn btn-warning">Applica</button></td>
    </tr>

    <tr>
      <th scope="row">Canny edge detection</th>
      <td>
        <div class="row g-2">
          <div class="col-md">
            <div class="form-floating">
              <input type="number" class="form-control" id="kernel_dimension_canny" bind:value={cannyObj.kernelDim}>
              <label for="kernel_dimension_canny">Dimensione kernel smoothing</label>
            </div>
          </div>
          <div class="col-md">
            <div class="form-floating">
              <input type="number" class="form-control" id="lower_th_canny" bind:value={cannyObj.lower_th}>
              <label for="lower_th_canny">Lower thresholding</label>
            </div>
          </div>
          <div class="col-md">
            <div class="form-floating">
              <input type="number" class="form-control" id="higher_th_canny" bind:value={cannyObj.higher_th}>
              <label for="higher_th_canny">Higher thresholding</label>
            </div>
          </div>
        </div>
      </td>
      <td><button on:click={canny} class="btn btn-warning">Applica</button></td>
    </tr>

    
  </tbody>
</table>


<style>
	:global(.image) {
		box-shadow: 2px 2px 8px rgba(0,0,0,.85);
	}
</style>
  
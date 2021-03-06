<script>
  export let name;
  export let method;
  export let numberRow;
  export let algorithmType;

</script>


<tbody>
  <tr>
    <th scope="row">{numberRow}</th>
    <td><button on:click={method} class="btn btn-warning">{name}</button></td>
  </tr>
</tbody>
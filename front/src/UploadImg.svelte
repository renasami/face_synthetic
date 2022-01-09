<script lang="ts">
	let file
    let src
	const reader = new FileReader();
	reader.onload = () => {
        src = reader.result;
	};
	reader.onerror = (error) => {
	  console.log('Error: ', error);
	};
	const convertToBase64 = () => {
		reader.readAsDataURL(file[0]);
	}

</script>
<div>
	<input id="1" bind:files={file} type="file" on:change={convertToBase64}/>
</div>

<style>
	div {
		text-align: center;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
	}


</style>
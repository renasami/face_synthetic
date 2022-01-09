<script lang="ts">
	import UploadImg from "./UploadImg.svelte"
	import {convertedImages} from "./store"
	const upload = () => {
		console.log($convertedImages)
	}
</script>
<main>
	
</main>
	<UploadImg/>
	<UploadImg/>
	<button on:click={upload}>Upload</button>
<style>
	main {
		text-align: center;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
	}


</style>
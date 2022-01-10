<script lang="ts">
	import UploadImg from "./UploadImg.svelte"
	import {convertedImages, convertedImages, convertedImages, convertedImages} from "./store"
	const upload = () => {
		console.log($convertedImages)
	}
	if ($convertedImages.length == 0) {
		convertedImages.update(()=> Array(2).map(_ => null))
		console.log($convertedImages)
	}
</script>
<main>
	
</main>
	<UploadImg index=0 />
	<UploadImg index=1/>
	<button on:click={upload}>Upload</button>
<style>
	main {
		text-align: center;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
	}


</style>
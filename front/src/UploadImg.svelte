<script lang="ts">
    import {convertedImages} from "./store"
	let file
    let img
	const reader = new FileReader();
	reader.onload = () => {
        img = reader.result;
        storeUpdate(img)
	};
	reader.onerror = (error) => {
	  console.log('Error: ', error);
	};
	const convertToBase64 = () => {
		reader.readAsDataURL(file[0]);
	}
    const storeUpdate = (img:string | ArrayBuffer) => {
        convertedImages.update((imgs) => [...imgs,img])
    };

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
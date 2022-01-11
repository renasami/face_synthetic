<script lang="ts">
	import UploadImg from "./UploadImg.svelte"
	import {convertedImages} from "./store"
	let src=""
	let decodedImg=""
	const url = "http://127.0.0.1:8000"

	const upload = async () => {
		// axios.defaults.headers.post = null;
		if ($convertedImages.length == 0) return
		console.log($convertedImages)
		const q = JSON.stringify($convertedImages)
		const url = `http://localhost:8000/img_save`
		const headers = {
			'Accept': 'application/json',
			'Content-Type': 'application/json'
		};
		const data = {
			method: "POST",	
			header:headers,
			body:JSON.stringify($convertedImages)
		}
		
		const resp = await fetch(url,data)
		const text = await resp.json()
		src = text
	}
	if ($convertedImages.length == 0) {
		convertedImages.update(()=> Array(2).map(_ => null))
	}
	const test = async () => {
		const a = "%5B%22SGVsbG8sIHdvcmxk%22%2C%22SGVsbG8sIHdvcmxk%22%5D"
		const headers = {
			'Accept': 'application/json',
			'Content-Type': 'application/json'
			};
		const data =[
			{foo:"YWFh"},
			{foo:"YWFh"}
		];
		const resp = await fetch(`http://localhost:8000/test`,{
			method:"POST",
			headers,
			// mode:"no-cors",
			body:JSON.stringify(data)
		})
		const d = await resp.json()
  		console.log(d)	
	}
	</script>
<main>
	
</main>
	<UploadImg index=0 />
	<UploadImg index=1/>
	<!-- <button on:click={test}>test</button> -->
	<button on:click={upload}>Upload</button>
	<img src={src} alt="non" />
<style>
	main {
		text-align: center;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
	}


</style>
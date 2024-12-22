
<script setup>

  const fetchProtected = () => {
    console.log("fetch protected api endpoint.")
    axios.get("http://127.0.0.1:8000/api/v1/todo/")
    .then( res => {
      console.log("API response: ", res)
    })
    .catch ( err => {
      console.log("error: ", err.response.data)
    })
  }

</script>
<template>
<button> custom login with Google </button>
<button @click="fetchProtected"> fetch protected </button>
</template>



<script setup>
  import axios from 'axios'
  import { googleAuthCodeLogin } from "vue3-google-login"
  axios.defaults.withCredentials = true

  const login = () => {
    googleAuthCodeLogin().then((response) => {
      console.log("received auth code from google:", response)
      axios.post('http://127.0.0.1:8000/api/v1/google-code-exchange/', response)
      .then((res) => {
        console.log("login success.", res)
      })
      .catch((error) => {
        console.log("login failed.", error.response.data)
      })
    })
  }

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
<button @click="login"> custom login with Google </button>
<button @click="fetchProtected"> fetch protected </button>
</template>


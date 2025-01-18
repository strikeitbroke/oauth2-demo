import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import vue3GoogleLogin from 'vue3-google-login'

const app = createApp(App)

app.use(vue3GoogleLogin, {
  clientId: '329690757308-jlij67amtq4os4056kvui98bse4v9ebr.apps.googleusercontent.com'
})

app.mount('#app')

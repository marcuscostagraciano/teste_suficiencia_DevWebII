import { createApp } from 'vue'
import router from './router'
import {createPinia} from 'pinia'

import './style.css'
import App from './App.vue'

createApp(App)
    .use(createPinia())
    .use(router)
    .mount('#app')

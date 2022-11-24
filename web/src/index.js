import {createApp} from "vue";
import {createRouter, createWebHistory} from "vue-router";
import axios from 'axios'

import App from "./App.vue";
import Home from "./Home.vue"
import Login from "./Login.vue"
import Hardware from "./components/Hardware.vue"

const router = createRouter({
  history: createWebHistory(),
  routes: [
        { path: '/', name:'Vue', component: Home },
        { path: '/login', name:'LoginPage', component: Login}
    ]
})

axios.defaults.withCredentials = true;
createApp(App).use(router).mount('#app')

import {createApp} from "vue";
import {createRouter, createWebHistory} from "vue-router";
import axios from 'axios'

import App from "./App.vue";
import Home from "./Home.vue"
import Login from "./Login.vue"
import Hardware from "./Hardware.vue"

const router = createRouter({
  history: createWebHistory(),
  routes: [
        { path: '/', name:'Vue', component: Home },
        { path: '/login', name:'LoginPage', component: Login},
        { path: '/hardware', name:'HardwarePage', component: Hardware}
    ]
})

axios.defaults.headers.common['Access-Control-Allow-Origin'] = '*';
axios.defaults.headers.common['Access-Control-Allow-Credentials'] = 'true';
axios.defaults.withCredentials = true;

createApp(App).use(router).mount('#app')

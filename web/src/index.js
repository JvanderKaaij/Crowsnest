import {createApp} from "vue";
import {createRouter, createWebHistory} from "vue-router";
import App from "./App.vue";
import Home from "./Home.vue"
import Login from "./Login.vue"

const router = createRouter({
  history: createWebHistory(),
  routes: [
        { path: '/', name:'Vue', component: Home },
        { path: '/login', name:'LoginPage', component: Login}
    ]
})

createApp(App).use(router).mount('#app')

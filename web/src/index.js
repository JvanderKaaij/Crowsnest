import {createApp} from "vue";
import {createRouter, createWebHistory} from "vue-router";
import axios from 'axios';
import { createStore } from "vuex";

import App from "./App.vue";
import Home from "./Home.vue";
import Login from "./Login.vue";

const router = createRouter({
  history: createWebHistory(),
  routes: [
        { path: '/', name:'Vue', component: Home },
        { path: '/login', name:'LoginPage', component: Login}
    ]
});

const store = createStore({
    state(){
        return {
            students: {},
            hardware: {}
        };
    },
    mutations:{
        UpdateStudents(state, data){
            state.students = data;
        },
        UpdateHardware(state, data){
            state.hardware = data;
        }
    },
    actions:{
        async InitStudents(context){
            axios
            .get('http://localhost:8000/students')
            .then(response => {
              context.commit('UpdateStudents', response.data);
            });
        },
        async InitHardware(context){
            axios
            .get('http://localhost:8000/hardware')
            .then(response => {
                context.commit('UpdateHardware', response.data);
            });
        }
    },
    getters:{
        //can be used as a return state with extra functionality
    }
});

axios.defaults.withCredentials = true;
createApp(App).use(router).use(store).mount('#app');

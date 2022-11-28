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
        EditStudents(state, data){
            var send_obj = {};
            send_obj["id"] = data.id;
            send_obj[data.value_endpoint_type] = data.value;
            axios
              .post('http://localhost:8000/edit_student', send_obj)
              .then(response => {
                  console.log(response);
              })
        },
        EditHardware(state, data){
            var send_obj = {};
            send_obj["id"] = data.id;
            send_obj[data.value_endpoint_type] = data.value;
            axios
              .post('http://localhost:8000/edit_hardware', send_obj)
              .then(response => {
                  console.log(response);
              })
        },
        CreateStudents(state, data){
            state.students = data;
        },
        CreateHardware(state, data){
            state.hardware = data;
        }
    },
    actions:{
        async InitStudents(context){
            axios
            .get('http://localhost:8000/students')
            .then(response => {
              context.commit('CreateStudents', response.data);
            });
        },
        async InitHardware(context){
            axios
            .get('http://localhost:8000/hardware')
            .then(response => {
                context.commit('CreateHardware', response.data);
            });
        }
    },
    getters:{
        //can be used as a return state with extra functionality
    }
});

axios.defaults.withCredentials = true;
createApp(App).use(router).use(store).mount('#app');

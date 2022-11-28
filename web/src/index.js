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
            students: [],
            hardware: []
        }
    },
    mutations:{
        InitStudents(state, data){
            state.students = data;
        },
        AddStudent(state, data){
            state.students.push(data);
            var form_data = new FormData();
            for ( var key in data ) {
                form_data.append(key, data[key]);
            }

            axios
            .post('http://localhost:8000/add_student', form_data, {
                headers: {
                  'Content-Type': 'multipart/form-data'
                }
              })
            .then(response => {
              console.log(response.data);
            });
        },
        EditStudents(state, data){
            var send_obj = {};
            send_obj["id"] = data.id;
            send_obj[data.value_endpoint_type] = data.value;
            axios.post('http://localhost:8000/edit_student', send_obj);
        },
        InitHardware(state, data){
            state.hardware = data;
        },
        AddHardware(state, data){
            state.hardware.push(data);
            var form_data = new FormData();
            for ( var key in data ) {
                form_data.append(key, data[key]);
            }

            axios
            .post('http://localhost:8000/add_hardware', form_data, {
                headers: {
                  'Content-Type': 'multipart/form-data'
                }
              })
            .then(response => {
              console.log(response.data);
            });
        },
        EditHardware(state, data){
            var send_obj = {};
            send_obj["id"] = data.id;
            send_obj[data.value_endpoint_type] = data.value;
            axios.post('http://localhost:8000/edit_hardware', send_obj);
        }
    },
    actions:{
        async InitStudents(context){
            axios
            .get('http://localhost:8000/students')
            .then(response => {
              context.commit('InitStudents', response.data);
            });
        },
        async InitHardware(context){
            axios
            .get('http://localhost:8000/hardware')
            .then(response => {
                context.commit('InitHardware', response.data);
            });
        }
    },
    getters:{
        //can be used as a return state with extra functionality
    }
});

axios.defaults.withCredentials = true;
createApp(App).use(router).use(store).mount('#app');

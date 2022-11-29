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

function ToFormDate(data){
    var form_data = new FormData();
    for ( var key in data ) {
        if(data[key] != null){
            form_data.append(key, data[key]);
        }
    }
    return form_data;
}


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
            var form_data = ToFormDate(data.data);
            axios
            .post('http://localhost:8000/add_student', form_data, {
                headers: {
                  'Content-Type': 'multipart/form-data'
                }
              })
            .then(response => {
                if(response.data.success){
                    state.students.push(data.data);
                    data.success();
                }else{
                    data.onError(response.data.errors);
                }
            });
        },
        EditStudents(state, data){
            var send_obj = {};
            send_obj["id"] = data.id;
            send_obj[data.value_endpoint_type] = data.value;
            axios.post('http://localhost:8000/edit_student', send_obj);
        },
        RemoveStudent(state, student){
            state.modal_popup_active = 'Are you sure?';

            //student is selected in hardware
            if(state.hardware.find(x => x.student_id === student.id)){
                state.modal_popup_active = 'Are you sure? This student has hardware assigned!';
            }

            state.modal_popup_agree = () => {
                state.students.find(e => e.id === student.id)['active'] = 0
                this.commit('EditStudents', {id:student.id, value_endpoint_type: 'active', value:0});
                state.modal_popup_active = null;
            }
            state.modal_popup_deny = () => {
                state.modal_popup_active = null;
            }
        },
        InitHardware(state, data){
            state.hardware = data;
        },
        AddHardware(state, data){
            var form_data = ToFormDate(data.data);
            axios
            .post('http://localhost:8000/add_hardware', form_data, {
                headers: {
                  'Content-Type': 'multipart/form-data'
                }
              })
            .then(response => {
                if(response.data.success){
                    state.students.push(data.data);
                    data.success();
                }else{
                    data.onError(response.data.errors);
                }
            });
        },
        EditHardware(state, data){
            var send_obj = {};
            send_obj["id"] = data.id;
            send_obj[data.value_endpoint_type] = data.value;
            axios.post('http://localhost:8000/edit_hardware', send_obj);
        },
        RemoveHardware(state, hardware){
            state.modal_popup_active = 'Are you sure?';
            state.modal_popup_agree = () => {
                state.hardware.find(e => e.id === hardware.id)['active'] = 0
                this.commit('EditHardware', {id:hardware.id, value_endpoint_type: 'active', value:0});
            }
            state.modal_popup_deny = () => {
                state.modal_popup_active = null;
            }
        },
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

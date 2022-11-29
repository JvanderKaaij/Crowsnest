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

function ToFormData(data){
    var form_data = new FormData();
    for ( var key in data ) {
        if(data[key] != null){
            form_data.append(key, data[key]);
        }
    }
    return form_data;
}

function ParseDate(date){
     const temp = new Date(date);
     return temp.toJSON().split('T')[0]
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
            data.forEach(x=>{
                x.start_date = ParseDate(x.start_date);
                x.estimated_end_date = ParseDate(x.estimated_end_date);
            })
            state.students = data;
        },
        AddStudent(state, data){
            var form_data = ToFormData(data.data);
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
        EditStudent(state, data){
            data.data.start_date = ParseDate(data.data.start_date);
            data.data.estimated_end_date = ParseDate(data.data.estimated_end_date);
            var form_data = ToFormData(data.data);
            axios.post('http://localhost:8000/edit_student', form_data).then(response => {
                if(response.data.success){
                    data.success();
                }else{
                    data.onError(response.data.errors);
                }
            });
        },
        RemoveStudent(state, student){
            state.modal_popup_active = 'Are you sure?';

            //student is selected in hardware
            if(state.hardware.find(x => x.student_id === student.id)){
                state.modal_popup_active = 'Are you sure? This student has hardware assigned!';
            }

            state.modal_popup_agree = () => {
                var stud = state.students.find(e => e.id === student.id);
                stud['active'] = 0;
                this.commit('EditStudent', {data:stud});
                state.modal_popup_active = null;
            }
            state.modal_popup_deny = () => {
                state.modal_popup_active = null;
            }
        },
        InitHardware(state, data){
            data.forEach(x=>{
                x.purchase_date = ParseDate(x.purchase_date);
            })
            state.hardware = data;
        },
        AddHardware(state, data){
            var form_data = ToFormData(data.data);
            axios
            .post('http://localhost:8000/add_hardware', form_data, {
                headers: {
                  'Content-Type': 'multipart/form-data'
                }
              })
            .then(response => {
                if(response.data.success){
                    state.hardware.push(data.data);
                    data.success();
                }else{
                    data.onError(response.data.errors);
                }
            });
        },
        EditHardware(state, data){
            data.data.purchase_date = ParseDate(data.data.purchase_date);
            var form_data = ToFormData(data.data);
            axios.post('http://localhost:8000/edit_hardware', form_data).then(response => {
                if(response.data.success){
                    data.success();
                }else{
                    data.onError(response.data.errors);
                }
            });
        },
        RemoveHardware(state, hardware){
            state.modal_popup_active = 'Are you sure?';
            state.modal_popup_agree = () => {
                var hard = state.hardware.find(e => e.id === hardware.id);
                hard['active'] = 0;
                this.commit('EditHardware', {data:hard});
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
                console.log(response);
                context.commit('InitStudents', response.data);
            }).catch(error =>{
                if(error.response.status === 401){
                    router.push('/login');
                }
            });
        },
        async InitHardware(context){
            axios
            .get('http://localhost:8000/hardware')
            .then(response => {
                context.commit('InitHardware', response.data);
            }).catch(error =>{
                if(error.response.status === 401){
                    router.push('/login');
                }
            });
        }
    },
    getters:{
        //can be used as a return state with extra functionality
    }
});

axios.defaults.withCredentials = true;
createApp(App).use(router).use(store).mount('#app');

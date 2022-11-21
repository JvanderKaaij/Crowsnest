import Vue from "vue/dist/vue";
import App from "./App.vue";

Vue.config.productionTip = false;

var instance = new Vue({
    el: '#app',
    components: {App},
    template: '<App/>'
});
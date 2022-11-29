<template>
    <div id="home-page">
      <Hardware></Hardware>
      <Students></Students>

      <div v-if="modal_popup_active" class="popup">{{ modal_popup_active }}
        <button @click="modal_popup_agree()">Yes</button>
        <button @click="modal_popup_deny()">No</button>

      </div>

    </div>
</template>

<script>
    import Hardware from "./components/Hardware.vue";
    import Students from "./components/Students.vue";
    import {mapActions, mapState} from "vuex"
    export default {
        name: 'Home',
        components: {Hardware, Students},
        computed:{
          ...mapState(['modal_popup_active','modal_popup_agree','modal_popup_deny'])
        },
        methods:{
          ...mapActions(["InitStudents", "InitHardware"]),
        },
        mounted() {

          if(!localStorage.logged_in){
            this.$router.push('/login');
          }

          this.$store.dispatch('InitStudents')
          this.$store.dispatch('InitHardware')
        }
    }
</script>
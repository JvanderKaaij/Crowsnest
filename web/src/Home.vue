<template>
    <div id="home-page">
      <Hardware></Hardware>
      <Students></Students>
      <div class="modal-container">
        <div  class="popup">{{ modal_popup_active }}
          <button @click="modal_popup_agree()">Yes</button>
          <button @click="modal_popup_deny()">No</button>
        </div>
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

<style scoped>
  .modal-container{
    position:absolute;
    width: 100%;
    height: 100%;
    top: 0;
    background-color: rgba(22,22,22,0.5); /* complimenting your modal colors */
  }

  .popup{
    position: relative;
    display:inline-block;
    margin: 0 auto;
    top: 25%;
  }


</style>
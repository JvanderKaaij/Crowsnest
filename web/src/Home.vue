<template>
    <div id="home-page">
      <div class="home-page-container">
        <div class="header">
          <span class="logo">Crowsnest</span>
          <button @click="doLogout()">Logout</button>
        </div>
        <div class="content">
          <Hardware></Hardware>
          <Students></Students>
        </div>
        <div v-if=modal_popup_active class="modal-container">
          <div class="modal">
            <div class="header-text">Alert!</div>
            <div class="modal-text">{{ modal_popup_active }}</div>
            <div class="button-container">
              <button @click="modal_popup_agree()">Yes</button>
              <span class="spacer"> </span>
              <button @click="modal_popup_deny()">No</button>
            </div>
          </div>
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
          doLogout(){
            this.$store.commit('Logout');
          }
        },
        mounted() {
          this.$store.dispatch('InitStudents')
          this.$store.dispatch('InitHardware')
        }
    }
</script>

<style scoped>
  #home-page{
    display: flex;
    justify-content: center;
  }

  .modal-container{
    position:absolute;
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100%;
    left: 0;
    right: 0;
    top: 0;
    background-color: rgba(22,22,22,0.5); /* complimenting your modal colors */
  }

  .modal{
    border-radius: 5px;
    min-width:300px;
    min-height:120px;
    background-color: var(--blue-yonder);
    position: relative;
    display:inline-block;
    margin: 0 auto;
  }

  .modal-text{
    margin-top:10px;
    font-size:12pt;
    text-align: center;
    padding:10px;
    color: var(--ghost-white);
  }

  .button-container{
    margin-top:20px;
    padding:10px;
    text-align: center;
  }

  .header{
    display: flex;
    justify-content: flex-end;
    padding: 10px;
    margin-bottom: 50px;
    align-items: center;
    background-color: var(--blue-yonder);
    height:60px;
  }

  .logo{
    margin-right: auto;
    font-size: 25px;
    color: var(--ghost-white);
  }

  .header-text{
    border-top-left-radius: 5px;
    border-top-right-radius: 5px;
    background-color: var(--orange-red-crayola);
    color: var(--ghost-white);
    text-align: center;
    font-size:19px;
    padding:10px;
  }

  .button-container .spacer{
    width: 10px;
    display: inline-block;
  }

  .button-container button{
    min-width:120px;
    padding:10px;
  }


</style>
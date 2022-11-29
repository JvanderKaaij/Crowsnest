<template>
    <div id="home-page">
      <Hardware></Hardware>
      <Students></Students>
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
          this.$store.dispatch('InitStudents')
          this.$store.dispatch('InitHardware')
        }
    }
</script>

<style scoped>
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
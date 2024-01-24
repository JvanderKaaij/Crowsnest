<template>
  <div class="modal-container" v-if=modal_popup_active>
    <div class="modal">
      <div class="modal-header-text">Alert!</div>
      <div class="modal-text">{{ modal_popup_active }}</div>
      <div class="button-container">
        <button @click="modal_popup_agree()">Yes</button>
        <span class="spacer"> </span>
        <button @click="modal_popup_deny()">No</button>
      </div>
    </div>
  </div>
</template>

<script>
import {mapState} from "vuex";
export default {
  name: "Modal",
  computed:{
    ...mapState(['modal_popup_active','modal_popup_agree','modal_popup_deny'])
  }
}
</script>

<style scoped>
  .modal-container{
    position: fixed;
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
    font-size:1em;
    text-align: center;
    padding:10px;
    color: var(--ghost-white);
  }

  .modal-header-text{
    border-top-left-radius: 5px;
    border-top-right-radius: 5px;
    background-color: var(--orange-red-crayola);
    color: var(--ghost-white);
    text-align: center;
    font-size:19px;
    padding:10px;
  }

  .button-container{
    margin-top:20px;
    padding:10px;
    text-align: center;
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
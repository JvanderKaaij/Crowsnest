<template>
    <div id="home-page">
      <div class="home-page-container">
        <div class="header">
          <Header/>
        </div>
        <div class="content">
          <Hardware/>
          <Students/>
        </div>
      </div>
      <Modal/>
    </div>
</template>

<script>
    import Hardware from "./components/Hardware.vue";
    import Students from "./components/Students.vue";
    import Header from "./components/Header.vue";
    import Modal from "./components/Modal.vue";
    import {mapActions, mapState} from "vuex"
    export default {
        name: 'Home',
        components: {Hardware, Students, Header, Modal},
        methods:{
          ...mapActions(["InitStudents", "InitHardware"]),

        },
        mounted() {
          this.$store.dispatch('InitStudents');
          this.$store.dispatch('InitHardware');
        }
    }
</script>

<style scoped>
  #home-page{
    display: flex;
    justify-content: center;
  }
</style>
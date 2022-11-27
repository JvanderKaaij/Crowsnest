<template>
    <div id="home-page">
      <Hardware></Hardware>
      <Students></Students>
    </div>
</template>

<script>
    import Hardware from "./components/Hardware.vue";
    import Students from "./components/Students.vue";
    import {mapActions } from "vuex"
    export default {
        name: 'Home',
        components: {Hardware, Students},
        methods:{
          ...mapActions(["InitStudents", "InitHardware"])
        },
        mounted() {
          this.$store.dispatch('InitStudents')
          this.$store.dispatch('InitHardware')
        }
    }
</script>
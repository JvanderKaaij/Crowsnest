<template>
  <div id="settings-page">
      <div class="settings-page-container">
        <div class="header">
          <Header/>
        </div>
        <div class="content">
        </div>
      </div>
    </div>
</template>

<script>
import Header from "./components/Header.vue";
export default {
  name: "Settings",
  components: {Header},
  data () {
    return {

    }
  },
  methods: {

  }
}

</script>

<style scoped>
  #settings-page{
    display: flex;
    justify-content: center;
  }
</style>
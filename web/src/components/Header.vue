<template>
  <div class="header-container">
    <span class="logo">Crowsnest</span>
    <button @click="goToHome()">Home</button>
    <button @click="goToSettings()">Settings</button>
    <button @click="doLogout()">Logout</button>
  </div>
</template>

<script>
export default {
  name: "Header",
  methods:{
    doLogout(){
      this.$store.commit('Logout');
    },
    goToHome() {
      this.$router.push('/app');
    },
    goToSettings() {
      this.$router.push('/settings');
    }
  }
}
</script>

<style scoped>
  .header-container{
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
</style>
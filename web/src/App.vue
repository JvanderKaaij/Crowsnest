<template>
  <div id="main-container">
      <router-view></router-view>
  </div>
</template>

<script setup>

</script>

<style>

:root {
  --black-coral: #495867ff;
  --blue-yonder: #577399ff;
  --beau-blue: #bdd5eaff;
  --ghost-white: #f9ffff;
  --orange-red-crayola: #fe5f55ff;
}

body{
  background-color: var(--ghost-white);
  font-family: Verdana, sans-serif;
  color: var(--black-coral);
}

.component-header{
  margin-top:10px;
  margin-bottom: 10px;
}

table{
  min-width: 70rem;
  border-collapse: collapse;
}

.t-header{
  color:var(--ghost-white);
}

tr{
  background-color: var(--beau-blue);
}

td.new{
  background-color: var(--blue-yonder);
}

td{
  margin:0;
  padding: 10px;
}

.val-input{
  border-radius: 5px;
  padding: 13px 15px;
  border: 1px solid;
}

.error{
    color:white;
    max-width:150px;
    font-size:9pt;
    margin-top:2px;
    padding:2px;
    background-color: var(--orange-red-crayola);
  }

</style>
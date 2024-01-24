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
  --fargo-blue: #d8eff5;
  --ghost-white: #f9ffff;
  --orange-red-crayola: #fe5f55ff;
  --md-green: #93fe55;
}

body{
  margin:0;
  background-color: var(--ghost-white);
  font-family: Verdana, sans-serif;
  color: var(--black-coral);
}

.component-header{
  font-size:24px;
  margin-top:10px;
  margin-bottom: 10px;
}

table{
  min-width: 70rem;
  border-collapse: collapse;
}

.t-header{
  color:var(--ghost-white);
  background-color: var(--blue-yonder);
}

tr{
  vertical-align: top;
  background-color: var(--beau-blue);
}

td.new{
  background-color: var(--fargo-blue);
}

td{
  margin:0;
  padding: 10px;
}

select{
  border-radius: 5px;
  box-sizing: border-box;
  min-width:110px;
  height: 48px;
  font-size: 15px;
  padding-left: 10px;
  border: 1px solid;
}

.val-input{
  border-radius: 5px;
  box-sizing: border-box;
  padding-left: 10px;
  width: 100%;
  height: 48px;
  font-size: 15px;
  border: 1px solid;
}

.checkbox-input{
  width:20px;
  height:20px;
}

.error{
    color:white;
    min-height: 24px;
    width: 100%;
    max-width:180px;
    border-radius: 5px;
    box-sizing: border-box;
    font-size:9pt;
    margin-top:2px;
    padding:4px;
    background-color: var(--orange-red-crayola);
}

.align-center{
  display: flex;
  justify-content: center;
}

button{
    min-width:120px;
    padding:10px;
  }


</style>
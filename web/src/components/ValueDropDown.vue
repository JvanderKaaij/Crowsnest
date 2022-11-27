<template>
  <select v-model="my_value" @change="signalChange">
    <option v-for="(item, index) in students" :value=item.id>{{item.name}}</option>
  </select>
</template>

<script>
    import {mapState} from "vuex";
    export default {
      name: 'ValueDropDown',
      components: {},
      computed: {
        ...mapState(['students'])
      }
    }
</script>

<style scoped>

</style>
<template>
  <select v-model="selected" @change="signalChange">
    <option v-for="(item, index) in map" :value=item.id>{{item.name}}</option>
  </select>
</template>

<script>
    import {mapState} from "vuex";
    export default {
      name: 'ValueDropDown',
      components: {},
      props:['map', 'url', 'value_endpoint_type', 'value'],
      data () {
        console.log(this.value);
        return {
          selected: this.value
        }
      },
      mounted(){
        this.computed = {...mapState([this.map])}; //take this out of computed to dynamically map this.map
      }
    }
</script>

<style scoped>

</style>
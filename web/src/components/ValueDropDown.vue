<template>
  <select v-model="selected" @change="signalChange">
    <option v-for="(item, index) in GetActive" :value=item.id>{{item.name}}</option>
  </select>
</template>

<script>
    import {mapState} from "vuex";
    export default {
      name: 'ValueDropDown',
      components: {},
      props:['id', 'map', 'mutation', 'value_endpoint_type', 'value'],
      data () {
        return {
          selected: this.value
        }
      },
      computed: {
        GetActive() {
          return this.map.filter(x => x['active']);
        }
      },
      methods:{
          signalChange: function(evt){
            this.$store.commit(this.mutation, {id:this.id, value_endpoint_type:this.value_endpoint_type, value:this.selected});
          }
      },
      mounted(){
        this.computed = {...mapState([this.map])}; //take this out of computed to dynamically map this.map
      }
    }
</script>

<style scoped>

</style>
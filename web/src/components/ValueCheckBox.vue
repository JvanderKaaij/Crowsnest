<template>
  <input type="checkbox" id="checkbox" v-model="my_value" v-on:change="signalChange"/>
</template>

<script>
    export default {
      name: 'ValueCheckBox',
      components: {},
      props: ['value', 'value_endpoint_type', 'mutation', 'id'],
      methods:{
        signalChange(evt){
          this.$store.commit(this.mutation, {id:this.id, value_endpoint_type:this.value_endpoint_type, value:this.my_value});
        }
      },
      data () {
        return {
          my_value: null
        }
      },
      mounted(){
        this.my_value = this.value === 1; //I need to set the prop to the data, as props are immutable. Also need to check against an integer
      }
    }
</script>

<style scoped>

</style>
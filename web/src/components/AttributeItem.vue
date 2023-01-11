<template>
  <input v-if="item.type.element_type == 'int'" v-model="item.content" v-on:change="signalChange">
  <input v-if="item.type.element_type == 'string'" v-model="item.content" v-on:change="signalChange">
  <input type="checkbox" v-if="item.type.element_type == 'bool'" v-model="checked">
</template>

<script>
    export default {
      name: 'AttributeItem',
      props:['item'],
      components: {},
      data() {
        return {
          checked: false,
        }
      },
      methods:{
        signalChange: function(evt){
            this.$store.commit('EditAttribute', {data:this.item, success:this.OnSuccess, onError:this.OnErrors});
        },
        OnSuccess(){
          console.log("Success");
        },
        OnErrors(errors) {
          console.log("Error");
        }
      },
      created() {
        if(this.item.type.element_type == 'bool'){
          this.checked = this.item.content == 1;
        }
      }
    }
</script>

<style scoped>

</style>
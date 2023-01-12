<template>
  <input v-if="type.element_type == 'int'" v-model="content" v-on:change="signalChange">
  <input v-if="type.element_type == 'string'" v-model="content" v-on:change="signalChange">
  <input type="checkbox" v-if="type.element_type == 'bool'" v-model="checked" v-on:change="signalChange">
</template>

<script>
    export default {
      name: 'AttributeItem',
      props:['type', 'attribute'],
      components: {},
      data() {
        return {
          checked: false,
          content: ""
        }
      },
      methods:{
        signalChange: function(evt){
          if(this.type.element_type == 'bool'){
            this.content = this.checked ? 1 : 0;
          }

          this.attribute.content = this.content;
          this.$store.commit('EditAttribute', {data:this.attribute, success:this.OnSuccess, onError:this.OnErrors});

        },
        OnSuccess(response){
          console.log(response);
        },
        OnErrors(errors) {
          console.log("Error");
        }
      },
      created() {
        if(this.attribute){
          this.content = this.attribute.content;
          this.checked = this.content == 1 ? true : false;
        }

      }
    }
</script>

<style scoped>

</style>
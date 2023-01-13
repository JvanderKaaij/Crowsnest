<template>
  <input v-if="type.element_type == 'int'" v-model="content" v-on:change="signalChange">
  <input v-if="type.element_type == 'string'" v-model="content" v-on:change="signalChange">
  <input type="checkbox" v-if="type.element_type == 'bool'" v-model="checked" v-on:change="signalChange">
</template>

<script>
    export default {
      name: 'AttributeItem',
      props:['type', 'attribute', 'student'],
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

          if(this.attribute){
            this.attribute.content = this.content;
            this.$store.commit('EditAttribute', {data:this.attribute, success:this.OnSuccess, onError:this.OnErrors});
          }else{
            //attribute didn't exist yet - we need to make it
            console.log("attribute needs to be created");
            this.$store.commit('AddAttribute', {data:{student_id:this.student.id, content:this.content, attribute_type_id:this.type.id}, success:this.OnSuccess, onError:this.OnErrors});
          }

          console.log(this.student);

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
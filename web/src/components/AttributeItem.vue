<template>
  <input class="val-input" v-if="type.element_type === 'int'" v-model="content" v-on:change="signalChange">
  <input class="val-input" v-if="type.element_type === 'string'" v-model="content" v-on:change="signalChange">
  <input class="checkbox-input" type="checkbox" v-if="type.element_type === 'bool'" v-model="checked" v-on:change="signalChange">
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
          if(this.type.element_type === 'bool'){
            this.content = this.checked ? 1 : 0;
          }

          if(this.attribute){
            this.attribute.content = this.content;
            this.$store.commit('EditAttribute', {data:this.attribute, success:this.OnSuccess, onError:this.OnErrors});
          }else{
            this.CreateAttribute(this.student.id);
          }
        },
        CreateAttribute(){
          this.$store.commit('AddAttribute', {data:{student_id:this.student.id, content:this.content, attribute_type_id:this.type.id}, success:this.OnSuccess, onError:this.OnErrors});
        },
        OnSuccess(response){

        },
        OnErrors(errors) {
          console.log("Error");
        },
        Reset(){
          this.content = "";
          this.checked = 0;
        }
      },
      created() {
        if(this.attribute){
          this.content = this.attribute.content;
          this.checked = this.content === "1";
        }

      }
    }
</script>

<style scoped>

</style>
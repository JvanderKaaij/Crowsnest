<template>
  <input v-if="item.type.element_type == 'int'" :value="item.content">
  <input v-if="item.type.element_type == 'string'" :value="item.content">
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
      created() {
        if(this.item.type.element_type == 'bool'){
          this.checked = this.item.content == 1;
        }
      }
    }
</script>

<style scoped>

</style>
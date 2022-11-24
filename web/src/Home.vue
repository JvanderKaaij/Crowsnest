<template>
    <div id="home-page">
      <div class="header">Home</div>
      <Hardware></Hardware>
      <Students></Students>
    </div>
</template>

<script>
    import Hardware from "./components/Hardware.vue";
    import Students from "./components/Students.vue";
    export default {
        name: 'Home',
        components: {Hardware, Students}
    }
</script>
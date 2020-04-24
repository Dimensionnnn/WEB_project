<template>
    <div class="pk_bg">
      <div class="avatar-box-me">

      </div>
    </div>
</template>

<script>
    export default {
        name: "compete_pk",
        data(){
          return {

          }
        },
        mounted() {
          $(".pk_bg").css('min-height', (window.innerHeight+100-62).toString()+'px')
        }
    }
</script>

<style scoped>
  .pk_bg{
    width: 100%;
    background: #eee;
  }
</style>

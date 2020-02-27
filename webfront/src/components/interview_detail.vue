<template>
    <div>
      {{this.$route.params.idname}}
    </div>
</template>

<script>
    export default {
        name: "interview_detail",
        data(){
          return{

          }
        },
      mounted(){
          console.log(this.$route.params.type)
      },
      created() {
      }
    }
</script>

<style scoped>

</style>

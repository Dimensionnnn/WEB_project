<template>
    <div style="background: rgb(207, 216, 221); min-width: 1400px">
      <div class="header">
        <div class="header-title">
          <h1>Cloud党建综合测验平台</h1>
        </div>
      </div>
      <transition name="el-fade-in-linear">
        <exam @child-event="ParentEvent" v-show="contextShow"></exam>
      </transition>
      <transition name="el-fade-in">
        <exam_detail :parentmsg="examId" v-show="examShow"></exam_detail>
      </transition>
    </div>
</template>

<script>
    import exam from '@/components/exam.vue'
    import exam_detail from '@/components/exam_detail.vue'
    export default {
        name: "exam_header",
        components: {
          exam,
          exam_detail
        },
      data(){
          return {
            examId: '',
            contextShow: true,
            examShow:false
          }
      },
      methods:{
          ParentEvent:function (data){
            this.examId = data
            this.contextShow = false
            this.examShow = true
          }
      }
    }
</script>

<style scoped>
  .header{
    min-width: 1400px;
    height: 300px;
    background-image: url("/static/picture/exam_bg.jpg");
    background-size: 100% 100%;
    background-repeat: no-repeat;
    background-position: center center;
  }
  .header-title{
    padding-top: 90px;
    position: relative;
    overflow: hidden;
    height: 150px;
    text-align: center;
  }
  .header-title h1{
    font-size: 50px;
    color: #fff;
  }
</style>

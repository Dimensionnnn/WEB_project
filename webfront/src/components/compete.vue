<template>
    <div class="bg">
      <div class="main-content">
        <el-row>
          <el-col :span="4">
            <el-menu background-color="#304156" text-color="#bfcbd9"
                     default-active="1" class="el-menu-vertical-demo mymenu"  @select="handleClick">
              <el-menu-item index="1">
                <i class="el-icon-user-solid"></i>
                <span slot="title">个人战绩</span>
              </el-menu-item>
              <el-menu-item index="2">
                <i class="el-icon-s-promotion"></i>
                <span slot="title">在线比武</span>
              </el-menu-item>
            </el-menu>
          </el-col>
          <el-col :span="20">
            <div class="header">
              <div class="logo-box">
                <div class="avatar-box">
                  <img src="/static/picture/avatar.png" class="avatar">
                </div>
              </div>
              <div class="nickname">雪山向日葵2333</div>
            </div>
            <transition name="el-fade-in-linear">
              <compete_personal v-show="personal_show"></compete_personal>
            </transition>
            <transition name="el-fade-in-linear">
              <compete_pk v-show="pk_show"></compete_pk>
            </transition>
          </el-col>
        </el-row>
      </div>
    </div>
</template>

<script>
    import compete_personal from '@/components/compete_personal'
    import compete_pk from '@/components/compete_pk'
    export default {
        name: "compete",
        components:{
          compete_personal,
          compete_pk
        },
        data(){
          return{
            personal_show: true,
            pk_show: false
          }
        },
        methods:{
          handleClick:function (key, keypath) {
            if (key === '1'){
              this.personal_show = true;
              this.pk_show = false;
            }
            if (key === '2'){
              this.personal_show = false;
              this.pk_show = true;
              $(".pk_bg").css('min-height', (window.innerHeight+100-62).toString()+'px');
              const loading = this.$loading({
                lock: true,
                text: '正在匹配对手',
                spinner: 'el-icon-loading',
                background: 'rgba(0, 0, 0, 0.7)'
              });
              setTimeout(function () {
                loading.close();
              },3000)
            }
          }
        },
        mounted() {
          $(".mymenu").css('min-height',(window.innerHeight+100).toString()+'px')
        }
    }
</script>

<style scoped>
  .nickname{
    font-size: 15px;
    color: #a6a9ad;
    font-weight: bold;
    float: left;
    margin-top: 20px;
  }
  .bg{
    min-width: 1400px;
    height: 100%;
    background: #f7f7f7;
  }
  .main-content{
    width: 100%;
    height: 100%;
    background: #fff;
  }
  .mymenu{

  }
  .logo-box{
    width: 100px;
    height: 100%;
    float: left;
  }
  .avatar-box{
    width: 50px;
    height: 50px;
    float: left;
    margin-left: 25px;
    margin-top: 5px;
  }
  .avatar{
    width: 100%;
    height: 100%;
  }
  .header{
    width: 100%;
    height: 60px;
    border-bottom: 2px solid #ddd;
  }
</style>

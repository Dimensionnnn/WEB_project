<template>
    <div class="bg">
      <div class="header-banner">
        <div class="title-box">
          <div class="title">
            <span>360°全景遨游红色景点</span>
          </div>
        </div>
      </div>
      <div class="main-content">
        <div class="card-box">
          <el-scrollbar style="height: 550px">
            <div v-for="(item,index) in card_list" :key="index">
            <el-card class="box-card" @click.native="Transfer(index)">
              <div class="card-container">
                <el-row>
                  <el-col :span="9">
                    <div class="card-logo">
                      <img :src="item.url">
                    </div>
                  </el-col>
                  <el-col :span="15">
                     <div class="logo-title">
                        <span>{{item.title}}</span>
                     </div>
                     <div class="logo-content">
                       <span>{{item.content}}</span>
                     </div>
                  </el-col>
                </el-row>
              </div>
            </el-card>
          </div>
          </el-scrollbar>
        </div>
      </div>
    </div>
</template>

<script>
    export default {
        name: "red_scenery",
        data(){
          return{
            search_content:'',
            card_list:[]
          }
        },
        methods:{
          getData: function(){
              let that = this;
              this.$axios({
                  method:'post',
                  url:'api/get_red_scene',
                }).then(function (res) {
                  let data = res.data.data;
                  for (let i=0; i<data.length; i++){
                    let dict = {};
                    dict['title'] = data[i][0];
                    dict['content'] = data[i][1];
                    dict['url'] = data[i][2];
                    that.card_list.push(dict)
                  }
              })
          },
          Transfer:function (index) {
            if (index === 0){
              window.location.href='http://47.111.227.79:3000'
            }
            if (index === 1){
              window.location.href='http://47.111.227.79:4000'
            }
          },
          Search:function () {
            let that = this;
            if (that.search_content === ''){
              that.$message({
                message:'输入内容不能为空',
                type:'error'
              })
            }
            else{
              this.card_list = [];
              that.getData();
            }
          }
        },
        watch:{
          '$route': 'FetchData'
        },
        created() {
          let params = this.$route.query.content;
          this.getData();
        }
    }
</script>

<style scoped>
  .bg{
    min-width: 1400px;
    height: 100%;
    background: #fffedc
  }
  .header-banner{
    min-width: 1400px;
    height: 300px;
    background-image: url("/static/picture/scene_banner.jpg");
    background-position: center center;
    background-repeat: no-repeat;
    background-size: 100% 100%;
  }
  .title-box{
    width: 1200px;
    margin: 0 auto;
    padding: 110px 20px;
  }
  .title{
    text-align: center;
    width: 100%;
    height: 100%;
  }
  .title span{
    font-size: 50px;
    font-weight: bold;
    letter-spacing: 15px;
    color: #8a2be2;
  }
  .main-content{
    width: 1200px;
    margin: 0 auto;
  }
  .box-card{
    margin-top: 20px;
    margin-bottom: 40px;
    cursor: pointer;
    transform: scaleX(1);
    transition-timing-function: cubic-bezier(0.52, 1.64, 0.37, 0.66);
  }
  .box-card:hover{
    background: #ffcc00;
  }
  .card-box{
    width: 1000px;
    margin: 0 auto;
  }
  .card-container{
    width: 100%;
    height: 200px;
    padding-bottom: 15px;
  }
  .card-logo{
    height: 210px;
    border-right: 1px solid rgba(0, 0, 0, 0.1);
    margin-right: 46px;
    padding-right: 30px;
  }
  .card-logo img{
    width: 100%;
    height: 100%;
  }
  .logo-title{
    width: 100%;
  }
  .logo-title span{
    font-size: 25px;
    letter-spacing: 5px;
    color: #fb1d04;
    font-weight: bold;
  }
  .logo-content{
    width: 100%;
    padding-top: 20px;
    padding-bottom: 10px;
  }
  .search{
    text-align: center;
  }
  .search-input{
    margin-top: 30px;
    position: relative;
    height: 52px;
    border-radius: 6px;
    display: inline-block;
    max-width: 834px;
  }
  .search-box{
    height: 100%;
    width: 834px;
  }
  .search-box input{
    font-size: 18px;
    display: block;
    box-sizing: border-box;
    width: 100%;
    height: 100%;
    padding: 0 20px;
    letter-spacing: 1px;
    border-top-left-radius: 4px;
    border-bottom-left-radius: 4px;
  }
  .search_button{
    width: 90px;
    margin-left: 10px;
    color: #fff;
    height: 52px;
    line-height: 52px;
    background-color: #FF5859;
    display: inline-block;
    border-top-right-radius: 4px;
    border-bottom-right-radius: 4px;
  }
</style>

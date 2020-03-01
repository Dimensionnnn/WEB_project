<template>
    <div style="background: #FAFAD2;">
      <div class="header">
        <div class="header-info">
          <h1>{{title}}----{{name}}</h1>
          <p>{{content}}</p>
        </div>
        <div class="picture">
          <img :src="src">
        </div>
      </div>
      <div class="main-content">
        <div v-html="text">{{text}}</div>
      </div>
    </div>
</template>

<script>
    export default {
        name: "Interview_Detail",
        data(){
          return{
            name:'',
            content:'',
            title:'',
            src:'',
            text:''
          }
        },
      mounted(){
          let that = this;
          let result = this.$route.query;
          let content = {};
          content['type'] = parseInt(result.type);
          content['index'] = parseInt(result.index);
          this.$axios({
            method:'post',
            url:'api/goodthing/detail',
            data:content
          }).then(function (res) {
            let content = res.data.data[0];
            that.src = content[0];
            that.name = content[1];
            that.title = content[2];
            that.content = content[3];
            that.text = content[5];
            $(".picture").css('background-color', 'url("'+that.src+'");')
          })
      },
      created() {
      }
    }
</script>

<style scoped>
  .header{
    background-image: url("/static/picture/model_detail_bg.jpg");
    background-size: 100% 100%;
    background-position: center center;
    background-repeat: no-repeat;
    min-width: 1400px;
    width: 100%;
    height: 300px;
  }
  .header-info{
    padding-top: 50px;
    padding-left: 85px;
    float: none;
    color: #fff;
  }
  .header-info h1{
    font-weight: bold;
    font-size: 38px;
    line-height: 48px;
    width: 895px;
    margin: 0;
    padding: 42px 0 20px 0;
  }
  .header-info p{
    font-size: 22px;
    color: #FFF;
    line-height: 26px;
    width: 895px;
    margin: 0 auto;
  }
  .picture{
    width: 200px;
    height: 250px;
    position: absolute;
    top: 27px;
    right: 57px;
  }
  .picture img{
    width: 100%;
    height: 100%;
  }
  .main-content{
    padding: 20px;
    width: 1200px;
    margin-left: auto;
    margin-right: auto;
    margin-top: 90px;
    margin-bottom: 50px;
    min-height: 400px;
    background-color: #fff;
    box-shadow: 0 0 10px 5px #cdcdcd;
  }
</style>


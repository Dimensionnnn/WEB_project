<template>
    <div class="container">
      <div class="main-body">
        <div class="title">
          <span>{{title}}</span>
          <div class="line">
            <img src="/static/picture/line.png">
          </div>
        </div>
        <div class="container_button">
          <img @click="Redirect" src="/static/picture/login.png">
        </div>
      </div>
      <div class="huabiao">
        <img src="/static/picture/huabiao.png">
      </div>
      <div class="footer">
        <img src="/static/picture/foot.png">
      </div>
      <div class="bird">
        <img src="/static/picture/bird.png">
      </div>
    </div>
</template>

<script>
    export default {
        name: "MainPage",
        data(){
          return {
            title: "“Cloud党建”学习驿站"
          }
        },
      methods:{
          Redirect:function () {
            this.$router.push('/home')
          }
      },
      mounted() {
      }
    }
</script>

<style scoped>
  .main-body{
    position: relative;
    width: 90%;
    height: 100%;
    margin: auto;
  }
  .bird{
    position: absolute;
    width: 20%;
    height: 30%;
    top: 0;
    right: 0;
  }
  .bird img{
    width: 100%;
    height: 100%;
  }
  .title{
    width: 80%;
    padding: 10px 20px;
    position: absolute;
    top: 35%;
    left: 50%;
    transform: translate(-50%,-50%);
    text-align: center;
    opacity: 0;
    animation: title_bounce 1s forwards;
    animation-delay: .5s;
  }
  .title span{
    font-size: 40px;
    font-weight: bold;
    color: #ce0000;
    letter-spacing: 20px;
  }
  .container_button{
    position: absolute;
    top: 60%;
    left: 50%;
    transform: translate(-50%,-50%);
    margin: 10px auto;
    text-align: center;
    z-index: 10;
    opacity: 0;
    -webkit-animation-name:button_animate, button_bounce;
    -webkit-animation-duration:1s, 1.5s;
    -webkit-animation-timing-function:ease-out, linear;
    -webkit-animation-delay:2s, 5s;
    -webkit-animation-iteration-count:1, infinite;
    -webkit-animation-fill-mode:forwards, none;
    transition: all 0.5s;
  }
  .container_button img{
    width: 60%;
  }
  .container_button img:hover{
    width: 65%;
    transition:  all .5s;
  }
  .container_button img:hover .container_button{
    animation-play-state: paused;
  }
  .footer{
    position: absolute;
    opacity: 0;
    bottom: 0;
    z-index: 1;
    animation: img_shade 2s forwards;
    animation-delay: 1s;
  }
  .footer img{
    width: 100%;
  }
  .line{
    position: relative;
    padding-top: 40px;
    padding-bottom: 20px;
  }
  .line img{
    width: 75%;
  }
  .huabiao{
    width: 24%;
    height: 90%;
    position: absolute;
    opacity: 0;
    bottom: 0;
    z-index: 2;
    animation: huabiao_animate 1s forwards;
    animation-delay: 1.5s;
  }
  .huabiao img{
    width: 100%;
    height: 100%;
  }
  .container{
    position: relative;
    width: 100%;
    height: 100%;
    background: url('/static/picture/bg_main.jpg') no-repeat;
    background-size: cover;
  }
  @keyframes button_bounce {
    0%{top: 60%}
    25%{top: 58%}
    50%{top: 60%}
    75%{top: 58%}
    100%{top: 60%}
  }
  @-webkit-keyframes button_bounce {
    0%{top: 60%}
    25%{top: 58%}
    50%{top: 60%}
    75%{top: 58%}
    100%{top: 60%}
  }
  @keyframes button_animate {
    0%{opacity: 0;top: 80%;}
    100%{opacity: 1;top: 60%}
  }
  @-webkit-keyframes button_animate {
    0%{opacity: 0;top: 80%;}
    100%{opacity: 1;top: 60%}
  }
  @keyframes line_shadow {
    0%{opacity: 0}
    100%{opacity: 1}
  }
  @-webkit-keyframes line_shadow {
    0%{opacity: 0}
    100%{opacity: 1}
  }

  @keyframes title_bounce {
    0%{top:0; left:50%; opacity: 0}
    100%{top:35%; left:50%; opacity: 1}
  }
  @-webkit-keyframes title_bounce {
    0%{top:0; left:50%; opacity: 0}
    100%{top:35%; left:50%; opacity: 1}
  }
  
  @keyframes huabiao_animate {
    0%{bottom: 50%; opacity: 0}
    100%{bottom: 0; opacity: 1}
  }
  @-webkit-keyframes huabiao_animate {
    0%{bottom: 50%; opacity: 0}
    100%{bottom: 0; opacity: 1}
  }
  @-moz-keyframes huabiao_animate {
    0%{bottom: 50%; opacity: 0}
    100%{bottom: 0; opacity: 1}
  }
  @keyframes img_shade {
    0%{opacity: 0}
    100%{opacity: 1}
  }
  @-moz-keyframes img_shade {
    0%{opacity: 0}
    100%{opacity: 1}
  }
  @-webkit-keyframes img_shade {
    0%{opacity: 0}
    100%{opacity: 1}
  }
</style>

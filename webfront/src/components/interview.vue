<template>
  <div class="main-bg">
    <div class="back-btn" v-if="page_index !== length">
      <img src="/static/picture/back.png" @click="handleBack">
    </div>
    <div class="go-btn" v-if="page_index !== 1">
      <img src="/static/picture/go.png" @click="handleGo">
    </div>
    <div class="book preserve-3d">
      <div v-for="(item, index) in model_people" :key="index">
        <div class="book-page-box preserve-3d"
             :class="[page_index<=index?'flip-animation-1':'', finish_page.indexOf(index)>-1?'flip-animation-2':'']">
          <div class="book-page page-front">
            <el-scrollbar style="height: 100%">
              <div class="detail-header">
                <div class="detail-text">
                  <div class="detail-text-name">
                    <div class="detail-text-name1">{{item.name}}</div>
                  </div>
                  <div class="detail-text-content">
                    <div class="detail-text-content1">{{item.content}}</div>
                  </div>
                </div>
                <div class="img-box">
                  <img :src="item.url">
                </div>
              </div>
              <p v-html="item.detail"></p>
            </el-scrollbar>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
    export default {
        name: "interview",
        data(){
          return{
            page_index: null,
            length: null,
            model_people:[],
            finish_page:[]
          }
        },
        methods: {
          handleGo:function () {
            this.page_index = this.page_index - 1;
            if (this.finish_page !== []){
              this.finish_page.pop()
            }
          },
          handleBack:function () {
            this.finish_page.push(this.page_index);
            this.page_index = this.page_index + 1;
          }
        },
        mounted() {
          let that = this;
          this.$axios.post('api/older').then(res=>{
            let data = res.data.data;
            that.page_index = data.length;
            that.length = data.length;
            for (let i=0; i<data.length; i++){
              let dict = {};
              dict['url'] = data[i][0];
              dict['name'] = data[i][1];
              dict['title'] = data[i][2];
              dict['content'] = data[i][3];
              dict['detail'] = data[i][5];
              that.model_people.push(dict)
            }
          })
        }
    }
</script>

<style scoped>
  .detail-header{
    width: 100%;
    height: 200px;
    display: flex;
    flex-direction: row;
  }
  .detail-text{
    width: 70%;
    height: 100%;
  }
  .detail-text-name{
    height: 50%;
    width: 100%;
  }
  .detail-text-name1{
    font-size: 40px;
    color: #343434;
    font-weight: bold;
    position: relative;
    margin-left: 40px;
    margin-top: 20px;
  }
  .detail-text-content{
    height: 50%;
    width: 100%;
  }
  .detail-text-content1{
    font-size: 18px;
    margin-left: 40px;
  }
  .img-box{
    width: 30%;
    height: 100%;
  }
  .img-box img{
    width: 100%;
    height: 100%;
  }
  .main-bg{
    min-width: 1400px;
    height: 100%;
    background-image: url("/static/picture/model_people_bg.jpg");
    background-position: center center;
    background-repeat: no-repeat;
    background-size: 100% 100%;
  }
  .back-btn{
    width: 70px;
    height: 70px;
    float: left;
    position: absolute;
    top: 45%;
    left: 40px;
    background: #ddd;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    cursor: pointer;
  }
  .back-btn img{
    width: 50px;
    height: 50px;
  }
  .go-btn{
    width: 70px;
    height: 70px;
    position: absolute;
    float: right;
    right: 40px;
    top: 45%;
    background: #ddd;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    cursor: pointer;
  }
  .go-btn img{
    width: 50px;
    height: 50px;
  }
  .book {
    position: absolute;
    width: 600px;
    height:870px;
    left: 50%;
    background-color: #fff;
    border-bottom: 10px #8c939d solid;
    -webkit-transform: rotateX(30deg);
    -ms-transform: rotateX(30deg);
    -o-transform: rotateX(30deg);
    transform: rotateX(30deg);
  }
  .preserve-3d {
    -webkit-transform-style: preserve-3d;
    -moz-transform-style: preserve-3d;
    -ms-transform-style: preserve-3d;
    transform-style: preserve-3d;
  }
  .book-page {
    position: absolute;
    top: 0;
    left: 0;
    width: 600px;
    height: 870px;
    border: 1px solid #8c939d;
    padding: 10px;
    background: #fff;
  }
  .book-page div{
    backface-visibility: hidden;
  }
  .book-page-box {
    -webkit-transform-origin: 0 50%;
    -moz-transform-origin: 0 50%;
    -ms-transform-origin: 0 50%;
    -o-transform-origin: 0 50%;
    transform-origin: 0 50%;
    -webkit-transform: rotateY(0deg);
    -ms-transform: rotateY(0deg);
    -o-transform: rotateY(0deg);
    transform: rotateY(0deg);
  }
  .preserve-3d {
    -webkit-transform-style: preserve-3d;
    -moz-transform-style: preserve-3d;
    -ms-transform-style: preserve-3d;
    transform-style: preserve-3d;
  }
  @keyframes flipBook1 {
    0% {
      -webkit-transform: rotateY(0deg);
      -ms-transform: rotateY(0deg);
      -o-transform: rotateY(0deg);
      transform: rotateY(0deg);
    }
    100% {
      -webkit-transform: rotateY(-175deg);
      -ms-transform: rotateY(-175deg);
      -o-transform: rotateY(-175deg);
      transform: rotateY(-175deg);
    }
  }

  /* Firefox */
  @-moz-keyframes flipBook1 {
     0% {
      -webkit-transform: rotateY(0deg);
      -ms-transform: rotateY(0deg);
      -o-transform: rotateY(0deg);
      transform: rotateY(0deg);
    }
    100% {
      -webkit-transform: rotateY(-175deg);
      -ms-transform: rotateY(-175deg);
      -o-transform: rotateY(-175deg);
      transform: rotateY(-175deg);
    }
  }

  /* Safari and Chrome */
  @-webkit-keyframes flipBook1 {
    0% {
      -webkit-transform: rotateY(0deg);
      -ms-transform: rotateY(0deg);
      -o-transform: rotateY(0deg);
      transform: rotateY(0deg);
    }
     100% {
      -webkit-transform: rotateY(-175deg);
      -ms-transform: rotateY(-175deg);
      -o-transform: rotateY(-175deg);
      transform: rotateY(-175deg);
    }
  }

  /* Opera */
  @-o-keyframes flipBook1 {
     0% {
      -webkit-transform: rotateY(0deg);
      -ms-transform: rotateY(0deg);
      -o-transform: rotateY(0deg);
      transform: rotateY(0deg);
    }
    100% {
      -webkit-transform: rotateY(-175deg);
      -ms-transform: rotateY(-175deg);
      -o-transform: rotateY(-175deg);
      transform: rotateY(-175deg);
    }
  }
  @keyframes flipBook2 {
    0% {
      -webkit-transform: rotateY(-175deg);
      -ms-transform: rotateY(-175deg);
      -o-transform: rotateY(-175deg);
      transform: rotateY(-175deg);
    }
    100% {
      -webkit-transform: rotateY(0deg);
      -ms-transform: rotateY(0deg);
      -o-transform: rotateY(0deg);
      transform: rotateY(0deg);
    }
  }

  /* Firefox */
  @-moz-keyframes flipBook2 {
    0% {
      -webkit-transform: rotateY(-175deg);
      -ms-transform: rotateY(-175deg);
      -o-transform: rotateY(-175deg);
      transform: rotateY(-175deg);
    }
    100% {
      -webkit-transform: rotateY(0deg);
      -ms-transform: rotateY(0deg);
      -o-transform: rotateY(0deg);
      transform: rotateY(0deg);
    }
  }

  /* Safari and Chrome */
  @-webkit-keyframes flipBook2 {
     0% {
      -webkit-transform: rotateY(-175deg);
      -ms-transform: rotateY(-175deg);
      -o-transform: rotateY(-175deg);
      transform: rotateY(-175deg);
    }
    100% {
      -webkit-transform: rotateY(0deg);
      -ms-transform: rotateY(0deg);
      -o-transform: rotateY(0deg);
      transform: rotateY(0deg);
    }
  }

  /* Opera */
  @-o-keyframes flipBook2 {
     0% {
      -webkit-transform: rotateY(-175deg);
      -ms-transform: rotateY(-175deg);
      -o-transform: rotateY(-175deg);
      transform: rotateY(-175deg);
    }
    100% {
      -webkit-transform: rotateY(0deg);
      -ms-transform: rotateY(0deg);
      -o-transform: rotateY(0deg);
      transform: rotateY(0deg);
    }
  }
  .flip-animation-1 {
    animation: flipBook1 8s forwards;
    -moz-animation: flipBook1 8s forwards; /* Firefox */
    -webkit-animation: flipBook1 8s forwards; /* Safari and Chrome */
    -o-animation: flipBook1 8s forwards; /* Opera */
  }

  .flip-animation-2 {
    animation: flipBook2 8s forwards;
    -moz-animation: flipBook2 8s forwards; /* Firefox */
    -webkit-animation: flipBook2 8s forwards; /* Safari and Chrome */
    -o-animation: flipBook2 8s forwards; /* Opera */
  }
</style>

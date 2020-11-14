<template>
    <div>
      <div class="main-content">
        <div class="exam_box">
          <div class="exam_box_container">
            <ul>
              <li>
                <div class="exam_box1">
                  <img class="snow-bg" src="/static/picture/snow.png">
                  <div class="main-title-box">
                    <span class="main-title-box-1">在线模考</span>
                    <span class="main-title-box-2">精选近年入党积极分子考试题目智能组卷，在线测验</span>
                  </div>
                  <div class="title-box">
                    <div class="pic-exam">
                      <img class="icon-exam" src="/static/picture/ic_examine.png">
                    </div>
                    <span>入党积极分子模拟测验</span>
                  </div>
                </div>
                <div class="exam-box2">
                  <ul>
                    <li @click="Transfer1" v-for="(item,index) in paper_list_1">
                      <div class="card-container">
                        <div class="exam-title">
                          <a href="#">{{item.title}}</a>
                          <i>{{item.time}}</i>
                        </div>
                        <div class="hot-logo" v-if="item.hot===1">
                          <div class="hot-logo-img"></div>
                        </div>
                      </div>
                    </li>
                  </ul>
                </div>
                <div class="footer">
                  <a href="#" @click="Transfer1">随机练习</a>
                </div>
              </li>
              <li>
                <div class="exam_box1" style="background-color: #f49537">
                  <img class="snow-bg" src="/static/picture/snow.png">
                  <div class="main-title-box">
                    <span class="main-title-box-1">党史测验</span>
                    <span class="main-title-box-2">精选党史知识难点重点，题目智能组卷，在线测验</span>
                  </div>
                  <div class="title-box">
                    <div class="pic-exam">
                      <img class="icon-exam" src="/static/picture/ic_examine.png">
                    </div>
                    <span>党史知识模拟测验</span>
                  </div>
                </div>
                <div class="exam-box2">
                  <ul>
                    <li @click="Transfer2" v-for="(item,index) in paper_list_2">
                      <div class="card-container">
                        <div class="exam-title">
                          <a href="#">{{item.title}}</a>
                          <i>{{item.time}}</i>
                        </div>
                        <div class="hot-logo" v-if="item.hot===1">
                          <div class="hot-logo-img"></div>
                        </div>
                      </div>
                    </li>
                  </ul>
                </div>
                <div class="footer">
                  <a href="#" @click="Transfer2">随机练习</a>
                </div>
              </li>
              <li>
                <div class="exam_box1" style="background-color: #a2c926">
                  <img class="snow-bg" src="/static/picture/snow.png">
                  <div class="main-title-box">
                    <span class="main-title-box-1">章节测验</span>
                    <span class="main-title-box-2">根据在线学习每章节的内容，进行重点知识抽查，重点掌握</span>
                  </div>
                  <div class="title-box">
                    <div class="pic-exam">
                      <img class="icon-exam" src="/static/picture/ic_examine.png">
                    </div>
                    <span>章节测验</span>
                  </div>
                </div>
                <div class="exam-box2">
                  <ul>
                    <li @click="Transfer2" v-for="(item,index) in paper_list_3">
                      <div class="card-container">
                        <div class="exam-title">
                          <a href="#">{{item.title}}</a>
                          <i>{{item.time}}</i>
                        </div>
                        <div class="hot-logo" v-if="item.hot===1">
                          <div class="hot-logo-img"></div>
                        </div>
                      </div>
                    </li>
                  </ul>
                </div>
                <div class="footer">
                  <a href="#" @click="Transfer2">随机练习</a>
                </div>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>
</template>

<script>
    export default {
       name: "exam",
       data(){
          return{
            paper_list_1:[
              {title: '2019年入党积极分子考试题目', time:'2020-03-24', hot: 1},
              {title: '2018年入党积极分子考试题目', time:'2020-09-12', hot: 0}
            ],
            paper_list_2:[
              {title:'党史测验题1', time:'2020-09-28', hot: 1},
              {title:'党史测验题2', time:'2020-10-12', hot: 0},
              {title:'党史测验题3', time:'2020-10-25', hot: 1},
              {title:'党史测验题', time:'2020-11-02', hot: 0}
            ],
            paper_list_3:[
              {title:'章节1测验题', time:'2020-10-21',hot: 1},
              {title:'章节2测验题',time:'2020-11-03', hot: 1},
              {title:'章节3测验题',time:'2020-11-25', hot: 0}
            ]
          }
       },
      methods:{
         Transfer1:function () {
           this.$emit('child-event', '1')
         },
         Transfer2:function () {
           this.$emit('child-event', '2')
         }
      }
    }
</script>

<style scoped>
  .main-content{
    width: 1200px;
    height: auto;
    margin: 60px auto;
    position: relative;
    margin-bottom: 15px;
  }
  .exam_box{
    width: 100%;
    height: auto;
    margin: 0 auto 20px auto;
  }
  .exam_box_container{
    width: 100%;
    height: 489px;
  }
  .exam_box_container li{
    width: 31.5%;
    height: 100%;
    margin-right: 20px;
    background: #fff;
    float: left;
    position: relative;
    overflow: hidden;
  }
  .exam_box1{
    width: 100%;
    height: 150px;
    background-color: #42abfb;
    text-align: center;
    overflow: hidden;
  }
  .snow-bg{
    width: 100%;
    height: 100%;
    opacity: 0.6;
  }
  .pic-exam{
    margin: 0 auto;
    margin-bottom: 14px;
    padding: 20px;
    border-radius: 50%;
    width: 48px;
    height: 48px;
    background: #fff;
  }
  .icon-exam{
    position: relative;
    width: 35px;
    top: -18px;
    left: 4px;
  }
  .title-box{
    width: 100%;
    text-align: center;
    transform: translate(0, -165px);
    transition: all 200ms;
    -webkit-transform: translate(0, -165px);
  }
  .title-box span{
    color: #fff;
    font-size: 20px;
    font-weight: bold;
  }
  .exam_box_container li:hover .title-box{
    transform: translate(0, -50px);
    -webkit-transform: translate(0, -50px);
  }
  .exam_box_container li:hover .main-title-box{
    transform: translate(0, -112px);
    -webkit-transform: translate(0, -112px);
  }
  .main-title-box{
    display: block;
    width: 350px;
    height: auto;
    transform: translate(-360px -112px);
    -webkit-transform: translate(-360px, -112px);
    text-align: center;
    transition: all 200ms;
  }
  .main-title-box-1{
    color: #fff;
    font-size: 20px;
    font-weight: bold;
  }
  .main-title-box-2{
    color: #fff;
    text-align: center;
    float: left;
  }
  .exam-box2{
    height: 243px;
    width: 100%;
    background: #fff;
    box-shadow: 4px 4px 10px 5px #8c939d;
  }
  .exam-box2 ul{
    width: 100%;
    margin-top: 0;
  }
  .exam-box2 li{
    margin-left: -40px;
    width: 100%;
    height: 60px;
    display: inline-block;
    float: left;
    transition: all 200ms linear;
    -webkit-transition: all 200ms linear;
    border-bottom: 1px solid #cdcdcd;
    cursor: pointer;
  }
  .exam-box2 li:hover{
    background: #f5f5f5;
  }
  .exam-box2 li a{
    color: #333;
    text-decoration: none;
    height: 30px;
    line-height: 30px;
    width: 340px;
    overflow: hidden;
    white-space: nowrap;
    font-weight: 500;
    float: left;
    margin-left: 20px;
    transition: all 200ms linear;
    -webkit-transition: all 200ms linear;
  }
  .exam-box2 li i{
    width: auto;
    color: #aaa;
    font-size: 12px;
    margin-right: 60px;
    background: 0;
    height: 20px;
    float: left;
    line-height: 20px;
    display: block;
    position: inherit;
    margin-left: 20px;
  }
  .footer{
    width: 100%;
    height: 80px;
    border-top: 1px solid #eaeaea;
    background: #f2f2f2;
    text-align: center;
  }
  .footer a{
    width: 110px;
    border: 1px solid #ddd;
    line-height: 30px;
    display: inline-block;
    color: #379be7;
    background: #fff;
    text-align: center;
    transition: all 100ms linear;
    -webkit-transition: all 100ms linear;
    border-radius: 3px;
    box-shadow: 0 3px 2px rgba(0, 0, 0, 0.05);
    -moz-box-shadow: 0 3px 2px rgba(0, 0, 0, 0.05);
    -webkit-box-shadow: 0 3px 2px rgba(0, 0, 0, 0.05);
    margin-top: 25px;
    text-decoration: none;
  }
  .footer a:hover{
    background: #379be7;
    color: #fff;
  }
  .card-container{
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: row;
    align-items: center;
  }
  .exam-title{
    width: 80%;
    height: 100%;
  }
  .hot-logo{
    width: 20%;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }
  .hot-logo-img{
    width: 40px;
    height: 40px;
    background: url("/static/picture/hot.gif") no-repeat center center;
    background-size: cover;
  }
</style>


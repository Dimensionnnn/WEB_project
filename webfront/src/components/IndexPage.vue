<template>
    <div>
      <div class="backgroud">
        <div class="w1330_index">
          <div class="Logo_top">
            <div class="header-title">
              <img src="/static/picture/title.png" class="title_picture">
            </div>
          </div>
          <div class="main-body">
            <div class="nav-line">
              <div class="index-nav">
                <el-row>
                  <el-col :span="6">
                    <el-dropdown @command="handleCommand1">
                      <span class="el-dropdown-link">全景旅游</span>
                      <el-dropdown-menu slot="dropdown">
                        <el-dropdown-item v-for="(list, index) in special_list" :key="index" :command="list.command">
                          <div class="drop-down-box">
                            <div class="drop-down-title">| {{list.title}}</div>
                            <div class="drop-down-content">| {{list.content}}</div>
                          </div>
                        </el-dropdown-item>
                      </el-dropdown-menu>
                    </el-dropdown>
                  </el-col>
                  <el-col :span="6">
                    <el-dropdown @command="handleCommand2">
                      <span class="el-dropdown-link">学习专区</span>
                      <el-dropdown-menu slot="dropdown">
                        <el-dropdown-item v-for="(list, index) in study_area" :key="index" :command="list.command">
                          <div class="drop-down-box">
                            <div class="drop-down-title">| {{list.title}}</div>
                            <div class="drop-down-content">| {{list.content}}</div>
                          </div>
                        </el-dropdown-item>
                      </el-dropdown-menu>
                    </el-dropdown>
                  </el-col>
                  <el-col :span="6">
                    <el-dropdown @command="handleCommand3">
                      <span class="el-dropdown-link">个人空间</span>
                      <el-dropdown-menu slot="dropdown">
                        <el-dropdown-item v-for="(list, index) in personal_area" :key="index" :command="list.command">
                          <div class="drop-down-box">
                            <div class="drop-down-title">| {{list.title}}</div>
                            <div class="drop-down-content">| {{list.content}}</div>
                          </div>
                        </el-dropdown-item>
                      </el-dropdown-menu>
                    </el-dropdown>
                  </el-col>
                  <el-col :span="6">
                    <el-dropdown @command="handleCommand4">
                      <span class="el-dropdown-link">党建天地</span>
                      <el-dropdown-menu slot="dropdown">
                        <el-dropdown-item v-for="(list, index) in party_area" :key="index" :command="list.command">
                          <div class="drop-down-box">
                            <div class="drop-down-title">| {{list.title}}</div>
                            <div class="drop-down-content">| {{list.content}}</div>
                          </div>
                        </el-dropdown-item>
                      </el-dropdown-menu>
                    </el-dropdown>
                  </el-col>
                </el-row>
              </div>
            </div>
            <div class="banner">
              <el-carousel :height="bannerheight+'px'">
                <el-carousel-item v-for="(img, index) in banner" :key="index">
                  <img style="width: 100%" ref="bannerheight" v-bind:src="img.url">
                </el-carousel-item>
              </el-carousel>
            </div>
            <div class="divider1">
              新闻动态
            </div>
            <el-row>
              <el-col :span="12">
                <el-carousel :interval="4000" style="width: 600px; margin-top: 20px" :height="350+'px'">
                  <el-carousel-item v-for="(img, index) in news" :key="index">
                    <img v-bind:src="img.url" style="width: 100%; height: 350px" class="image">
                    <div class="hover-news">
                      <span class="news-title">{{img.title}}</span>
                    </div>
                  </el-carousel-item>
                </el-carousel>
              </el-col>
              <el-col :span="12">
                <div class="news-list">
                  <el-scrollbar style="width: 100%; height: 100%">
                    <ul>
                      <li class="news-list-item" v-for="(news, index) in news_outline" :key="index"
                          @click="handleNewsClick(news.id)">
                        {{news.title}}
                      </li>
                    </ul>
                  </el-scrollbar>
                </div>
              </el-col>
            </el-row>
            <div class="divider1">
              特别活动推荐
            </div>
            <el-row style="margin-top: 50px;">
              <el-col :span="6" v-for="(img, index) in card" :key="index" :offset="index > 0 ? 3 : 0">
                <el-card :body-style="{ padding: '0px', width: '100%' }" shadow="hover" class="boxShadow wow fadeInDown">
                  <img v-bind:src="img.url" class="image">
                  <div style="padding: 14px;">
                    <span class="card-text">{{img.text}}</span>
                  </div>
                  <div style="padding: 14px">
                    <span class="card-content">{{img.content}}</span>
                  </div>
                </el-card>
              </el-col>
            </el-row>
            <div class="divider1">
              大数据统计
            </div>
            <el-row style="margin-top: 20px">
              <el-col :span="8">
                <div class="data-box box-slide1 wow fadeInDown">
                  <div class="data-img">
                    <img src="/static/picture/study.png">
                  </div>
                  <div class="data-content">
                    <div class="data-number">{{study_hours}}</div>
                    <div class="data-analyse">本学期一共学习时长</div>
                  </div>
                </div>
              </el-col>
              <el-col :span="8">
                <div class="data-box box-slide2 wow fadeInDown">
                  <div class="data-img">
                    <img src="/static/picture/activity.png">
                  </div>
                  <div class="data-content">
                    <div class="data-number">{{activity_hours}}</div>
                    <div class="data-analyse">本学期一共参加活动时长</div>
                  </div>
                </div>
              </el-col>
              <el-col :span="8">
                <div class="data-box box-slide3 wow fadeInDown">
                  <div class="data-img">
                    <img src="/static/picture/score.png">
                  </div>
                  <div class="data-content">
                    <div class="data-number">{{score}}</div>
                    <div class="data-analyse">本学期一共累计积分</div>
                  </div>
                </div>
              </el-col>
            </el-row>
             <div class="footer">
                沪公网安备31011502009号
             </div>
          </div>
        </div>
      </div>
    </div>
</template>

<script>
    import {WOW} from '../assets/js/wow.min.js'
    export default {
        name: "IndexPage",
        data(){
          return {
            bannerheight:"",
            study_hours:0,
            activity_hours:0,
            score:0,
            news_outline:[],
            banner:[],
            card:[],
            news:[],
            special_list:[
              {title:'史海遨游', content:'通过VR让你360°游览红色景点。感受革命先辈，仁人烈士的风采与精神',command:'a'},
              {title:'重走长征路', content:'在虚拟长征地图中带领你重走长征路，不忘初心，砥砺前行',command:'b'}
            ],
            study_area:[
              {title:'有声故事书', content:'让"小精灵"带你一起品读历史，了解一个个了不起成就的背后不为人知故事',command:'a'},
              {title:'心得分享',content:'与志同道合的小伙伴一起交流学习，共同进步',command:'b'},
              {title:'在线学习',content:'在线学习，课程节奏掌控自如',command:'c'},
              {title:'模拟测验',content:'智能组卷，测一测自己学习的成果吧',command:'d'}
            ],
            personal_area:[
              {title:'学习计划',content:'自定义学习计划，我的学习我做主',command:'a'},
              {title:'会议助手',content:'一键预约活动教室和会议室',command:'b'},
              {title:'入党阶段',content:'看看自己离成为光荣的党员还差了多少',command:'c'},
              {title:'活动积分',content:'获得足够多的的积分将会获得神秘奖励',command:'d'},
              {title:'我的错题',content:'温故而知新，可以为师矣',command:'e'}
            ],
            party_area:[
              {title:'外交足迹',content:'跟随习大大的脚步，纵览大国外交',command:'a'},
              {title:'前辈寄语',content:'听听老同志们对我们的谆谆教诲',command:'b'},
              {title:'模范党支部',content:'学习的榜样',command:'c'},
              {title:'组织生活窗',content:'记录党组织生活的点点滴滴',command:'d'}
            ]
          }
        },
        methods:{
          data_init:function () {
            let that = this;
            this.$axios.post('api/credit').then(function (res) {
              let data = res.data.data;
              that.study_hours = data[0][0];
              that.activity_hours = data[0][1];
              that.score = data[0][2]
            })
          },
          init_card:function(){
            let that = this;
            this.$axios.post('api/act').then(function (res) {
              let cards = res.data.data;
              for (let i=0; i<cards.length; i++){
                let dict = {};
                dict['url'] = cards[i][0];
                dict['text'] = cards[i][1];
                dict['content'] = cards[i][2];
                that.card.push(dict)
              }
            })
          },
          init_news_outline:function(){
            let that = this;
            this.$axios.post('api/news/outline').then(function (res) {
              let news = res.data.data;
              for (let i=0; i<news.length; i++) {
                let dict = {};
                dict['title'] = news[i][1];
                dict['content'] = news[i][2];
                dict['id'] = news[i][0];
                that.news_outline.push(dict)
              }
            });
          },
          init_header_banner:function(){
            let that = this;
            this.$axios.post('api/header/banner').then(function (res) {
              let data = res.data.data;
              for (let i=0; i<data.length; i++){
                let dict = {};
                dict['url'] = data[i][0];
                that.banner.push(dict)
              }
            })
          },
          init_news_pic:function(){
            let that = this;
            this.$axios.post('api/news/banner').then(function (res) {
              let data = res.data.data;
              for (let i=0; i<data.length; i++){
                let dict = {};
                dict['url'] = data[i][0];
                dict['title'] = data[i][1];
                that.news.push(dict)
              }
            })
          },
          handleCommand1:function (command) {
            if (command === 'a'){
              let new_url = this.$router.resolve({path:'/red_scenery'});
              window.open(new_url.href)
            }
          },
          handleCommand2:function (command) {
            if (command === "b"){
              let new_url = this.$router.resolve({path:'/message'});
              window.open(new_url.href);
            }
            else if (command === 'd'){
              let new_url = this.$router.resolve({path:'/exam'});
              window.open(new_url.href)
            }
          },
          handleCommand3:function (command) {

          },
          handleCommand4:function (command) {
            if (command === "a"){
              let new_url = this.$router.resolve({path:'/diplomat'});
              window.open(new_url.href)
            }
            else if (command === "b"){
              let new_url = this.$router.resolve({path:'/interview'});
              window.open(new_url.href)
            }
            else if (command === "c"){
              let new_url = this.$router.resolve({path:'/modelparty'});
              window.open(new_url.href)
            }
            else{
              let new_url = this.$router.resolve({path:'/window'});
              window.open(new_url.href)
            }
          },
          handleNewsClick:function (index) {
            const new_href = this.$router.resolve({
              path: '/news',
              query: {
                id: index
              }
            });
            window.open(new_href.href)
          }
        },
      watch:{
          study_hours(idx){
            console.log(idx)
          }
      },
        mounted() {
          window.addEventListener('resize', () => {
            this.bannerheight = this.$refs.bannerheight[0].height;
          },false);
          this.data_init();
          new WOW().init();
        },
        created() {
          this.init_news_outline();
          this.init_header_banner();
          this.init_news_pic();
          this.init_card()
        }
    }
</script>

<style scoped>
  .backgroud{
    padding-top: 0;
    position: relative;
    box-sizing: border-box;
    height: 750px;
    width: 100%;
    min-width: 1400px;
    background: url("/static/picture/bg_index.jpg") no-repeat;
    background-position: center 0
  }
  .w1330_index{
    width: 1200px;
    position: relative;
    margin-left: auto;
    margin-right: auto;
    z-index: 1;
  }
  .Logo_top{
    padding-top: 20px;
    position: relative;
    z-index: 2;
    height: 150px;
    box-sizing: border-box;
  }
  .header-title{
    width: 500px;
    height: 200px;
    margin-left: auto;
    margin-right: auto;
    margin-top: -142px;
  }
  .title_picture{
    width: 600px;
    height: 100px;
    margin: 0 auto;
    margin-top: 183px;
    margin-left: -20px;
  }
  .main-body{
    width: 100%;
    background-color: #fff;
    box-sizing: border-box;
    padding: 0 35px;
    position: relative;
    z-index: 10;
    box-shadow: 0 6px 30px 0 rgba(0, 0, 0, 0.4);
    border-radius: 8px 8px 0 0;
    animation: main-body-animate 1s forwards;
    animation-delay: 0.5s;
    animation-fill-mode: both;
  }
  @keyframes main-body-animate {
    0%{margin-top: 40px;opacity: 0}
    100%{margin-top: 62px;opacity: 1}
  }
  @-webkit-keyframes main-body-animate {
    0%{margin-top: 40px;opacity: 0}
    100%{margin-top: 62px;opacity: 1}
  }
  .nav-line{
    width: 100%;
    padding-top: 18px;
    text-align: center;
    box-shadow: 0 10px 10px -10px rgba(0, 0, 0, 0.4);
  }
  .index-nav{
    width: 100%;
    float: none;
    display: inline-block;
    text-align: center;
  }
  .functions {
    text-align: center;
    box-sizing: border-box;
    margin: 0 -20px 0 -10px;
    display: inline-block;
  }
  .el-dropdown-link{
    display: block;
    line-height: 50px;
    color: rgba(0, 0, 0, 0.65);
    font-weight: bold;
    position: relative;
    letter-spacing: 0.6px;
  }
  /deep/.el-scrollbar__wrap {
    overflow-x: hidden;
  }
  .el-dropdown-link{
    text-decoration: none;
    position: relative;
    font-size: 18px;
  }
  .el-dropdown-link:hover{
    font-size: 23px;
  }
  .el-dropdown-link::before{
    content: "";
    position: absolute;
    left: 50%;
    bottom: -6px;
    width: 0;
    height: 4px;
    border-radius: 5px;
    background: #ce0000;
    transition: all .3s;
  }
  .el-dropdown-link:hover::before{
    width: 100%;
    left: 0;
    right: 0;
  }
  .banner{
    margin-top: 56px;
  }
  .image {
    width: 100%;
    display: block;
  }

  .divider1{
    width: 100%;
    margin-top: 20px;
    font-size: 30px;
    font-weight: bold;
    color: #ce0000;
    text-align: center;
  }
  .el-card{
    cursor: pointer;
  }
  .card-text{
    font-size: 20px;
    font-weight: bold;
    color: #ce0000;
    font-style: oblique;
  }
  .footer{
    margin-top: 30px;
    text-align: center;
    margin-bottom: 50px;
  }
  .boxShadow:hover{
    box-shadow: 0 6px 20px rgba(255, 0, 0, 0.4);
  }
  .boxShadow{
    -webkit-animation: fadeInDown 2s ease-out 0.5s 1 both;
  }
  @-webkit-keyframes fadeInDown{
  0%{opacity:0;-webkit-transform:translate3d(0,-20%,0);transform:translate3d(0,-20%,0)}
  100%{opacity:1;-webkit-transform:none;transform:none}
  }
  @keyframes fadeInDown{
    0%{opacity:0;-webkit-transform:translate3d(0,-20%,0);-ms-transform:translate3d(0,-20,0);transform:translate3d(0,-20%,0)}
    100%{opacity:1;-webkit-transform:none;-ms-transform:none;transform:none}
  }
.fadeInDown{-webkit-animation-name:fadeInDown;animation-name:fadeInDown}

  .drop-down-title{
    text-align: left;
    font-size: 20px;
    font-weight: bold;
    color: #ce0000;
  }
  .drop-down-content{
    margin-top: 10px;
    font-size: 15px;
    text-align: left;
    margin-bottom: 10px;
    line-height: 20px;
  }
  .drop-down-box{
    width: 250px;
    border-bottom: #cdcdcd 1px solid;
  }
  .drop-down-box:hover .drop-down-title{
    animation: title-change 0.5s forwards;
  }
  @keyframes title-change {
    0%{font-size: 20px}
    100%{font-size: 23px}
  }
  @-khtml-keyframes title-change {
    0%{font-size: 20px}
    100%{font-size: 23px}
  }
  .hover-news{
    width: 100%;
    height: 100%;
    position: absolute;
    top: 0;
    left: 0;
    text-align: center;
    background-color: rgba(14,22,32,0.7);
    opacity: 0;
    transition: all .4s;
    cursor: pointer;
  }
  .hover-news:hover{
    opacity: 1;
  }
  .news-title{
    color: white;
    font-size: 20px;
    position: relative;
    top: 185px;
  }
  .news-list{
    width: 500px;
    height: 385px;
    position: absolute;
    margin-left: 46px;
  }
  .news-list-item{
    display: inline-block;
    vertical-align: initial;
    transform: perspective(1px) translateZ(0);
    box-shadow: 0 0 1px transparent;
    position: relative;
    transition-property: color;
    transition-duration: 0.5s;
    cursor: pointer;
  }
  .news-list li{
    background: #f1ddb6;
    width: 400px;
    height: 40px;
    padding: 15px 25px;
    margin-bottom: 1px;
  }
  .news-list li::before{
    content:"";
    position: absolute;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    background: #b01a16;
    transform: scaleX(0);
    transition-property: transform;
    transition-duration: 0.5s;
    transition-timing-function: ease-out;
    transform-origin: 0 50%;
    z-index: -1;
  }
  .news-list li:hover::before{
    transform: scaleX(1);
    opacity: 1;
    transition-timing-function: cubic-bezier(0.52, 1.64, 0.37, 0.66);
  }
  .news-list li:hover{
    color: white;
  }
  .data-box{
    display: block;
    box-sizing: border-box;
    position: relative;
    padding: 12px;
  }
  .data-img{
    position: relative;
    text-align: center;
    animation: img-animate 1s infinite;
  }
  .data-content{
    margin-top: 40px;
    text-align: center;
  }
  .data-number{
    font-size: 48px;
    line-height: 50px;
  }
  .data-analyse{
    margin-top: 10px;
    font-size: 18px;
    color: #999999;
  }
  .data-box:hover .data-number{
    animation: number-change .3s forwards;
  }
  @keyframes number-change {
    0%{font-size: 48px}
    100%{font-size: 53px}
  }
  @-webkit-keyframes number-change {
    0%{font-size: 48px}
    100%{font-size: 53px}
  }
  .data-box::before{
    content: "";
    position: absolute;
    left: 50%;
    bottom: -6px;
    width: 0;
    height: 4px;
    border-radius: 10px;
    background: #3399ff;
    transition: all .3s;
  }
  .data-box:hover::before{
    width: 100%;
    left: 0;
    right: 0;
  }
  @keyframes img-animate {
    0%{top: -10px}
    50%{top: 10px}
    100%{top: -10px}
  }
  @-webkit-keyframes img-animate {
    0%{top: -10px}
    50%{top: 10px}
    100%{top: -10px}
  }
  .box-slide1{
    -webkit-animation: fadeInDown 2s ease-out 0.5s 1 both;
  }
  .box-slide2{
    -webkit-animation: fadeInDown 2s ease-out 1s 1 both;
  }
  .box-slide3{
    -webkit-animation: fadeInDown 2s ease-out 1.5s 1 both;
  }
</style>

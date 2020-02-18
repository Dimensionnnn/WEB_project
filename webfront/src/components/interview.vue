<template>
  <div style="height: 100%">
    <partynav></partynav>
    <div class="top-banner">
      <div class="swipper-container">
        <div class="swipper-wrapper">
          <div class="main_bg">
            <div class="bg_cover">
              <div class="content_container">
                <div class="content-title">
                  <span>先辈寄语</span>
                </div>
                <div class="vice-title">
                  <span>从先辈的手中接过历史的接力棒，走好我们这一代人的长征路</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="items-body" style="background: #efefef">
      <div class="main-wrap">
        <p class="main-title">共和国荣誉勋章获得者</p>
        <div class="main-content">
          <ul>
            <div v-for="(item,index) in medal_list" :key="index">
              <li>
                <div class="img-box">
                  <img v-bind:src="item.url">
                  <el-popover placement="bottom-start" v-bind:title="item.title" width="200" trigger="hover"
                              v-bind:content="item.content">
                    <div class="hover-element" slot="reference">
                      <div class="info-box">
                        <div class="in-title-text">
                          <span>{{item.name}}</span>
                        </div>
                      </div>
                    </div>
                  </el-popover>
                </div>
              </li>
            </div>
          </ul>
        </div>
      </div>
    </div>
    <div class="items-body">
      <div class="main-wrap">
        <p class="main-title">部分全国道德模范</p>
        <div class="main-content">
          <ul>
            <div v-for="(item,index) in moral_list" :key="index">
              <li>
                <div class="img-box">
                  <img v-bind:src="item.url">
                  <div class="hover-element">
                    <div class="info-box">
                      <div class="in-title-text">
                        <span>{{item.name}}</span>
                      </div>
                    </div>
                  </div>
                </div>
              </li>
            </div>
          </ul>
        </div>
      </div>
    </div>
    <div class="items-body" style="background: rgba(255,96,0,0.1)">
      <div class="main-wrap">
        <p class="main-title" style="color: #cc2a1d">部分全国道德模范</p>
        <div class="main-content">
          <ul>
            <div v-for="(item,index) in reform_list" :key="index">
              <li>
                <div class="img-box">
                  <img v-bind:src="item.url">
                  <div class="hover-element">
                    <div class="info-box">
                      <div class="in-title-text">
                        <span>{{item.name}}</span>
                      </div>
                    </div>
                  </div>
                </div>
              </li>
            </div>
          </ul>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
    import {WOW} from '../assets/js/wow.min.js'
    import partynav from '@/components/partynav.vue'
    export default {
        name: "interview",
        components:{
          partynav
        },
        data(){
          return {
            medal_list:[
              {url:require('../assets/picture/zhangfuqing.jpg'),name:'张富清',title:'深藏功与名的共和国英雄',
              content:'和我并肩作战多年的战友，有好多都牺牲了，他们才是真正的英雄'},
              {url:require('../assets/picture/yumin.jpg'), name:'于敏',title:'氢弹之父，国家脊梁',
                content:'国家需要我，我一定全力以赴'},
              {url:require('../assets/picture/shenjilan.jpg'),name:'申纪兰',title:'人民的好代表',
                content:'要和乡亲们在一起，把根永远扎根在农村大地上'},
              {url:require('../assets/picture/sunjiadong.jpg'), name:'孙家栋',title:'志在苍穹，星河灿烂',
                content:'能造一辈子中国“星”，是我人生最大的心愿'},
              {url:require('../assets/picture/liyannian.jpg'), name:'李延年',title:'抗美援朝，永葆军人本色',
              content:'当初当兵我就做好了准备，命就交给国家了'},
              {url:require('../assets/picture/yuanlongping.jpg'),name:'袁隆平',title:'撒播智慧，收获富足',
              content:'中国人的饭碗要牢牢掌握在自己手中'},
              {url:require('../assets/picture/huangxuhua.jpg'),name:'黄旭华',title:'大国重器，潜艇之父',
              content:'我的一生属于核潜艇，属于祖国，无怨无悔'},
              {url:require('../assets/picture/tuyouyou.jpg'),name:'屠呦呦',title:'青蒿一握，拯救多少生命',
              content:'青蒿素研究获奖是中国科学家集体的荣誉'}
            ],
            moral_list:[
              {url:require('../assets/picture/道德模范/道德模范-杜富国.jpg'),name:'杜富国',animate:'box-slide1'},
              {url:require('../assets/picture/道德模范/道德模范-蓝连青.jpg'),name:'蓝连青',animate:'box-slide2'},
              {url:require('../assets/picture/道德模范/道德模范-刘传健.png'),name:'刘传健',animate:'box-slide3'},
              {url:require('../assets/picture/道德模范/道德模范-尤良英.jpg'),name:'尤良英',animate:'box-slide4'},
              {url:require('../assets/picture/道德模范/道德模范-马旭.jpg'),name:'马旭',animate:'box-slide1'},
              {url:require('../assets/picture/道德模范/道德模范-曲建武.jpg'),name:'曲建武',animate:'box-slide2'},
              {url:require('../assets/picture/道德模范/道德模范-王书茂.jpg'),name:'王书茂',animate:'box-slide3'},
              {url:require('../assets/picture/道德模范/道德模范-王红心.jpg'),name:'王红心',animate:'box-slide4'}
            ],
            reform_list:[
              {url:require('../assets/picture/改革先锋/改革-马云.jpg'),name:'马云',animate:'box-slide1'},
              {url:require('../assets/picture/改革先锋/改革-马化腾.jpg'),name:'马化腾',animate:'box-slide2'},
              {url:require('../assets/picture/改革先锋/改革-柳传志.jpg'),name:'柳传志',animate:'box-slide3'},
              {url:require('../assets/picture/改革先锋/改革-景海鹏.jpg'),name:'景海鹏',animate:'box-slide4'},
              {url:require('../assets/picture/改革先锋/改革-李彦宏.jpg'),name:'李彦宏',animate:'box-slide1'},
              {url:require('../assets/picture/改革先锋/改革-李雪健.jpg'),name:'李雪健',animate:'box-slide2'},
              {url:require('../assets/picture/改革先锋/改革-许海峰.jpg'),name:'许海峰',animate:'box-slide3'},
              {url:require('../assets/picture/改革先锋/改革-郭明义.jpg'),name:'郭明义',animate:'box-slide4'}
            ]
          }
        },
        methods:{

        },
      mounted() {
          new WOW().init();
      }
    }
</script>

<style scoped>
  .top-banner{
    min-width: 1400px;
    height: 620px;
  }
  .swipper-container{
    height: 100%;
    margin-left: auto;
    margin-right: auto;
    position: relative;
    overflow: hidden;
    list-style: none;
    padding: 0;
    z-index: 1;
  }
  .swipper-wrapper{
    position: relative;
    width: 100%;
    height: 100%;
    z-index: 1;
    display: flex;
    transition-property: transform;
    box-sizing: content-box;
  }
  .main_bg{
    width: 100%;
    height: 100%;
    box-sizing: border-box;
    padding-top: 65px;
    background: url("../assets/picture/interview_bg.jpg") no-repeat bottom;
    background-size: cover;
  }
  .bg_cover{
    position: absolute;
    width: 100%;
    height: 100%;
    background: rgba(0,0,0,0.6);
  }
  .content_container{
    position: relative;
    height: 100%;
    width: 1200px;
    margin: 0 auto;
    min-width: 1200px;
  }
  .content-title{
    padding: 144px 0 30px;
    font-size: 50px;
    font-weight: 500;
    color: #ffffff;
    text-shadow: 0 2px 9px rgba(0, 0, 0, 0.2);
    text-align: center;
  }
  .content-title span{
    letter-spacing: 60px;
  }
  .vice-title{
    text-align: center;
    font-size: 30px;
    font-weight: 400;
    color: #ffffff;
    text-shadow: 0 2px 9px rgba(0, 0, 0, 0.2);
    padding: 90px 0 24px;
  }
  .items-body{
    width: 100%;
    min-width: 1400px;
    padding: 60px 0;
    overflow: hidden;
  }
  .main-wrap{
    width: 1200px;
    margin: 0 auto;
    position: relative;
    min-width: 1200px;
  }
  .main-title{
    font-size: 36px;
    text-align: center;
    font-weight: bold;
    line-height: 1.4em;
  }
  .main-content{
    width: 100%;
    height: auto;
    margin-top: 60px;
  }
  .main-content ul{
    list-style: none;
    padding: 10px 5px;
  }
  .main-content ul li{
    width: 280px;
    height: 320px;
    box-shadow: 0 0 10px rgba(0,0,0, 0.5);
    float: left;
    margin-left: 16px;
    margin-bottom: 10px;
    border-radius: 4px;
  }
  .main-content ul li img{
    width: 100%;
    height: 100%;
    border-radius: 4px;
  }
  .img-box{
    position: relative;
    width: 100%;
    height: 100%;
    background: #e7e7e7;
  }
  .hover-element{
    opacity: 1;
    width: 100%;
    height: 100%;
    position: absolute;
    top: 0;
    left: 0;
    background: rgba(14,22,32,0.5);
    transition: all .4s;
    cursor: pointer;
  }
  .hover-element:hover{
    opacity: 0;
  }
  .info-box{
    top: 50%;
    text-align: center;
    position: relative;
    transform: translateY(-50%);
  }
  .in-title-text{

  }
  .in-title-text span{
    color: rgba(255, 255, 255, 0.85);
    position: relative;
    font-size: 20px;
    line-height: 28px;
    width: 100%;
    padding: 0 41px;
    box-sizing: border-box;
    overflow: hidden;
    text-overflow: ellipsis;
  }
</style>

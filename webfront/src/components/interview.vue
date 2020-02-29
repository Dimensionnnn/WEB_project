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
              <li @click="medal_people_click(index)">
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
        <p class="main-title" style="color: #cc2a1d">部分全国改革先锋</p>
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
          partynav,
        },
        data(){
          return {
            medal_list:[],
            moral_list:[],
            reform_list:[]
          }
        },
        methods:{
          medal_people_click:function (index) {
            let new_rul = this.$router.resolve({
              path:'/interview/detail',
              query:{index:index, type:1}
            });
            window.open(new_rul.href)
          }
        },
      mounted() {
          new WOW().init();
      },
      created() {
          let that = this;
          this.$axios.post('api/older').then(function (res) {
            let content = res.data.data;
            for (let i=0; i<content.length; i++){
                let dict = {};
                dict['url'] = content[i][0];
                dict['name'] = content[i][1];
                dict['title'] = content[i][2];
                dict['content'] = content[i][3];
                dict['animate'] = (i+1)%4;
                if (content[i][4] === 1){
                  that.medal_list.push(dict)
                }
                else if (content[i][4] === 2){
                  that.moral_list.push(dict)
                }
                else{
                  that.reform_list.push(dict)
                }
            }
          })
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
    background: url("/static/picture/interview_bg.jpg") no-repeat bottom;
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

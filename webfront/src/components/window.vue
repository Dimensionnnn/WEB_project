<template>
    <div>
      <partynav></partynav>
      <div class="main-content">
        <div class="img-background">
          <div class="background-title">
            <div class="title-box">
              <img src="/static/picture/window-title.png">
            </div>
          </div>
        </div>
        <div class="shyk">
          <div class="main-title">
            <div class="main-title-max">
              <span>主题党日</span>
            </div>
            <div class="main-title-small">
              <p>集中学习，相互交流，共同进步</p>
            </div>
            <div class="ztdk">
              <el-row>
                <el-col :span="10">
                  <div class="main-content-box wow fadeInDown">
                    <span>{{ztdkTitle}}</span>
                    <p>{{ztdkContent}}</p>
                  </div>
                </el-col>
                <el-col :span="14">
                  <div class="main-img-box">
                    <ul>
                      <div v-for="(item,index) in ztdkImg" :key="index">
                        <li>
                          <img v-bind:src="item.url" class="wow fadeInDown">
                        </li>
                      </div>
                    </ul>
                  </div>
                </el-col>
              </el-row>
              <div class="ztdk-button">
                <a href="#" class="button">了解更多</a>
              </div>
            </div>
            <div class="ztdr">
              <el-row>
                <el-col :span="14">
                  <div class="main-img-box wow fadeInDown">
                    <ul>
                      <div v-for="(item,index) in ztdrImg" :key="index">
                        <li>
                          <img v-bind:src="item.url">
                        </li>
                      </div>
                    </ul>
                  </div>
                </el-col>
                <el-col :span="10">
                  <div class="main-content-box wow fadeInDown">
                    <span>{{ztdrTitle}}</span>
                    <p>{{ztdrContent}}</p>
                  </div>
                </el-col>
              </el-row>
              <div class="ztdk-button">
                <a href="#" class="button">了解更多</a>
              </div>
            </div>
          </div>
        </div>
        <div class="mzsh">
          <div class="main-title">
            <div class="main-title-max">
              <span>民主生活会</span>
            </div>
            <div class="main-title-small">
              <p>统一思想、明确目标、凝聚力量</p>
            </div>
            <div class="ztdk">
              <el-row>
                <el-col :span="10">
                  <div class="main-content-box wow fadeInDown">
                    <span>{{mzshTitle}}</span>
                    <p>{{mzshContent}}</p>
                  </div>
                </el-col>
                <el-col :span="14">
                  <div class="main-img-box wow fadeInDown">
                    <ul>
                      <div v-for="(item,index) in mzshImg" :key="index">
                        <li>
                          <img v-bind:src="item.url">
                        </li>
                      </div>
                    </ul>
                  </div>
                </el-col>
              </el-row>
              </div><div class="ztdk-button">
                <a href="#" class="button">了解更多</a>
              </div>
          </div>
        </div>
        <div class="zzsh">
          <div class="main-title">
            <div class="main-title-max">
              <span style="color: #df3737">组织生活会</span>
            </div>
            <div class="main-title-small">
              <p style="color: #df3737">增进交流，加强监督，增强活力</p>
            </div>
            <div class="zzsh-title-box wow fadeInDown">
              <span>{{zzshTitle1}}</span>
              <p>{{zzshContent1}}</p>
            </div>
            <div class="zzsh-img-box wow fadeInDown">
              <el-row>
                <div v-for="(item,index) in zzsh1Img" :key="index">
                  <el-col :span="8">
                    <div class="zzsh-card">
                      <img v-bind:src="item.url">
                      <div class="zzsh-card-text">
                        <span>{{item.content}}</span>
                        <p>{{item.subject}}</p>
                      </div>
                    </div>
                  </el-col>
                </div>
              </el-row>
            </div>
            <div class="ztdk-button">
              <a href="#" class="button">了解更多</a>
            </div>
            <div class="zzsh-meeting">
              <el-row>
                <el-col :span="10">
                  <div class="main-content-box wow fadeInDown">
                    <span>{{zzshTitle2}}</span>
                    <p>{{zzshContent2}}</p>
                  </div>
                </el-col>
                <el-col :span="14">
                  <div class="main-img-box wow fadeInDown">
                    <ul>
                      <div v-for="(item,index) in zzsh2Img" :key="index">
                        <li>
                          <img v-bind:src="item.url">
                        </li>
                      </div>
                    </ul>
                  </div>
                </el-col>
              </el-row>
              <div class="ztdk-button">
                <a href="#" class="button">了解更多</a>
              </div>
            </div>
          </div>
        </div>
        <div class="congress">
          <div class="main-title">
            <div class="main-title-max">
              <span style="color: #fff">三会一课</span>
            </div>
            <div class="main-title-small">
              <p style="color: #fff">党支部党员大会/党支部委员会会议/党小组会议/党课</p>
            </div>
            <div class="congress-meeting">
              <el-row>
                <el-col :span="10">
                  <div class="main-content-box wow fadeInDown">
                    <span style="color: #fff">{{congressTitle}}</span>
                    <p style="color: #fff">{{congressContent}}</p>
                  </div>
                </el-col>
                <el-col :span="14">
                  <div class="main-img-box wow fadeInDown">
                    <ul>
                      <div v-for="(item,index) in congressImg" :key="index">
                        <li>
                          <img v-bind:src="item.url">
                        </li>
                      </div>
                    </ul>
                  </div>
                </el-col>
              </el-row>
              <div class="ztdk-button">
                <a href="#" class="button-new" style="color: #fff">了解更多</a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
</template>

<script>
  import partynav from '@/components/partynav.vue'
  import {WOW} from '../assets/js/wow.min.js'
    export default {
        name: "window",
        components:{
          partynav
        },
        data(){
          return {
            ztdkTitle:'参观红色景点，牢固理想信念',
            ztdkContent:'重温党的光辉历程，讴歌党的丰功伟绩，教育引导全体干部和广大党员进一步坚定理想信念，强化党性锻炼，补足精神之钙',
            ztdkImg:[],
            ztdrTitle:'相互交流，思想碰撞，共同进步',
            ztdrContent:'主题党日是党性锤炼的“大熔炉”。在严肃的党内生活中，党员不断实现自我净化、自我完善、自我革新、自我提高。',
            ztdrImg:[],
            mzshTitle:'广泛讨论，凝聚共识',
            mzshContent:'民主生活会意义重大，在于它不断正风肃纪、永葆党内生机活力的重要方式。要以民主生活会为契机，直面问题，' +
              '深刻自省，补齐短板，做人民群众真正满意的共产党员',
            mzshImg:[],
            zzshTitle1:'深入基层，温暖他人',
            zzshContent1:'深入社会，了解社会，在实践中接受锻炼与提高，培养艰苦奋斗的品质，将理论知识内化为自身的思想认识进而提高理论水平',
            zzsh1Img:[],
            zzshTitle2:'开会交流，永葆党的青春性与纯洁性',
            zzshContent2:'开展好党的组织生活，就可以使每一个共产党员，自觉地贯彻执行党的路线、方针和政策。同时，也可以通过组织生活，使党员经常检查和克服各种非无产阶级思想，坚定共产主义信念',
            zzsh2Img:[],
            congressTitle:'不忘初心，牢记使命，永葆本色',
            congressContent:'三会一课在健全党的组织生活，严格党员教育管理监督，加强基层组织建设，实现党的目标任务等方面' +
              '发挥着不可替代的重要作用。坚持“三会一课”制度是严肃党内政治生活的重要内容和载体，是全面从严治党的必然要求。',
            congressImg:[]
          }
        },
      methods:{
          init_window:function () {
            let that = this;
            this.$axios.post('api/window').then(function (res) {
               let content = res.data.data;
               for (let i=0; i<content.length; i++){
                 let dict = {};
                 dict['url'] = content[i][0];
                 dict['content'] = content[i][1];
                 if (content[i][2] === 1){
                   that.ztdkImg.push(dict)
                 }
                 else if (content[i][2] === 2){
                   that.ztdrImg.push(dict)
                 }
                 else if (content[i][2] === 3){
                   that.mzshImg.push(dict)
                 }
                 else if (content[i][2] === 4){
                   that.zzsh1Img.push(dict)
                 }
                 else if (content[i][2] === 5){
                   that.zzsh2Img.push(dict)
                 }
                 else{
                   that.congressImg.push(dict)
                 }
               }
            })
          }
      },
      mounted() {
          new WOW().init();
      },
      created() {
          this.init_window()
      }
    }
</script>

<style scoped>
  .main-content{
    position: relative;
    width: 100%;
    top: 64px;
  }
  .img-background{
    background: url("/static/picture/group.jpg") no-repeat;
    background-size: cover;
    width: 100%;
    height: 750px;
    background-position: center 0;
    min-width: 1400px;
    position: relative;
  }
  .background-title{
    width: 1200px;
    margin: auto;
    height: 100%;
  }
  .title-box{
    position: relative;
    width: 742px;
    margin: auto;
    animation: title 1.5s forwards;
    animation-delay: .5s;
    opacity: 0;
  }
  .title-box img{
    width: 100%;
    height: 100%;
  }
  @keyframes title {
    0%{top: 100px;opacity: 0}
    100%{top: 0;opacity: 1}
  }
  @-webkit-keyframes title {
    0%{top: 100px;opacity: 0}
    100%{top: 0;opacity: 1}
  }
  .shyk{
    min-width: 1400px;
    width: 100%;
    height: auto;
    background: #efefef;
    padding-top: 1px;
  }
  .main-title{
    width: 1200px;
    padding-right: 15px;
    padding-left: 15px;
    margin-right: auto;
    margin-left: auto;
  }
  .main-title-max{
    text-align: center;
    padding: 60px 0 20px 0;
    margin-top: 20px;
    margin-bottom: 10px;
  }
  .main-title-max span{
    color: #424242;
    font-size: 54px;
  }
  .main-title-small{
    text-align: center;
    padding: 0 0 20px 0;
  }
  .main-title-small p{
    font-size: 30px;
    color: #424242;
  }
  .ztdk{
    padding-top: 60px;
    overflow: hidden;
    margin: 0;
    padding: 0;
    outline: 0;
    background: transparent;
    -webkit-font-smoothing: antialiased;
  }
  .main-content-box{
    padding: 30px 50px;
    margin-top: 45px;
    text-align: left;
  }
  .main-content-box span{
    color: #424242;
    font-size: 30px;
  }
  .main-content-box p{
    line-height: 30px;
    color: #424242;
    font-size: 20px;
    padding-top: 20px;
  }
  .main-img-box{
    text-align: right;
  }
  .main-img-box ul{
    width: 100%;
    padding: 10px 5px;
  }
  .main-img-box ul li{
    width: 100%;
    list-style: none;
  }
  .main-img-box ul li img{
    width: 310px;
    height: 200px;
    float: left;
    margin-left: 10px;
    margin-bottom: 10px;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0,0,0, 0.5);
  }
  .ztdk-button{
    padding-top: 40px;
    text-align: center;
    padding-bottom: 40px;
  }
  .button{
    text-decoration: none;
    display: inline-block;
    width: auto;
    min-width: 60px;
    padding: 0 50px;
    height: 52px;
    line-height: 52px;
    margin: 0 20px 0 20px;
    text-align: center;
    font-size: 18px;
    color: #FFF;
    background-color: #cb1c1d;
    box-shadow: 0 6px 12px 0 rgba(0,0,0,.1);
    transition: all .8s ease;
  }
  .button:hover{
    color: #FFF;
    background-color: #ea2626;
    box-shadow: 1px 3px 8px 0 rgba(234, 38, 38, 0.3)
  }
  .button-new{
    text-decoration: none;
    display: inline-block;
    width: auto;
    min-width: 60px;
    padding: 0 50px;
    height: 52px;
    line-height: 52px;
    text-align: center;
    font-size: 16px;
    color: #fff;
    background-color: transparent;
    border: 1px solid #fff;
    box-shadow: 0 6px 12px 0 rgba(0,0,0,.1);
    transition: all .8s ease;
  }
  .button-new:hover{
    background-color: #f9a709;
    border: 1px solid #f9a709;
  }
  .ztdr{
    padding-top: 140px;
    overflow: hidden;
  }
  .mzsh{
    min-width: 1400px;
    width: 100%;
    height: auto;
    background: #fff;
    padding-top: 1px;
  }
  .zzsh{
    min-width: 1400px;
    height: auto;
    padding-top: 20px;
    background: rgba(255,96,0,0.1);
  }
  .zzsh-title-box{
    padding-top: 40px;
    text-align: center;
    padding-bottom: 40px;
  }
  .zzsh-title-box span{
    font-size: 40px;
    color: #df3737;
    padding-bottom: 20px;
  }
  .zzsh-title-box p{
    padding-top: 25px;
    font-size: 24px;
    color: #df3737;
    padding-bottom: 20px;
  }
  .zzsh-card{
    width: 90%;
    height: auto;
    padding: 10px;
  }
  .zzsh-card-text{
    text-align: center;
    padding: 5px;
    margin-top: 10px;
  }
  .zzsh-card img{
    width: 100%;
    height: 200px;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0,0,0, 0.5);
  }
  .zzsh-card span{
    color: #df3737;
    font-size: 25px;
    line-height: 25px;
    letter-spacing: 3px;
  }
  .zzsh-card p{
    color: #df3737;
    font-size: 18px;
  }
  .zzsh-meeting{
    padding-top: 140px;
    overflow: hidden;
  }
  .congress{
    min-width: 1400px;
    width: 100%;
    height: auto;
    background: #e34d41;
    padding-top: 1px;
  }
  .congress-meeting{
    padding-top: 60px;
    overflow: hidden;
  }
</style>

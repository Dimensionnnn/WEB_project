<template>
  <div style="background: #f4f4f4;min-width: 1400px">
    <partynav></partynav>
    <div class="id-banner">
      <div class="id-banner-box">
        <div class="id-banner-rap">
          <img class="backgroud-picture" src="/static/picture/party-title.png">
        </div>
      </div>
    </div>
    <div class="nav-box clear">
      <div class="nav-box-list clear">
        <ul>
          <li class="li01">
            <a href="#">政治建设</a>
          </li>
          <li class="li02">
            <a href="#">组织建设</a>
          </li>
          <li class="li03">
            <a href="#">纪律建设</a>
          </li>
          <li class="li04">
            <a href="#">思想建设</a>
          </li>
          <li class="list05">
            <a href="#">作风建设</a>
          </li>
           <li class="list06">
            <a href="#">制度建设</a>
          </li>
        </ul>
      </div>
    </div>
    <div class="id-box">
      <div class="id-item">
        <div class="id-item-1">
          <div class="focus-box">
            <el-carousel :interval="3000" :height="316+'px'" indicator-position="none">
              <el-carousel-item v-for="(item,index) in banner" :key="index">
                <img v-bind:src="item.url" class="banner-img">
                <div class="nav-bg">
                   <div class="nav-bg-txt">
                      <div class="nav-bg-txt-box">
                        <a href="#">{{item.title}}</a>
                      </div>
                    </div>
                </div>
              </el-carousel-item>
            </el-carousel>
          </div>
          <div class="focus-nav">
            <a class="list1" href="#">
              <i></i>
              <span>图片新闻</span>
            </a>
            <a class="list2" href="#">
              <i></i>
              <span>视频新闻</span>
            </a>
          </div>
        </div>
        <div class="id-item-notice">
          <div class="tab-hd">
            <div class="tab-nav">
              <ul class="tab-nav-ul">
                <li class="list1" @mouseover="JudgeOver('1')"><a href="#">党建要闻</a></li>
                <li class="list2" @mouseover="JudgeOver('2')"><a href="#">评论观点</a></li>
                <li class="list3" @mouseover="JudgeOver('3')"><a href="#">干部论坛</a></li>
                <li class="list4" @mouseover="JudgeOver('4')"><a href="#">各地动态</a></li>
                <li class="list5" @mouseover="JudgeOver('5')"><a href="#">交流体会</a></li>
              </ul>
            </div>
          </div>
          <div class="tab-bd">
            <div class="tab-pal" id="list1">
              <div class="id-list">
                <ul>
                  <div v-for="(item,index) in news[0]" :key="index" style="margin-left: -40px">
                    <li>{{item.title}}</li>
                  </div>
                </ul>
              </div>
            </div>
            <div class="tab-pal" id="list2">
              <div class="id-list">
                <ul>
                  <div v-for="(item,index) in news[1]" :key="index" style="margin-left: -40px">
                    <li>{{item.title}}</li>
                  </div>
                </ul>
              </div>
            </div>
            <div class="tab-pal" id="list3">
              <div class="id-list">
                <ul>
                  <div v-for="(item,index) in news[2]" :key="index" style="margin-left: -40px">
                    <li>{{item.title}}</li>
                  </div>
                </ul>
              </div>
            </div>
            <div class="tab-pal" id="list4">
              <div class="id-list">
                <ul>
                  <div v-for="(item,index) in news[3]" :key="index" style="margin-left: -40px">
                    <li>{{item.title}}</li>
                  </div>
                </ul>
              </div>
            </div>
            <div class="tab-pal" id="list5">
              <div class="id-list">
                <ul>
                  <div v-for="(item,index) in news[4]" :key="index" style="margin-left: -40px">
                    <li>{{item.title}}</li>
                  </div>
                </ul>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="tb-focus">
        <div class="bd" @click="Transfer"></div>
      </div>
      <div class="notice-main">
        <div class="notice-title">
          <div class="notice-title-box border1" @mouseover="noticeOver('1')"><span>优秀党员</span></div>
          <div class="notice-title-box border2" @mouseover="noticeOver('2')"><span>风采展示</span></div>
          <div class="notice-title-box border3" @mouseover="noticeOver('3')"><span>先进事迹</span></div>
          <div class="notice-title-box border4" style="border-right: 0" @mouseover="noticeOver('4')"><span>未来展望</span></div>
        </div>
        <div class="notice-title-body1" style="display: none">
          <div v-for="(item, index) in partymember" :key="index" class="img-entry">
            <div>
              <a href="#">
                <img class="img-entry-img" v-bind:src="item.url">
                <div class="shadow">
                  <div class="shadow-title">{{item.title}}</div>
                </div>
              </a>
            </div>
          </div>
        </div>
        <div class="notice-title-body2" style="display: none">
          <div class="body-pal">
            <div class="id-rcgz">
              <div class="id-rcgz-title">
                <i></i>
                <a href="#">模范党支部风采</a>
              </div>
              <div class="id-rcgz-ul">
                <div v-for="(item,index) in banner" :key="index">
                  <div class="id-rcgz-card">
                    <img v-bind:src="item.url">
                    <div class="title"><span>{{item.title}}</span></div>
                    <div class="content">{{item.content}}</div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="notice-title-body3" style="display: none">
          <div class="body-pal">
            <div class="id-xjsj">
              <ul>
                <div v-for="(item,index) in xinajinshiji" :key="index">
                  <li>{{item.title}}</li>
                </div>
              </ul>
            </div>
            <div class="id-activity">
              <div class="activity-title">
                <i></i>
                <span>特别活动推荐</span>
              </div>
              <div v-for="(item,index) in xianjinbanner" :key="index">
                <div class="activity-banner">
                 <div class="activity-banner-box">
                    <img v-bind:src="item.url">
                    <div class="activity-banner-cover">
                      <div class="info-box">
                        <div class="info-title">
                          <span>{{item.content}}</span>
                        </div>
                      </div>
                    </div>
                 </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="notice-title-body4" style="display: none">
          <div class="body-pal">
            <div class="id-wlzw">
              <div class="id-wlzw-title">
                <i></i>
                <span>留言精选</span>
              </div>
              <div class="id-wlzw-list">
                <ul>
                  <div v-for="(item,index) in comment" :key="index">
                    <li>[ {{item.name}} ]: {{item.content}}</li>
                  </div>
                </ul>
              </div>
            </div>
            <div class="id-wlzw-comment">
              <div class="id-wlzw-comment-title">
                <i></i>
                <span>我要发表展望</span>
              </div>
              <div class="id-wlzw-comment-content">
                <el-input type="textarea" :autosize="{ minRows:4 }" placeholder="我要发表评论" v-model="textarea"></el-input>
              </div>
              <div class="id-wlzw-button">
                <el-button type="primary" style="float: right">提交评论</el-button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
    import partynav from '@/components/partynav.vue'
    export default {
      name: "ModelParty",
      components:{
        partynav
      },
      data(){
        return {
          textarea:'',
          banner:[],
          news:[[],[],[],[],[]],
          partymember:[],
          xinajinshiji:[],
          xianjinbanner:[
            {title:'学习路上',url:'/static/picture/activity_banner1.png',content:'习总书记系列讲话'},
            {title:'学习有声',url:'/static/picture/activity_banner2.png',content:'习总书记经典语录'},
            {title:'学习金句',url:'/static/picture/activity_banner3.png',content:'习总书记重要论述'}
          ],
          comment:[]
        }
      },
      methods:{
        Transfer:function(){
          window.location.href = 'http://chuxin.people.cn/GB/index.html'
        },
        JudgeOver:function (e) {
          let ul_list = $('.tab-nav-ul').children('li');
          for (let i=0; i<ul_list.length; i++){
            if (i+1 !== parseInt(e)){
              $(".tab-nav-ul .list"+(i+1).toString()).removeClass('on');
              for (let j=0; j<ul_list.length; j++){
                if (j+1 !== parseInt(e)){
                  $("#list"+(j+1).toString()).css('display','none')
                }
                else{
                  $("#list"+(j+1).toString()).css('display', 'block')
                }
              }
            }
          }
          $(".tab-nav-ul .list"+e).addClass('on')
        },
        noticeOver:function(e){
          if (e === '1'){
            $(".border"+e).css('background','#0477c5');
            $(".notice-title-body"+e).css('display','block')
          }
          else if (e === '2'){
            $(".border"+e).css('background','#f86b6b');
            $(".notice-title-body"+e).css('display','block')
          }
          else if (e === '3'){
            $(".border"+e).css('background','#46cb5f');
            $(".notice-title-body"+e).css('display','block')
          }
          else{
            $(".border"+e).css('background','#f9da2e');
            $(".notice-title-body"+e).css('display','block')
          }
          for (let i=1; i<=4;i++){
            if (i !== parseInt(e)){
              $(".border"+i.toString()).css('background','#efefef');
              $(".border"+i.toString()+" span").css({'color':'#888888','font-weight':'normal'});
              $(".notice-title-body"+i.toString()).css('display','none')
            }
          }
          $(".border"+e+" span").css({'color':'#fff','font-weight':'bold'})
        },
        initClass:function () {
          $(".tab-nav-ul .list1").addClass('on');
          $("#list1").css('display','block');
          $(".notice-title-body1").css('display','block');
          $(".border1").css('background','#0477c5');
          $(".border1 span").css({'color':'#fff','font-weight':'bold'})
        },
        init_Model_Party:function () {
          let that = this;
          this.$axios.post('api/org').then(function (res) {
            let content = res.data.data;
            for (let i=0; i<content.length; i++){
              let dict = {};
              dict['url'] = content[i][0];
              dict['title'] = content[i][1];
              dict['content'] = content[i][2];
              that.banner.push(dict)
            }
          })
        },
        init_News_Title:function () {
          let that = this;
          this.$axios.post('api/orgnews').then(function (res) {
            let content = res.data.data;
            for (let i=0; i<content.length; i++){
              if (content[i][1] === 1){
                let dict = {};
                dict['title'] = '> '+content[i][0];
                that.news[0].push(dict)
              }
              else if (content[i][1] === 2){
                let dict = {};
                dict['title'] = '> '+content[i][0];
                that.news[1].push(dict)
              }
              else if (content[i][1] === 3){
                let dict = {};
                dict['title'] = '> '+content[i][0];
                that.news[2].push(dict)
              }
              else if (content[i][1] === 4){
                let dict = {};
                dict['title'] = '> '+content[i][0];
                that.news[3].push(dict)
              }
              else{
                let dict = {};
                dict['title'] = '> '+content[i][0];
                that.news[4].push(dict)
              }
            }
          })
        },
        init_Partymember:function () {
          let that = this;
          this.$axios.post('api/partymember').then(function (res) {
            let content = res.data.data;
            for (let i=0; i<content.length; i++){
              let dict = {};
              dict['url'] = content[i][0];
              dict['title'] = content[i][1];
              that.partymember.push(dict)
            }
          })
        },
        init_Good_Thing:function () {
          let that = this;
          this.$axios.post('api/goodthing').then(function (res) {
            let content = res.data.data;
            for (let i=0; i<content.length; i++){
              let dict = {};
              dict['title'] = content[i][0];
              that.xinajinshiji.push(dict)
            }
          })
        },
        init_comment:function () {
          let that = this;
          this.$axios.post('api/party_comment').then(function (res) {
            let content = res.data.data;
            for (let i=0; i<content.length; i++){
              let dict = {};
              dict['name'] = content[i][0];
              dict['content'] = content[i][1];
              that.comment.push(dict)
            }
          })
        }
      },
      mounted() {
        this.initClass()
      },
      created() {
        this.init_Model_Party();
        this.init_News_Title();
        this.init_Partymember();
        this.init_Good_Thing();
        this.init_comment()
      }
    }
</script>

<style scoped>
  .id-banner{
    margin-top: 65px;
    position: relative;
    z-index: 1;
    width: 100%;
    height: 250px;
    background: url("/static/picture/party_background.jpg") no-repeat;
    background-size: 100% 100%;
  }
  .id-banner-box{
    z-index: 100;
    position: absolute;
    left: 0;
    top: 0;
    height: 250px;
    width: 100%;
  }
  .id-banner-rap{
    overflow: hidden;
    height: 223px;
    width: 1200px;
    margin: auto;
  }
  .backgroud-picture {
    width: 680px;
    position: relative;
    float: left;
    top: -92px;
    left: -82px;
  }
  .nav-box{
    margin-top: -18px;
    height: 60px;
    background: #66b1ff;
    z-index: 99;
  }
  .nav-box-list{
    width: 1200px;
    margin: auto;
    height: 60px;
  }
  .nav-box-list ul li{
    float: left;
    list-style: none;
  }
  .nav-box-list ul li a{
    width: 192px;
    display: block;
    line-height: 60px;
    color: #fff;
    font-size: 18px;
    text-align: center;
    text-decoration: none;
    cursor: pointer;
  }
  .nav-box-list ul li a:hover{
    background: linear-gradient(to bottom, #3a8ee6, #8cc5ff);
  }
  .id-box{
    width: 1200px;
    margin: auto;
    overflow: hidden;
    padding-top: 20px;
    padding-bottom: 40px;
  }
  .id-item{
    padding: 15px;
    background: #fff;
    overflow: hidden;
  }
  .id-item-1{
    float: left;
    width: 480px;
  }
  .focus-box{
    position: relative;
    width: 480px;
    height: 316px;
    overflow: hidden;
    text-align: left;
    background: white;
  }
  .banner-img{
    width: 100%;
    height: 316px;
  }
  .focus-nav{
    background: #efefef;
    margin-top: 8px;
    overflow: hidden;
  }
  .focus-nav a{
    margin-left: 85px;
    float: left;
    height: 50px;
    text-decoration: none;
  }
  .focus-nav .list1 i{
    background: url("/static/picture/picture.png") no-repeat center center;
    background-size: cover;
    width: 26px;
    height: 26px;
    float: left;
    margin-top: 13px;
  }
  .focus-nav .list2 i{
    background: url("/static/picture/video.png") no-repeat center center;
    background-size: cover;
    width: 26px;
    height: 26px;
    float: left;
    margin-top: 13px;
  }
  .focus-nav a span{
    float: left;
    font-size: 16px;
    color: #0477c5;
    line-height: 50px;
    margin-left: 14px;
  }
  .nav-bg{
    position: absolute;
    bottom: 0;
    z-index: 99;
    height: 40px;
    width: 100%;
    background: rgba(0,0,0,0.5);
    overflow: hidden;
  }
  .nav-bg-txt{
    position: absolute;
    bottom: 0;
    z-index: 100;
    height: 40px;
    width: 100%;
    overflow: hidden;
  }
  .nav-bg-txt-box{
    height: 40px;
    line-height: 40px;
    position: absolute;
    width: 100%;
    text-align: center;
  }
  .nav-bg-txt a{
    display: block;
    color: white;
    font-size: 16px;
    text-decoration: none;
    width: 100%;
  }
  .id-item-notice{
    width: 666px;
    float: right;
    overflow: hidden;
  }
  .tab-hd{
    height: 50px;
    overflow: hidden;
    background: #f4f4f4;
  }
  .tab-nav ul{
    margin: 0;
    padding: 0;
  }
  .tab-nav ul li{
    float: left;
    width: 20%;
    list-style: none;
  }
  .tab-nav ul li a{
    display: block;
    text-align: center;
    line-height: 50px;
    font-size: 18px;
    color: #333;
    text-decoration: none;
  }
  .tab-nav ul li.on a{
    color: #fff;
    background: #0477c5;
    font-weight: bold;
    transition: all .3s;
  }
  .tab-bd{
    overflow: hidden;
  }
  .tab-pal{
    height: 326px;
    overflow: hidden;
    display: none;
  }
  .tab-pal ul li{
    margin-bottom: 2px;
    background: #f4f4f4;
    width: 100%;
    height: 30px;
    padding: 15px 25px;
    list-style: none;
    cursor: pointer;
  }
  .tab-pal ul li:hover{
    background: #0477c5;
    color: white;
  }
  .tb-focus{
    background: #fff;
    width: 1200px;
    height: 110px;
    position: relative;
    overflow: hidden;
    margin-top: 16px;
  }
  .bd{
    position: relative;
    width: 1200px;
    height: 110px;
    background: url("/static/picture/party-banner.jpg") no-repeat center center;
    background-size: cover;
    cursor: pointer;
  }
  .notice-main{
    width: 100%;
    overflow: hidden;
    margin-top: 14px;
  }
  .notice-title{
    padding-top: 10px;
    background: #fff;
    width: 100%;
    height: 60px;
    padding-bottom: 10px;
  }
  .notice-title-box{
    width: 299px;
    height: 100%;
    float: left;
    text-align: center;
    position: relative;
    background: #efefef;
    border-right: 1px solid #cdcdcd;
    transition: all .3s;
    cursor: pointer;
  }
  .border1{
    border-bottom: 6px solid #0477c5;
  }
  .border2{
    border-bottom: 6px solid #f86b6b;
  }
  .border3{
    border-bottom: 6px solid #46cb5f;
  }
  .border4{
    border-bottom: 6px solid #f9da2e;
  }
  .notice-title-box span{
    position: relative;
    line-height: 64px;
    font-size: 18px;
    color: #888888;
  }
  .notice-title-body1{
    padding-left: 10px;
    padding-right: 10px;
    padding-top: 20px;
    width: 1200px;
    height: 400px;
    background: #fff;
  }
  .notice-title-body2{
    float: left;
    width: 1200px;
    height: auto;
  }
  .body-pal{
    overflow: hidden;
    height: auto;
  }
  .id-rcgz{
    float: left;
    width: 100%;
    height: auto;
    background: #fff;
    padding: 15px;
  }
  .id-rcgz-title{
    overflow: hidden;
    height: 40px;
  }
  .id-rcgz-title i{
    float: left;
    width: 6px;
    height: 30px;
    background: #0477c5;
  }
  .id-rcgz-title a{
    font-weight: bold;
    float: left;
    margin-left: 26px;
    line-height: 30px;
    color: #343434;
    font-size: 18px;
    text-decoration: none;
  }
  .id-rcgz-ul{
    overflow: hidden;
    margin-top: 5px;
  }
  .id-rcgz-card{
    float: left;
    margin-bottom: 10px;
    margin-right: 20px;
    width: 265px;
    height: auto;
    border-radius: 4px;
    border: 1px #d1d1d1 solid;
    padding: 5px;
    cursor: pointer;
  }
  .id-rcgz-card:hover{
    box-shadow: 10px 10px 10px rgba(206,0,0,0.5);
  }
  .id-rcgz-card img{
    width: 100%;
    height: 200px;
  }
  .id-rcgz-card .title{
    margin-top: 5px;
    color: #ce0000;
    font-size: 18px;
    font-weight: bold;
  }
  .id-rcgz-card .content{
    margin-top: 10px;
  }
  .img-entry{
    float: left;
    width: 280px;
    height: 160px;
    border-radius: 4px;
    margin-right: 20px;
    overflow: hidden;
    margin-top: 10px;
  }
  .img-entry:last-child{
    float: left;
    width: 280px;
    height: 160px;
    border-radius: 4px;
    margin-right: 0;
    overflow: hidden;
  }
  .img-entry a{
    position: relative;
    width: 100%;
    height: 100%;
    display: block;
  }
  .img-entry-img{
    width: 100%;
    height: 100%;
  }
  .shadow{
    position: absolute;
    content: "";
    width: 100%;
    height: 100%;
    border-radius: 4px;
    background: rgba(0,0,0,0.5);
    top: 0;
    left: 0;
    transition: all 0.2s ease-out;
    cursor: pointer;
  }
  .shadow-title{
    width: 100%;
    text-align: center;
    position: relative;
    height: 25px;
    line-height: 25px;
    font-size: 18px;
    color: #ffffff;
    letter-spacing: 1.14px;
    top: 70px;
    cursor: pointer;
  }
  .shadow:hover{
    opacity: 0;
  }
  .notice-title-body3{
    width: 1200px;
    height: auto;
  }
  .id-xjsj{
    float: left;
    width: 730px;
    height: auto;
    background: #fff;
    padding: 10px;
  }
  .id-activity{
    width: 400px;
    float: right;
    height: 458px;
    background: #fff;
    padding: 10px 20px;
  }
  .activity-title{
    width: 100%;
    height: 40px;
    overflow: hidden;
  }
  .activity-title i{
    float: left;
    width: 6px;
    height: 30px;
    background: #0477c5;
  }
  .activity-title span{
    float: left;
    margin-left: 26px;
    line-height: 30px;
    color: #333;
    font-size: 18px;
  }
  .activity-banner{
    width: 100%;
    height: 128px;
    margin-bottom: 10px;
  }
  .activity-banner-box{
    position: relative;
    display: block;
    width: 100%;
    height: 100%;
  }
  .activity-banner-cover{
    position: absolute;
    width: 100%;
    height: 100%;
    border-radius: 4px;
    z-index: 2;
    top: 0;
    left: 0;
    background: rgba(0,0,0,0.4);
    opacity: 0;
    transition: all .4s;
    cursor: pointer;
  }
  .activity-banner-cover:hover{
    opacity: 1;
  }
  .info-box{
    top: 50%;
    text-align: center;
    position: relative;
    transform: translateY(-50%);
    -webkit-transform: translateY(-50%);
  }
  .info-title span{
    font-size: 20px;
    line-height: 28px;
    width: 100%;
    padding: 0  41px;
    box-sizing: border-box;
    overflow: hidden;
    text-overflow: ellipsis;
    -webkit-box-orient: vertical;
    color: #fff;
  }
  .activity-banner img{
    width: 100%;
    height: 100%;
    border-radius: 4px;
  }
  .notice-title-body3 ul{
    list-style: none;
  }
  .notice-title-body3 li{
    background: #efefef;
    height: 40px;
    padding: 15px 25px;
    margin-bottom: 1px;
    cursor: pointer;
  }
  .notice-title-body3 li:hover{
    color: white;
    background: #0477c5;
  }
  .notice-title-body4{
    width: 1200px;
    height: auto;
  }
  .id-wlzw{
    width: 700px;
    padding: 10px;
    height: auto;
    float: left;
    background: #fff;
  }
  .id-wlzw-title{
    height: 40px;
    overflow: hidden;
  }
  .id-wlzw-title i{
    float: left;
    width: 6px;
    height: 30px;
    background: #0477c5;
  }
  .id-wlzw-title span{
    float: left;
    margin-left: 26px;
    line-height: 30px;
    color: #333;
    font-size: 18px;
  }
  .id-wlzw-list ul{
    list-style: none;
  }
  .id-wlzw-list ul li{
    width: 80%;
    min-height: 20px;
    padding: 15px 25px;
    border-bottom: #cdcdcd 1px solid;
  }
  .id-wlzw-comment{
    width: 430px;
    float: right;
    background: #fff;
    height: auto;
    padding: 10px;
  }
  .id-wlzw-comment-title{
    height: 40px;
    overflow: hidden;
  }
  .id-wlzw-comment-title i{
    float: left;
    height: 30px;
    width: 6px;
    background: #0477c5;
  }
  .id-wlzw-comment-title span{
    float: left;
    margin-left: 26px;
    line-height: 30px;
    color: #333;
    font-size: 18px;
  }
  .id-wlzw-comment-content{
    width: 100%;
    height: auto;
    margin-top: 10px;
  }
  .id-wlzw-button{
    margin-top: 10px;
    width: 100%;
    height: auto;
  }
</style>

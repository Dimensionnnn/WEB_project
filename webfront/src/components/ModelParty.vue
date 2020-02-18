<template>
  <div style="background: #f4f4f4;min-width: 1400px">
    <partynav></partynav>
    <div class="id-banner">
      <div class="id-banner-box">
        <div class="id-banner-rap">
          <img class="backgroud-picture" src="../assets/picture/party-title.png">
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
          banner:[
            {url:require('../assets/picture/模范党支部/外语学院第三党支部.jpg'),title:'外语学院教工第三党支部',content:'我了才能是那次你收到了磁轭辽宁卫视近年来ID拿出来的时拿出来哪里你是吃了啥南陈路'},
            {url:require('../assets/picture/模范党支部/理学院化学实验中心.jpg'), title:'理学院化学实验中心党支部',content:'课程的是你擦地来收到了年底深V你熟练度呢猥琐男另外你为了你历五年了那算了我你老是'},
            {url:require('../assets/picture/模范党支部/计院智科.jpg'),title:'计算机工程与科学学院智能科学与技术系第一党支部',content:'会查理斯哦长时间hi殴打欧神诺我哦哦我John哦以殴打偶极矩到都欧迪芬京东'},
            {url:require('../assets/picture/模范党支部/机自工训中心.jpg'),title:'机电工程与自动化学院工程训练中心党总支',content:'回款表科技板块hihike开 看固顾客顾客会快不快好看包括和U包括和UK好包括和库顾客'},
            {url:require('../assets/picture/模范党支部/材料学院材料研究所.jpg'),title:'材料科学与工程学院材料研究所党总支',content:'互不开很酷很酷库个课号贵一顾客hi课号根据胡歌蠢花括号固看个可好看法国苦海个看个看看'},
            {url:require('../assets/picture/模范党支部/通信特种光纤.jpg'),title:'通信与信息工程学院特征光纤与光接入网党总支',content:'还客户开会给hi后个u花开花落u9of挺好 返回寄顾客匞就看个开顾客好看顾客活力固课号个了'},
            {url:require('../assets/picture/模范党支部/经济学院金融系.jpg'),title:'经济学院金融系教工党总支',content:'汇款户口课号活力里hi考虑好里活力hi干部科 一里hi空白课号不顾看吧OKhoist不课号了hike户口包括会列表'},
            {url:require('../assets/picture/模范党支部/数码艺术学院.jpg'),title:'数码艺术学院2015级学生党支部',content:'数码艺术学院2015级学生党支部是一支与时俱进、乐于奉献、开拓创新、团结协作的基层党组织，是一个温馨的大家庭。所有党员在学校、学院的人才培养工作中充分发挥先锋模范和战斗堡垒作用'}
          ],
          news:[[{title:'> 中央不忘初心，牢记使命主题教育领导小组印发通知,认真学习贯彻习近平总书记....'},
                  {title:'> 习近平在"不忘初心，牢记使命"大会上的讲话'},
                  {title:'> 习近平：以主题教育为新的起点 持续推动全党不忘初心，牢记使命'},
                  {title:'> 中共中央政治局常务委员会召开会议，习近平主持'},
                  {title:'> 以高质量党建推动国有企业高质量发展'}],
            [{title:'> 评论员观察:全面从严治党，凝聚磅礴伟力'},
              {title:'> 人民日报评论员:发扬斗争精神，用于担当作为'},
              {title:'> 人民日报评论员：强大的政党是在自我革命中锻炼出来的'},
              {title:'> 人民日报评论员:把学习贯彻党的创新理论作为思想武装的重中之重'},
              {title:'> 党建评:永恒课题需要永远解答'}
            ],
            [{title:'> 治理者说:擦亮基层群众的幸福底色'},
              {title:'> 治理之道:把不忘初心，牢记使命作为终身课题'},
              {title:'> 一线思考:扎紧乡村检查监督的“篱笆”'},
              {title:'> 让初心始终闪耀'},
              {title:'> 治理者说:以务实创新激发治理效能'}],
            [{title:'> 湖南省三下乡:将惠民服务送到老乡家门口'},
              {title:'> 山东省淄博市淄川区探索流动党员教育管理实践路径'},
              {title:'> 贵州遵义立足资源优势，探索构建红色文化育人体系'},
              {title:'> 党建引领促脱贫'},
              {title:'> “支部引领-村社合一”壮大村级集体经济'}],
            [{title:'> 以新金融履践初心使命锻造政治忠诚'},
              {title:'> 发挥党建引领作用'},
              {title:'> 哈尔滨工程大学:传承红色基因，铸就国家栋梁'},
              {title:'> 一线行走:只做小事儿的“老郭”'},
              {title:'> 减负不减责，见效盼长效'}]
          ],
          partymember:[
            {url:require('../assets/picture/优秀党员/毛雪峰.jpg'), title:'毛雪峰'},
            {url:require('../assets/picture/优秀党员/沈文枫.jpg'), title:'沈文枫'},
            {url:require('../assets/picture/优秀党员/叶飞跃.jpg'), title:'叶飞跃'},
            {url:require('../assets/picture/优秀党员/姜颖.jpg'), title:'姜颖'},
            {url:require('../assets/picture/优秀党员/梁霞.jpg'), title:'梁霞'},
            {url:require('../assets/picture/优秀党员/冯玉鑫.jpg'),title:'冯玉鑫'},
            {url:require('../assets/picture/优秀党员/林自强.jpg'), title:'林自强'},
            {url:require('../assets/picture/优秀党员/王武荣.jpeg'),title:'王武荣'}
          ],
          xinajinshiji:[
            {title:'邓志瑞：用欣赏和爱托起一片蓝天，培育好每一个学生'},
            {title:'钟杨：做牢记使命的奋斗者，鞠躬尽瘁，死而后已'},
            {title:'李友梅：立足大地，不懈耕耘'},
            {title:'张统一：在改革的新时代号角中弘扬科学家精神'},
            {title:'张建华：培育科技创新人才，凝聚团队科研精神'},
            {title:'陈青：育人为先，创新探索'}
          ],
          xianjinbanner:[
            {title:'学习路上',url:require('../assets/picture/activity_banner1.png'),content:'习总书记系列讲话'},
            {title:'学习有声',url:require('../assets/picture/activity_banner2.png'),content:'习总书记经典语录'},
            {title:'学习金句',url:require('../assets/picture/activity_banner3.png'),content:'习总书记重要论述'}
          ],
          comment:[
            {name:'李梅梅',content:'不忘初心，砥砺前行！'},
            {name:'朱正涛',content:'同志们一起努力，吧我国建设策划归纳为富强民主文明和谐美丽的社会主义现代化强国'},
            {name:'李嘉瑞',content:'向前辈们学习，吾辈当自强'},
            {name:'周树立',content:'做好本职工作，为中国梦而奋斗'},
            {name:'秦水生',content:'让生活更美好，让国家更富强'},
            {name:'陈秋安',content:'撸起袖子加油干！'},
            {name:'李安琪',content:'生为华夏人而自豪'},
            {name:'刘书瑞',content:'加油加油！空谈误国，实干兴邦'}
          ]
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
        }
      },
      mounted() {
        this.initClass()
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
    background: url("../assets/picture/party_background.jpg") no-repeat;
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
    background: url("../assets/picture/picture.png") no-repeat center center;
    background-size: cover;
    width: 26px;
    height: 26px;
    float: left;
    margin-top: 13px;
  }
  .focus-nav .list2 i{
    background: url("../assets/picture/video.png") no-repeat center center;
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
    background: url("../assets/picture/party-banner.jpg") no-repeat center center;
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

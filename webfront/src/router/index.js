import Vue from 'vue'
import Router from 'vue-router'
import Mainpage from '@/components/MainPage.vue'
import IndexPage from '@/components/IndexPage.vue'
import Diplomat from '@/components/diplomat.vue'
import Interview from '@/components/interview.vue'
import Modelparty from '@/components/ModelParty.vue'
import Window from '@/components/window.vue'
import Message from '@/components/message.vue'
import Exam from '@/components/exam_header.vue'
import RedScenery from '@/components/red_scenery.vue'
import News from '@/components/news_detail.vue'

Vue.use(Router);

export default new Router({
  mode:'history',
  routes: [
    // {
    //   path: '/',
    //   name: 'HelloWorld',
    //   component: HelloWorld
    // }
    {
      path:'/',
      name:'Mainpage',
      component:Mainpage,
      meta:{
        index:0,
        title:'欢迎页面'
      }
    },
    {
      path: '/home',
      name: 'IndexPage',
      component: IndexPage,
      meta:{
        index:1,
        title:'主界面'
      }
    },
    {
      path:'/diplomat',
      name:'Diplomat',
      component: Diplomat,
      meta:{
        index:2,
        title:'外交足迹'
      }
    },
    {
      path:'/interview',
      name:'Interview',
      component: Interview,
      meta:{
        index:2,
        title:'先辈寄语'
      }
    },
    {
      path:'/modelparty',
      name:'Modelarty',
      component:Modelparty,
      meta:{
        index:2,
        title:'模范党支部'
      }
    },
    {
      path:'/window',
      name:'Window',
      component:Window,
      meta:{
        index:2,
        title:'组织生活窗'
      }
    },
    {
      path:'/message',
      name:'Message',
      component:Message,
      meta:{
        index:2,
        title:'心得分享'
      }
    },
    {
      path:'/exam',
      name:'Exam',
      component:Exam,
      meta:{
        index:2,
        title:'模拟测验'
      }
    },
    {
      path:'/red_scenery',
      name:'RedScenery',
      component:RedScenery,
      meta:{
        index:2,
        title:'景点游览'
      }
    },
    {
      path: '/news',
      name: 'News',
      component: News,
      meta: {
        index:2,
        title: '新闻详情'
      }
    }
  ]
})

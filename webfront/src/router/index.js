import Vue from 'vue'
import Router from 'vue-router'
import Mainpage from '@/components/Mainpage.vue'
import IndexPage from '@/components/IndexPage.vue'
import Diplomat from '@/components/diplomat.vue'
import Interview from '@/components/interview.vue'
import Modelparty from '@/components/ModelParty.vue'
import Window from '@/components/window.vue'

Vue.use(Router);

export default new Router({
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
      meta:{index:0}
    },
    {
      path: '/home',
      name: 'IndexPage',
      component: IndexPage,
      meta:{index:1}
    },
    {
      path:'/diplomat',
      name:'Diplomat',
      component: Diplomat,
      meta:{index:2}
    },
    {
      path:'/interview',
      name:'Interview',
      component: Interview,
      meta:{index:2}
    },
    {
      path:'/modelparty',
      name:'Modelarty',
      component:Modelparty,
      meta:{index:2}
    },
    {
      path:'/window',
      name:'Window',
      component:Window,
      meta:{index:2}
    }
  ]
})

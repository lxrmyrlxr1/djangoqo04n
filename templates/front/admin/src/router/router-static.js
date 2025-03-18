import Vue from 'vue';

import VueRouter from 'vue-router'
Vue.use(VueRouter);

import Index from '@/views/index'
import Home from '@/views/home'
import Board from '@/views/board'
import Login from '@/views/login'
import NotFound from '@/views/404'
import UpdatePassword from '@/views/update-password'
import pay from '@/views/pay'
import register from '@/views/register'
import center from '@/views/center'
    import systemintro from '@/views/modules/systemintro/list'
    import mingsuxinxi from '@/views/modules/mingsuxinxi/list'
    import menpiaoxinxi from '@/views/modules/menpiaoxinxi/list'



const routes = [{
    path: '/index',
    name: 'System Home',
    component: Index,
    children: [{
      path: '/',
      name: 'System Home',
      component: Home,
      meta: {icon:'', title:'center'}
    }, {
      path: '/updatePassword',
      name: 'Revise password',
      component: UpdatePassword,
      meta: {icon:'', title:'updatePassword'}
    }, {
      path: '/pay',
      name: 'pay',
      component: pay,
      meta: {icon:'', title:'pay'}
    }, {
      path: '/center',
      name: 'personal information',
      component: center,
      meta: {icon:'', title:'center'}
    }
      ,{
	path: '/systemintro',
        name: 'system introduce',
        component: systemintro
      }
      ,{
	path: '/mingsuxinxi',
        name: 'hotel Information',
        component: mingsuxinxi
      }
      ,{
	path: '/menpiaoxinxi',
        name: 'ticket information',
        component: menpiaoxinxi
      }
    ]
  },
  {
    path: '/login',
    name: 'login',
    component: Login,
    meta: {icon:'', title:'login'}
  },
  {
    path: '/board',
    name: 'board',
    component: Board,
    meta: {icon:'', title:'board'}
  },
  {
    path: '/register',
    name: 'register',
    component: register,
    meta: {icon:'', title:'register'}
  },
  {
    path: '/',
    name: 'System Home',
    redirect: '/index'
  },
  {
    path: '*',
    component: NotFound
  }
]

const router = new VueRouter({
  mode: 'hash',
  routes 
})
const originalPush = VueRouter.prototype.push
VueRouter.prototype.push = function push(location) {
   return originalPush.call(this, location).catch(err => err)
}
export default router;

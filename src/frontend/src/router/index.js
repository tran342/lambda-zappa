import Vue from 'vue'
import Router from 'vue-router'
import RiskTypeView from '@/components/RiskTypeView'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'RiskTypeView',
      component: RiskTypeView
    }
  ],
  mode: 'history'
})

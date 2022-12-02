import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/backups',
    name: 'backups',
    component: () => import(/* webpackChunkName: "backups" */ '../views/BackupsView.vue')
  },
  {
    path: '/servers',
    name: 'servers',
    component: () => import(/* webpackChunkName: "servers" */ '../views/ServersView.vue')
  },
  {
    path: '/customers',
    name: 'customers',
    component: () => import(/* webpackChunkName: "customers" */ '../views/CustomersView.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router

import find from 'lodash/find'
import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const state = {
  isAuthenticated: true,
  authErrorMessage: '',
  riskTypes: []
}

const getters = {
  getRiskTypes: state => state.riskTypes,
  getRiskTypeById: state => id => {
    return find(state.riskTypes, riskType => riskType.id === id)
  },
  getIsAuthenticated: state => {
    return state.isAuthenticated
  }
}

const actions = {
  requestRiskTypes ({commit}) {
    Vue.http.get('risk-types/').then(response => {
      commit('setRiskTypes', response.body)
    })
  }
}

const mutations = {
  setIsAuthenticated (state, isAuthenticated) {
    state.isAuthenticated = isAuthenticated
    state.authErrorMessage = ''
  },
  setRiskTypes (state, riskTypes = []) {
    state.riskTypes = riskTypes
  }
}

export default new Vuex.Store({
  state,
  getters,
  actions,
  mutations
})

import Vue from "vue";
import Vuex from "vuex";

import { api } from "./constants";
import locations from "./modules/locations";

Vue.use(Vuex);

const apiPlugin = store => {
  (store.load = function(commit, url, mutation) {
    api
      .get(url)
      .then(response => response.data)
      .then(data => {
        commit(mutation, data);
      });
  }),
    (store.create = function(commit, url, data, mutation) {
      api
        .post(url, data)
        .then(response => response.data)
        .then(data => {
          commit(mutation, data);
        });
    });
  store.update = function(commit, url, data, mutation) {
    api
      .put(url, data)
      .then(response => response.data)
      .then(data => {
        commit(mutation, data);
      });
  };
  store.delete = function(commit, url, data, mutation) {
    api
      .delete(url, data)
      .then(response => response.config)
      .then(data => {
        commit(mutation, data);
      });
  };
};

const statePlugin = store => {
  store.addInState = function(state, item) {
    state.push(item);
  };
  store.updateInState = function(state, newItem) {
    const toBeUpdated = state.find(element => element.id === newItem.id);
    Object.assign(toBeUpdated, newItem);
  };
  store.deleteFromState = function(state, item) {
    const toBeDeleted = state.find(element => element.id === item.id);
    state.splice(state.indexOf(toBeDeleted), 1);
  };
};

export default new Vuex.Store({
  modules: {
    locations
  },
  plugins: [apiPlugin, statePlugin]
});

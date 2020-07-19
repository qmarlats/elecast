export default {
  SET_LOCATIONS(state, locations) {
    state.locations = locations;
  },
  ADD_LOCATION(state, location) {
    this.addInState(state.locations, location);
  },
  UPDATE_LOCATION(state, location) {
    this.updateInState(state.locations, location);
  },
  DELETE_LOCATION(state, location) {
    this.deleteFromState(state.locations, location);
  }
};

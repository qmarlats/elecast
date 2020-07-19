export default {
  loadLocations({ commit }) {
    this.load(commit, "locations/", "SET_LOCATIONS");
  },
  createLocation({ commit }, location) {
    this.create(commit, "locations/create/", location, "ADD_LOCATION");
  },
  updateLocation({ commit }, location) {
    this.update(
      commit,
      `locations/${location.id}/update/`,
      location,
      "UPDATE_LOCATION"
    );
  },
  deleteLocation({ commit }, location) {
    this.delete(
      commit,
      `locations/${location.id}/delete/`,
      location,
      "DELETE_LOCATION"
    );
  }
};

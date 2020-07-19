<template>
  <e-crud-table
    :meta="meta"
    :headers="headers"
    :items="locations"
    :items-per-page="10"
    :fields="fields"
    store-create-action="locations/createLocation"
    store-update-action="locations/updateLocation"
    store-delete-action="locations/deleteLocation"
  ></e-crud-table>
</template>

<script>
import { mapState } from "vuex";
import ECRUDTable from "../components/ECRUDTable.vue";

export default {
  data() {
    return {
      meta: {
        objectName: "location",
        objectNamePlural: "locations"
      },
      headers: [
        { text: "Name", align: "start", value: "name" },
        { text: "Latitude", sortable: false, value: "latitude" },
        { text: "Longitude", sortable: false, value: "longitude" }
      ],
      fields: [
        {
          name: "name",
          label: "Name",
          required: true,
          counter: "50",
          cols: 12,
          rules: [
            v => !!v || "Name is required",
            v => (v && v.length <= 50) || "Name must be less than 50 characters"
          ]
        },
        {
          name: "latitude",
          label: "Latitude",
          cols: 6,
          rules: [
            v =>
              !v ||
              /^(\d{1,2})(\.)(\d{1,6})$/.test(v) ||
              "Invalid latitude format"
          ]
        },
        {
          name: "longitude",
          label: "Longitude",
          cols: 6,
          rules: [
            v =>
              !v ||
              /^(\d{1,2})(\.)(\d{1,6})$/.test(v) ||
              "Invalid longitude format"
          ]
        }
      ]
    };
  },
  mounted() {
    this.$store.dispatch("locations/loadLocations");
  },
  computed: {
    ...mapState("locations", ["locations"])
  },
  components: {
    "e-crud-table": ECRUDTable
  }
};
</script>

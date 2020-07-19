<template>
  <v-data-table
    :headers="headers"
    :items="items"
    :items-per-page="itemsPerPage"
    class="elevation-1"
  >
    <template v-slot:top>
      <v-toolbar flat>
        <v-toolbar-title>{{
          meta.objectNamePlural | capitalize
        }}</v-toolbar-title>

        <v-spacer></v-spacer>

        <v-dialog v-model="createUpdateDialog" max-width="500px">
          <template v-slot:activator="{ on, attrs }">
            <v-btn color="primary" dark class="mb-2" v-bind="attrs" v-on="on"
              >New {{ meta.objectName }}</v-btn
            >
          </template>

          <v-form
            ref="createUpdateForm"
            v-model="createUpdateFormValid"
            lazy-validation
            @submit.prevent
          >
            <v-card>
              <v-card-title>
                <span class="headline">{{ createUpdateFormTitle }}</span>
              </v-card-title>

              <v-card-text>
                <v-container>
                  <v-row>
                    <v-col
                      v-for="field in fields"
                      :key="field.name"
                      :cols="field.cols"
                    >
                      <v-text-field
                        v-model="selectedItem[field.name]"
                        :name="field.name"
                        :label="field.label"
                        :required="field.required ? true : false"
                        :counter="field.counter"
                        :rules="field.rules"
                      ></v-text-field>
                    </v-col>
                  </v-row>
                </v-container>
              </v-card-text>

              <v-card-actions>
                <v-spacer></v-spacer>

                <v-btn
                  color="grey darken-1"
                  text
                  @click="closeCreateUpdateDialog"
                  >Cancel</v-btn
                >
                <v-btn
                  type="submit"
                  color="blue darken-1"
                  text
                  @click="saveItem"
                  >Save</v-btn
                >
              </v-card-actions>
            </v-card>
          </v-form>
        </v-dialog>

        <v-dialog v-model="deleteDialog" max-width="290px">
          <v-form ref="deleteForm" @submit.prevent>
            <v-card>
              <v-card-title>
                <span class="headline">Delete {{ meta.objectName }}</span>
              </v-card-title>

              <v-card-text>
                Are you sure you want to delete the {{ meta.objectName }}
                <strong>{{ selectedItem.name }}</strong
                >?
              </v-card-text>

              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="grey darken-1" text @click="closeDeleteDialog"
                  >Cancel</v-btn
                >
                <v-btn
                  type="submit"
                  color="red darken-1"
                  text
                  @click="deleteItem"
                  >Delete</v-btn
                >
              </v-card-actions>
            </v-card>
          </v-form>
        </v-dialog>
      </v-toolbar>
    </template>

    <template v-slot:item.actions="{ item }">
      <v-icon
        class="mr-2"
        color="primary"
        @click="openCreateUpdateDialog(item)"
      >
        mdi-pencil
      </v-icon>
      <v-icon color="red" @click="openDeleteDialog(item)">
        mdi-delete
      </v-icon>
    </template>
  </v-data-table>
</template>

<script>
export default {
  props: [
    "headers",
    "items",
    "itemsPerPage",
    "meta",
    "fields",
    "storeCreateAction",
    "storeUpdateAction",
    "storeDeleteAction"
  ],
  data() {
    return {
      createUpdateDialog: false,
      deleteDialog: false,
      createUpdateFormValid: true,
      defaultItem: {},
      selectedItem: {},
      selectedItemIndex: -1
    };
  },
  methods: {
    _selectItem(item) {
      this.selectedItemIndex = this.items.indexOf(item);
      this.selectedItem = Object.assign({}, item);
    },
    _closeDialog() {
      this.$nextTick(() => {
        this.selectedItem = Object.assign({}, this.defaultItem);
        this.selectedItemIndex = -1;
      });
    },
    openCreateUpdateDialog(item) {
      this._selectItem(item);
      this.createUpdateDialog = true;
    },
    openDeleteDialog(item) {
      this._selectItem(item);
      this.deleteDialog = true;
    },
    closeCreateUpdateDialog() {
      this.createUpdateDialog = false;
      this.$refs.createUpdateForm.resetValidation();
      this._closeDialog();
    },
    closeDeleteDialog() {
      this.deleteDialog = false;
      this._closeDialog();
    },
    saveItem() {
      if (this.selectedItemIndex > -1) {
        this.$store.dispatch(this.storeUpdateAction, this.selectedItem);
      } else {
        this.$store.dispatch(this.storeCreateAction, this.selectedItem);
      }
      this.closeCreateUpdateDialog();
    },
    deleteItem() {
      this.$store.dispatch(this.storeDeleteAction, this.selectedItem);
      this.closeDeleteDialog();
    }
  },
  mounted() {
    this.headers.push({
      text: "Actions",
      align: "end",
      sortable: false,
      value: "actions"
    });
    this.fields.forEach(
      field => (this.defaultItem[field.name] = field.defaultValue || null)
    );
    this.selectedItem = this.defaultItem;
  },
  computed: {
    createUpdateFormTitle() {
      return this.selectedItemIndex === -1
        ? `New ${this.meta.objectName}`
        : `Edit ${this.meta.objectName}`;
    }
  },
  watch: {
    createUpdateDialog(val) {
      val || this.closeCreateUpdateDialog();
    },
    deleteDialog(val) {
      val || this.closeDeleteDialog();
    }
  },
  filters: {
    capitalize: function(str) {
      return str.charAt(0).toUpperCase() + str.slice(1);
    }
  }
};
</script>

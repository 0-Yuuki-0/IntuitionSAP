<template>
  <div id="main-content">
    <div class="page-heading">
      <h3>Clinics</h3>
    </div>
    <div class="page-content">
        <section class="row">
            <div class="col-12">
                <div class="card">
                    <div class="card-header">
                        <h4>All Clinics</h4>
                    </div>
                    <div class="card-body ">
                        <table class='table table-hover'>
                            <thead>
                                <tr>
                                    <th>#</th>
                                    <th>Name</th>
                                    <th>Location</th>
                                    <th>State</th>
                                    <th>Address</th>
                                    <th>Action</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr v-for="(clinic, index) in clinics" :key="index">
                                    <td>{{index+1}}</td>
                                    <td>{{clinic.name}}</td>
                                    <td>{{clinic.addr_country}}</td>
                                    <td>{{clinic.addr_state}}</td>
                                    <td>{{clinic.addr_line_1}}</td>
                                    <td>
                                        <button class='btn btn-warning'>Edit</button>
                                        <button class='btn btn-danger' @click="deleteClinic(clinic.id)">Delete</button>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </section>
    </div>
  </div>
</template>

<script>
export default {
  layout: 'sidebar-user',
  data() {
      return {
          clinics: []
      }
  },
  mounted() {
      this.getClinics() 
  },
  methods: {
    getClinics() {
      this.$axios.get('/api/clinics')
        .then(res => {
          console.log(res.data);
          this.clinics = res.data;
        });
    },
    deleteClinic(id) {

    }
  }
};
</script>
<style lang="scss">
    .alarm-icon {
        font-size: 4rem;
    }
</style>
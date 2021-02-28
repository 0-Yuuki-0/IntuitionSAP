<template>
  <div id="main-content">
    <div class="page-heading">
      <h3>New Appointment</h3>
    </div>
    <div class="page-content">
        <section class="row">
            <div class="col-12 col-md-6">
                <div class="card">
                    <div class="card-header">
                        <h4>Appointment Form</h4>
                    </div>
                    <div class="card-body">
                        <div class="mb-3">
                            <label for="name" class="form-label">Choose Hospital/Clinic</label>
                            <select name="" class='form-control' id=""  v-model="clinic">
                                <option value="" v-for="(clinic, index) in clinics" :key="index">{{clinic.name}}</option>
                            </select>
                        </div>
                        <div class="mb-3">
                            <label for="name" class="form-label">Choose Appointment Date</label>
                            <input type="date" class="form-control" id="name" placeholder="John Doe" v-model="date">
                        </div>
                        <div class="mb-3">
                            <label for="">Appointment Time</label>
                            <input type="time" name="" class='form-control' v-model="time" id="">
                            <button class="btn btn-primary float-end" @click="submit">Submit</button>
                        </div>
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
  methods: {
    addAppointment() {
      this.$axios.post()
    },
    getClinics() {
      this.$axios.get('/api/clinics')
        .then(res => {
          this.clinics = res.data;
          
        });
    },
    submit() {
      this.$axios.get('/api/appointments', {clinic: this.clinic, date_time: `${this.date} ${this.time}`, patient: this.$store.state.user.id})
        .then(res => {
          console.log(res.data)
        });
    },
  },
  mounted() {
    this.getClinics();
  },
  data() {
    return {
      clinics: [],
      clinic: '',
      date: '',
      time: '',
    };
  },
};
</script>
<style lang="scss">
    .alarm-icon {
        font-size: 4rem;
    }
</style>
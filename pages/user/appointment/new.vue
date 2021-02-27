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
                            <label for="name" class="form-label">Your Name</label>
                            <input type="email" class="form-control" id="name" placeholder="John Doe">
                        </div>
                        <div class="mb-3">
                            <label for="name" class="form-label">Choose Appointment Date</label>
                            <input type="date" class="form-control" id="name" placeholder="John Doe">
                        </div>
                        <div class="mb-3">
                            <label for="">Available Appointment Time (Choose one)</label>
                            <div class="form-check">
                                <input class="form-check-input" type="radio" name="flexRadioDefault" id="flexRadioDefault1">
                                <label class="form-check-label" for="flexRadioDefault1">
                                    09:00
                                </label>
                            </div>
                            <div class="form-check">
                                <input class="form-check-input" type="radio" name="flexRadioDefault" id="flexRadioDefault1">
                                <label class="form-check-label" for="flexRadioDefault1">
                                    10:00
                                </label>
                            </div>
                            <div class="form-check">
                                <input class="form-check-input" type="radio" name="flexRadioDefault" id="flexRadioDefault1">
                                <label class="form-check-label" for="flexRadioDefault1">
                                    13:00
                                </label>
                            </div>
                            <button class="btn btn-primary float-end">Submit</button>
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
  data() {
    return {
      peoplesVaccined: {
        annotations: {
          position: "back",
        },
        dataLabels: {
          enabled: false,
        },
        chart: {
          type: "bar",
        },
        fill: {
          opacity: 1,
        },
        plotOptions: {},
        series: [
          {
            name: "People",
            data: [9, 20, 30, 20, 10, 20, 30, 20, 10, 20, 30, 20],
          },
        ],
        colors: "#435ebe",
        xaxis: {
          categories: [
            "Jan",
            "Feb",
            "Mar",
            "Apr",
            "May",
            "Jun",
            "Jul",
            "Aug",
            "Sep",
            "Oct",
            "Nov",
            "Dec",
          ],
        },
      },
    };
  },
};
</script>
<style lang="scss">
    .alarm-icon {
        font-size: 4rem;
    }
</style>
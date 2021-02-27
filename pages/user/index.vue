<template>
  <div id="main-content">
    <div class="page-heading">
      <h3>Appointments</h3>
    </div>
    <div class="page-content">
        <section class="row">
            <div class="col-12">
                <div class="card">
                    <div class="card-header">
                        <h4>Upcoming Appointment</h4>
                    </div>
                    <!-- <div class="card-body text-center">
                        <i class='bi bi-alarm-fill alarm-icon'></i>
                        <h3>Next appointment in:</h3>
                        <h1>1 days 10 hours 3 minutes 60 secs</h1>
                        <button class="btn btn-lg btn-primary">Check in</button>
                    </div> -->

                    <!-- If havent make any appointmeny -->
                    <div class="card-body text-center">
                        <h3>You have not made any appointment yet</h3>
                        <nuxt-link :to="{name: 'user-appointment-new'}" class="btn btn-primary btn-lg">Make an Appointment Now</nuxt-link>
                    </div>
                </div>
            </div>
        </section>
        <section class="row">
            <div class="col-12">
                <div class="card">
                    <div class="card-header">
                        <h4>All Appointments</h4>
                    </div>
                    <div class="card-body">
                        <table class="table table-hover">
                            <thead>
                                <tr>
                                    <th>#</th>
                                    <th>Clinic Location</th>
                                    <th>Date</th>
                                    <th>Time</th>
                                    <th>Doctor Name</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td>32315</td>
                                    <td>Singapore Hospital</td>
                                    <td>02 Mar 2021</td>
                                    <td>14:00</td>
                                    <td>Dr. John</td>
                                </tr>
                                <tr>
                                    <td>32315</td>
                                    <td>Malaysia Hospital</td>
                                    <td>16 Mar 2021</td>
                                    <td>10:00</td>
                                    <td>Dr. John</td>
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
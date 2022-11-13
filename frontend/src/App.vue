<template>
  <div id="app">
    <router-view/>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <div class="container">
        <a class="navbar-brand" href="#">Navbar</a>
        <button
            class="navbar-toggler"
            type="button"
            data-mdb-toggle="collapse"
            data-mdb-target="#navbarNav"
            aria-controls="navbarNav"
            aria-expanded="false"
            aria-label="Toggle navigation"
        >
          <i class="fas fa-bars"></i>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav">
            <li class="nav-item">
              <a class="nav-link active" aria-current="page" href="{% url 'home' %}">Home</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="{% url 'download_index' %}">Download Index</a>
            </li>
          </ul>
        </div>
      </div>
    </nav>
    <div class="container mt-5">
      <div class="row justify-content-center">
        <div class="col-lg-6 text-center">
          <table class="table">
            <thead class="table-primary">
            <tr>
              <th scope="col">Index</th>
              <th scope="col">Cena</th>
            </tr>
            </thead>
            <tbody>
            <tr>
              <td></td>
              <td></td>
            </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name: 'App',

}
</script>

<style>

</style>

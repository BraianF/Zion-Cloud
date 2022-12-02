<template>
    <!-- Navbar -->
<nav class="navbar navbar-expand navbar-white navbar-light" id="navbar">
    <!-- Left navbar links -->
    <router-link class="brand-link" to="/">
        <img src="img/zion.svg" alt="AdminLTE Logo" class="brand-image img-circle elevation-3" style="opacity: .8">
    </router-link>
    
    <ul class="navbar-nav">
      
      <li class="nav-item d-none d-sm-inline-block">
        <router-link class="nav-link" to="/">Home</router-link>
      </li>
      <li class="nav-item d-none d-sm-inline-block">
        <router-link class="nav-link" to="/backups">Backups</router-link>
      </li>
      <li class="nav-item d-none d-sm-inline-block">
        <router-link class="nav-link" to="/servers">Servidores</router-link>
      </li>
      <li class="nav-item d-none d-sm-inline-block">
        <router-link class="nav-link" to="/customers">Clientes</router-link>
      </li>
    </ul>

    <!-- Right navbar links -->
    <ul class="navbar-nav ml-auto">
      <!-- Notifications Dropdown Menu -->
      <li class="nav-item dropdown">
        <a class="nav-link" data-toggle="dropdown" href="#">
          <i class="far fa-bell"></i>
          <span class="badge badge-warning navbar-badge">5</span>
        </a>
        <div class="dropdown-menu dropdown-menu-lg dropdown-menu-right">
          <span class="dropdown-item dropdown-header">5 Notifications</span>
          <div class="dropdown-divider"></div>
          <a href="#" class="dropdown-item">
            <i class="fa-solid fa-file-circle-exclamation mr-2"></i> 5 Backups precisam de atenção
            <span class="float-right text-muted text-sm">3 mins</span>
          </a>
          <div class="dropdown-divider"></div>
        </div>
      </li>
      <li class="nav-item">
        <a class="nav-link" data-widget="fullscreen" href="#" role="button">
          <i class="fas fa-expand-arrows-alt"></i>
        </a>
      </li>
    </ul>
  </nav>
  <!-- /.navbar -->
</template>

<script>
export default {
  name : "Navbar",
}
</script>

<style scoped>
   #navbar{
    border-bottom: 1px solid #dee2e6;
   }
</style>
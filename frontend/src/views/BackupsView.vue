<template>
    <div class="main-container">
        <div>
            <h1>Gerenciar Backups:</h1>
            <Message :msg="msg" v-show="msg" />
        </div>
    <div id="backup-table" v-if="backups">
      <div>
        <div id="backup-table-heading">
          <div class="backup-id">ID:</div>
          <div>Descrição:</div>
          <div>Servidor:</div>
          <div>Retenção (dias):</div>
          <div>Ativo:</div>
          <div>Ações:</div>
        </div>
      </div>
      <div id="backup-table-rows">
        <div class="backup-table-row" v-for="backup in backups" :key="backup.pk">
          <div class="backup-number">{{ backup.pk }}</div>
          <div>{{ backup.description }}</div>
          <div>{{ backup.server_name }}</div>
          <div>{{ backup.daily_retention }}</div>
          <div>{{ backup.active }}</div>
          <div>
            <button class="btn btn-danger" @click="deleteBackup(backup.pk)">Apagar</button>
          </div>
        </div>
      </div>
    </div>
    <div v-else>
      <h2>Não há backups cadastrados!</h2>
    </div>
</div>
  </template>
  
<script>
    export default {
      name: "BackupsView",
      data() {
        return {
          backups: null,
          backup_id: null,
        }
      },
      methods: {
        async getBackups() {
          const req = await fetch('http://172.16.31.197:8000/api/backups/')
  
          const data = await req.json()
          console.log(data)
          
          if (data.results.length > 0){
            this.backups = data.results
          } else {
            this.backups = null
          }
  
        },
        async deleteBackup(pk) {
  
          const req = await fetch(`http://172.16.31.197:8000/api/backups/${pk}`, {
            method: "DELETE"
          });
  
          //console.log(req)
          if(req.ok){

          }
          this.getBackups()
  
        },
      },
      mounted () {
      this.getBackups()
      }
    }
  </script>
  
  <style scoped>
    #backup-table {
      max-width: 1200px;
      margin: 0 auto;
    }
  
    #backup-table-heading,
    #backup-table-rows,
    .backup-table-row {
      display: flex;
      flex-wrap: wrap;
    }
  
    #backup-table-heading {
      font-weight: bold;
      padding: 12px;
      border-bottom: 3px solid #333;
    }
  
    .backup-table-row {
      width: 100%;
      padding: 12px;
      border-bottom: 1px solid #CCC;
    }
  
    #backup-table-heading div,
    .backup-table-row div {
      width: 19%;
    }
  
    #backup-table-heading .backup-id,
    .backup-table-row .backup-number {
      width: 5%;
    }
  
    select {
      padding: 12px 6px;
      margin-right: 12px;
    }
  
    .delete-btn {
      background-color: #222;
      color:#fcba03;
      font-weight: bold;
      border: 2px solid #222;
      padding: 10px;
      font-size: 16px;
      margin: 0 auto;
      cursor: pointer;
      transition: .5s;
    }
    
    .delete-btn:hover {
      background-color: transparent;
      color: #222;
    }
    .main-container {
        margin: 50px;
        min-height: 250px;
    }

    h1 {
        text-align: center;
        font-size: 42px;
        margin-bottom: 30px;
        color: #222;
    }
    h2 {
        text-align: center;
        margin-bottom: 30px;
        color: #222;
    }
  </style>
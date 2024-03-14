<script lang="ts">
  import '../app.css';
  export let title = "Default Title"; // Puoi impostare un titolo predefinito o passarlo come prop
</script>

<div class="min-h-screen flex flex-col">
  <header class="bg-blue-500 text-white p-4">
    <h1 class="text-xl">{title}</h1>
  </header>

  <main class="flex-1 p-4">
    <slot></slot> <!-- Il contenuto specifico della pagina verrà inserito qui -->
  </main>

  <footer class="bg-gray-700 text-white p-4 text-center">
    Table Soccer Tournament &copy; {new Date().getFullYear()}
  </footer>
</div>

<style>
  /* Qui puoi aggiungere stili specifici del layout */
</style>

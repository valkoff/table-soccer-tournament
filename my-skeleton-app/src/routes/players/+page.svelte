<script lang="ts">
	import { onMount } from 'svelte';
	import { players } from '../../stores/playerStore';
	import { getPlayers, addPlayer, deletePlayer, type Player } from '$lib/api';

	let newName = '';

	onMount(async () => {
		const fetchedPlayers = await getPlayers();
		players.set(fetchedPlayers);
	});

	async function handleAddPlayer() {
		try {
			const player = {
				name: newName
			} as Player;
			const newPlayer = await addPlayer(player);

			players.update((currentPlayers) => [...currentPlayers, newPlayer]);

			newName = ''; // Reset input field
		} catch (error) {
			console.error("Errore nell'aggiunta del giocatore:", error);
		}
	}

	async function handleDeletePlayer(player: Player) {
		try {
			await deletePlayer(player);
			players.update((currentPlayers) => currentPlayers.filter((p) => p.id !== player.id));
		} catch (error) {
			console.error("Errore nell'eliminazione del giocatore:", error);
		}
	}
</script>

<div class="p-4">
	<div class="card p-4">
		<h1 class="text-2xl font-bold mb-4">Create Player</h1>
		<form>
			<div class="sm:col-span-4">
				<label for="username" class="block text-sm font-medium leading-6">Username</label>
				<div class="mt-2">
					<div
						class="flex rounded-md shadow-sm ring-1 ring-inset ring-gray-300 focus-within:ring-2 focus-within:ring-inset focus-within:ring-indigo-600 sm:max-w-md"
					>
						<input
							type="text"
							bind:value={newName}
							name="username"
							id="username"
							autocomplete="username"
							class="block flex-1 border-0 bg-transparent py-1.5 pl-1 focus:ring-0 sm:text-sm sm:leading-6"
						/>
					</div>
				</div>
			</div>
			<div class="flex items-center justify-end gap-x-6">
				<button type="button" class="text-sm font-semibold leading-6 text-gray-900">Cancel</button>
				<button
					on:click={handleAddPlayer}
					class="rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
					>Save</button
				>
			</div>
		</form>
	</div>

	<div class="card p-4 mt-8">
		<h2 class="text-2xl font-bold mb-4">Players</h2>

		<ul role="list" class="divide-y divide-gray-100 mt-4">
			{#each $players as player}
				<li class="flex justify-between gap-x-6 py-5">
					{player.name}
					<button
						class="bg-red-500 hover:bg-red-700 text-white font-bold py-1 px-2 rounded-full text-xs"
						on:click={() => handleDeletePlayer(player)}
					>
						Elimina
					</button>
				</li>
			{/each}
		</ul>
	</div>
</div>

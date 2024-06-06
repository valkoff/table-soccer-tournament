<script lang="ts">
	import type { Player } from '$lib/api'; // Assumi di avere definito questo tipo altrove
	export let players: Player[] = [];
	export let selectedId: number | undefined = undefined;

	// Evento dispatch per notificare il componente genitore quando viene selezionato un giocatore
	import { createEventDispatcher } from 'svelte';
	const dispatch = createEventDispatcher();

	function handleChange(event: Event) {
		const selectedPlayerId = +(event.target as HTMLSelectElement).value;
		dispatch(
			'select',
			players.find((p) => p.id === selectedPlayerId)
		);
	}
</script>

<select on:change={handleChange} class="select">
	<option value="" disabled selected={selectedId === undefined}>Seleziona un giocatore...</option>
	{#each players as player}
		<option value={player.id} selected={player.id === selectedId}>
			{player.name}
		</option>
	{/each}
</select>
